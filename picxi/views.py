from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
#from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import InPic, OutPic
from .serializers import InPicSerializer, OutPicSerializer


class InPicList(generics.ListCreateAPIView):
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
   # permission_classes = (IsAuthenticated,)
    queryset = InPic.objects.all()
    serializer_class = InPicSerializer
    print("123")

class InPicDetail(generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
    #permission_classes = (IsAuthenticated,)
    queryset = InPic.objects.all()
    serializer_class = InPicSerializer

class OutPicList(generics.ListCreateAPIView):
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
   # permission_classes = (IsAuthenticated,)
    queryset = OutPic.objects.all()
    serializer_class =OutPicSerializer


class OutPicDetail(generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
    #permission_classes = (IsAuthenticated,)
    queryset = OutPic.objects.all()
    serializer_class = OutPicSerializer

