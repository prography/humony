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
        s = SegPic.objects.create(in_id = i ,ing = cutimage[1][2:], color_list=cutimage[2])
        return JsonResponse({
        'before' : str("'{0}{1}'".format(SERVERURL, i.before)),
        'ing' : str("'{0}{1}'".format('http://127.0.0.1:8000/', s.ing)),
        'colo_list' : str(s.color_list),
    }, json_dumps_params = {'ensure_ascii': True})



class outpic(APIView):
    def post(self, request, format=None):
        i = self.request.data["before"]
        i = i[len(SERVERURL):] 
        i = "../"+i
        s = self.request.data["ing"]
        s = s[len(SERVERURL):]
        s = "../"+s
        cl = self.request.data["color_list"]
        cs = self.request.data["color_sel"]  
        print(i)
        print(s)      
        r = humony_selcut(str(i), str(s), list(cl), list(cs))
        OutPic.objects.create(after=r)
        return JsonResponse({
        'after' : str("'{0}{1}'".format(SERVERURL, r.after)),
    }, json_dumps_params = {'ensure_ascii': True})
