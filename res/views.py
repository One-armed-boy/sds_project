from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from .models import Res,Review
from accounts.models import AppUser
from .serializers import ResSerializer,ReviewSerializer
from rest_framework.views import APIView
from django.utils import timezone
import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds
import json
# Create your views here.

def id_to_String(dic):
    for i in dic:
        i['res']=Res.objects.get(id=i['res']).name
    return dic
class res_detail(APIView):
    def get(self,request,res_id):
        res=get_object_or_404(Res, pk=res_id)
        serializer = ResSerializer(res)
        return Response(serializer.data)

class Recommendation(APIView):
    def get(self,request):
        res_df=pd.DataFrame(Res.objects.values_list('id'),columns=['id'])
        review_df=pd.DataFrame(Review.objects.values_list('author','res','score'),columns=['author','res','score'])
        user_res_pivot=review_df.pivot(index='author',columns='res',values='score').fillna(0)
        matrix=np.array(user_res_pivot)
        user_score_mean=np.mean(matrix,axis=1)
        matrix-=user_score_mean.reshape(-1,1)
        U, sigma, Vt=svds(matrix, k=1)
        sigma = np.diag(sigma)
        preds=pd.DataFrame(np.dot(np.dot(U,sigma),Vt),columns=user_res_pivot.columns,index=user_res_pivot.index)
        user_preds=preds.loc[str(request.user)]
        res_preds=pd.DataFrame({'res':np.array(preds.columns),'score':np.array(user_preds)})
        visited_list=[i.res.id for i in Review.objects.filter(author=request.user)]
        res_preds_unvisited=res_preds[(res_preds['res'].isin(visited_list))!=True].sort_values('score',ascending=False)
        if len(res_preds)!=0:
            serializer = res_preds_unvisited.to_json(orient='records')
            return Response(json.loads(serializer))
        else:
            return Response('없다.')

class Visited(APIView):
    def get(self,request):
        res_list=Review.objects.filter(author=request.user).order_by('-score')
        if res_list:
            serializer = ReviewSerializer(res_list, many=True)
            return Response(id_to_String(serializer.data))
        else:
            return Response('없다.')

class add_res(APIView):
    def get(self,request): return

    def post(self,request):
        serializer = ResSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            new_Res_id=Res.objects.get(name=serializer.name).id
            user_all=[i.id for i in AppUser.objects.all()]
            for user in user_all:
                review_serial=ReviewSerializer({'author':user,'res':new_Res_id,'score':0,'comment':'','create_date':timezone.now()})
                if review_serial.is_valid():
                    review_serial.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class scoring(APIView):
    def post(self,request):
        serializer = ReviewSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)