from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from .models import Res,Review
from .serializers import ResSerializer,ReviewSerializer
# Create your views here.

@api_view(['GET'])
def res_detail(request,res_id):
    res=get_object_or_404(Res,pk=res_id)
    serializer=ResSerializer(res)
    return Response(serializer.data)

@api_view(['GET'])
def visited_res(request,author_id):
    visited_list=Review.objects.filter(author=author_id,is_pred=False).order_by('-score')
    if visited_list:
        serializer=ReviewSerializer(visited_list,many=True)
        return Response(serializer.data)
    else:
        return Response('없다.')

@api_view(['GET'])
def unvisited_res(request,author_id):
    unvisited_list=Review.objects.filter(author=author_id,is_pred=True).order_by('-score')
    if unvisited_list:
        serializer=ResSerializer(unvisited_list,many=True)
        return Response(serializer.data)
    else:
        return Response('없다')

