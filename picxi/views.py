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
from deep.humony_inference_url import *
# from config.settings import MEDIA_URL

@api_view(['POST'])
def InPicCreate(request):
    iserializer = InPicSerializer(data=request.data)
    if iserializer.is_valid():
        iserializer.save()
        Image = iserializer.data.get('before')
        id = iserializer.data.get('guidmodel_ptr_id')
        cutimage = humony("{0}{1}".format('http://127.0.0.1:8000', Image))
        # print(cutimage+"이거다"+id)
        OutPic(after=cutimage, origin_id_id=id).save()
        return Response(iserializer.data, status=status.HTTP_201_CREATED)
    return Response(iserializer.error)


class InPicList(generics.ListCreateAPIView):
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
   # permission_classes = (IsAuthenticated,)
    queryset = InPic.objects.all()
    serializer_class = InPicSerializer


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

