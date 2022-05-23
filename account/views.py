from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def signup_view(request):
    return Response('HI')


@api_view(['GET'])
def login_view(request):
    return Response('HI')

@api_view(['GET'])
def logout_view(request):
    return Response('HI')