from django.db import models
from adminApp.models import item
from datetime import datetime

# Create your models here.
class userInfo(models.Model):
    userName = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "userInfo"
    
class myCart(models.Model):
    user = models.ForeignKey(userInfo,on_delete=models.CASCADE)
    item = models.ForeignKey(item,on_delete=models.CASCADE)
    qyt = models.IntegerField(default=1)

    class Meta:
        db_table  = "MyCart"

class orderMaster(models.Model):
    user = models.ForeignKey(userInfo,on_delete=models.CASCADE)
    date_of_order = models.DateField(default= datetime.now)
    amount = models.FloatField(default=1000)
    details = models.CharField(max_length=200)

    class Meta:
        db_table = 'orderMaster'
