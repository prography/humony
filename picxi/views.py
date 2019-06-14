from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import InPic, OutPic, SegPic
from deep.humony_inference_url import *
from rest_framework.views import APIView

class inpic(APIView):
    def post(self, request, format=None):
        i = InPic.objects.create(before = self.request.data["before"])
        cutimage = humony_segment(str("{0}{1}".format('http://127.0.0.1:8000/', i.before)))
        s = SegPic.objects.create(in_id = i ,ing = cutimage[1], color_list=cutimage[2])
        response_data= "{       "+  "'before':"+ str("'{0}{1}'".format('http://127.0.0.1:8000/', i.before)) +",         "+"'ing':"+ str("'{0}{1}'".format('http://127.0.0.1:8000/', s.ing)) + ",            " + "'color_list':"+ str(s.color_list) +"             }"
        return Response(response_data, status=201)



class outpic(APIView):
    def post(self, request, format=None):
        i = self.request.data["before"]
        s = self.request.data["ing"]
        cl = self.request.data["color_list"]
        cs = self.request.data["color_sel"]        
        r = humony_selcut(i, s, cl, cs)
        OutPic(after=r, origin_id_id=id).save()
        response_data=""
        for key,value in r.items():
            response_data+= "{       "+  "'after':"+ r.append(value) +"       }"
        return Response(response_data, status=201)
