from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from .models import Res,Review
#from account_tmp.models import User
from .serializers import ResSerializer,ReviewSerializer
from rest_framework.views import APIView
from django.utils import timezone
# Create your views here.

def id_to_String(dic):
    for i in dic:
        i['author']=User.objects.get(id=i['author']).nickname
        i['res']=Res.objects.get(id=i['res']).name
    return dic

class res_detail(APIView):
    def get(self,request,res_id):
        res=get_object_or_404(Res, pk=res_id)
        serializer = ResSerializer(res)
        return Response(serializer.data)

class ResListUp(APIView):
    def get(self,request,is_pred,author_id):
        is_pred=True if is_pred==0 else False
        res_list=Review.objects.filter(author=author_id, is_pred=is_pred).order_by('-score')
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
            user_all=[i.id for i in User.objects.all()]
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