from django.db import models

# Create your models here.

class Phb(models.Model):
    user=models.CharField(max_length=255,verbose_name='客户端')
    grade=models.IntegerField(verbose_name='分数')