from django.db import models
import hashlib
import random

class GUIDModel(models.Model):

    guid = models.CharField(primary_key=True, max_length=40)

    def save(self, *args, **kwargs):

      if not self.guid:
        self.guid = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()

      super(GUIDModel, self).save(*args, **kwargs)