from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import InPic, OutPic, SegPic
from deep.humony_inference_url import *
from rest_framework.views import APIView
from config.settings import SERVERURL
class inpic(APIView):
    def post(self, request, format=None):
        i = InPic.objects.create(before = self.request.data["before"])
        cutimage = humony_segment(str("{0}{1}".format(SERVERURL, i.before)))
        s = SegPic.objects.create(in_id = i ,ing = cutimage[1], color_list=cutimage[2])
        response_data= "{\\r\\n       "+  "'before':"+ str("'{0}{1}'".format(SERVERURL, i.before)) +",\\r\\n         "+"'ing':"+ str("'{0}{1}'".format('http://127.0.0.1:8000/', s.ing)) + ",\\r\\n            " + "'color_list':"+ str(s.color_list) +"\\r\\n             }"
        return Response(response_data, status=201)



class outpic(APIView):
    def post(self, request, format=None):
        i = self.request.data["before"]
        i = i[:len(SERVERURL)]
        s = self.request.data["ing"]
        s = s[:len(SERVERURL)]
        cl = self.request.data["color_list"]
        cs = self.request.data["color_sel"]        
        r = humony_selcut(i, s, cl, cs)
        OutPic(after=r, origin_id_id=id).save()
        response_data = "{   \r    "+  "'after':"+ r.after +"   \n    }"
        return Response(response_data, status=201)
