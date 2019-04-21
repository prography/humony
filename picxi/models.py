from django.db import models
from picxi.util import GUIDModel
# Create your models here.

class InPic(GUIDModel):
    before = models.ImageField(upload_to='inpic/%Y/%m/%d/', blank=False)
    created = models.DateTimeField(auto_now_add=True)




class OutPic(GUIDModel):
    origin_id = models.ForeignKey(InPic, on_delete=models.CASCADE)
    after = models.ImageField(upload_to='outpic/%Y/%m/%d/', blank=False)
    created = models.DateTimeField(auto_now_add=True)
