from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from .models import Res,Review,Res_reserve
from accounts.models import AppUser
from .serializers import ResSerializer,ReviewSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,UpdateAPIView,GenericAPIView
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]
    def get(self,request,res_id):
        res=get_object_or_404(Res, pk=res_id)
        serializer = ResSerializer(res).data
        res_review_list=Review.objects.filter(res=res_id)
        if len(res_review_list)==0:
            serializer['score']=-1
        else:
            score_mean=sum([i.score for i in res_review_list])/len(res_review_list)
            serializer['score']=score_mean
        return Response(serializer)

class review_list(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,res_id):
        reviews=Review.objects.filter(res=res_id)
        if reviews:
            serializer=ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        else:
            return Response('없다.')

class Recommendation(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        res_df=pd.DataFrame(Res.objects.values_list('id'),columns=['id'])
        review_df=pd.DataFrame(Review.objects.values_list('author','res','score'),columns=['author','res','score'])
        user_res_pivot=review_df.pivot(index='author',columns='res',values='score').fillna(0)
        matrix=np.array(user_res_pivot)
        user_score_mean=np.mean(matrix,axis=1)
        matrix-=user_score_mean.reshape(-1,1)
        U, sigma, Vt=svds(matrix, k=1)
        sigma = np.diag(sigma)
        preds=pd.DataFrame(np.dot(np.dot(U,sigma),Vt)+user_score_mean.reshape(-1,1),columns=user_res_pivot.columns,index=user_res_pivot.index)
        user_preds=preds.loc[str(request.user)]
        res_preds=pd.DataFrame({'res':np.array(preds.columns),'score':np.array(user_preds)})
        visited_list=[i.res.id for i in Review.objects.filter(author=request.user)]
        res_preds_unvisited=res_preds[(res_preds['res'].isin(visited_list))!=True].sort_values('score',ascending=False)
        if len(res_preds)!=0:
            serializer = res_preds_unvisited.to_json(orient='records')
            return Response(id_to_String(json.loads(serializer)))
        else:
            return Response('없다.')

class Visited(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        res_list=Review.objects.filter(author=request.user).order_by('-score')
        if res_list:
            serializer = ReviewSerializer(res_list, many=True)
            return Response(id_to_String(serializer.data))
        else:
            return Response('없다.')

class add_res_reserve(CreateAPIView):
    queryset = Res_reserve.objects.all()
    serializer_class = ResSerializer
    permission_classes = [IsAuthenticated]

class scoring_create(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        author = get_object_or_404(AppUser,email=self.request.user)
        return serializer.save(author=author,create_date=timezone.now())

class scoring_update(UpdateAPIView,CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        queryset=self.get_queryset()
        obj = get_object_or_404(queryset,author=self.request.user,res=self.request.data.get('res',None))
        return obj
    def perform_update(self, serializer):
        author = get_object_or_404(AppUser,email=self.request.user)
        return serializer.save(author=author,create_date=timezone.now())

