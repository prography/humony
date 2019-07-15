from django.db import models
from picxi.util import GUIDModel
# Create your models here.

class InPic(GUIDModel):
    before = models.ImageField(upload_to='dataset/inpic/%Y/%m/%d/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

class SegPic(GUIDModel):
    ing = models.ImageField(upload_to='dataset/segpic/%Y/%m/%d/', blank=True, null=True)
    color_list = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
class OutPic(GUIDModel):
    after = models.ImageField(upload_to='dataset/outpic/%Y/%m/%d/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
