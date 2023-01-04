from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Conversion(models.Model):
    ts = models.DateTimeField(auto_now=True)
    yt_url = models.CharField(max_length=255)
    file = models.FileField(upload_to='mp3/')
    user = models.ForeignKey(get_user_model(), models.CASCADE)
