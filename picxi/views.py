from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import InPic, OutPic, SegPic
from deep.humony_inference_url import *
from rest_framework.views import APIView
from config.settings import SERVERURL
from django.http import JsonResponse
class inpic(APIView):
    def post(self, request, format=None):
        i = InPic.objects.create(before = self.request.data["before"])
        cutimage = humony_segment(str("{0}{1}".format(SERVERURL, i.before)))
        s = SegPic.objects.create(ing = cutimage[1][2:], color_list=cutimage[2])
        response_data= {
                   'before': str("{0}{1}".format(SERVERURL, i.before)) ,
                   'ing': str("{0}{1}".format(SERVERURL, s.ing)) ,
                   'color_list': str(s.color_list)          
                   }
        return JsonResponse(response_data)

  

class outpic(APIView):
    def post(self, request, format=None):
        i = self.request.data["before"]
        i = i[len(SERVERURL):] 
        s = self.request.data["ing"]
        s = s[len(SERVERURL):]
        cl = self.request.data["color_list"]
        cs = self.request.data["color_sel"]        
        #print(i,s, cl, cs)
        r = humony_selcut(i, s, cl,list(map(int,cs)))
        OutPic.objects.create(after = r[2:])
        response_data = { 'after': str("{0}{1}".format(SERVERURL, r[2:])) }
        return JsonResponse(response_data)