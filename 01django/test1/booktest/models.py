from django.db import models


# Create your models here.
class BookInfo(models.Model):
    """docstring for BookInfo"""
    btitle = models.CharField(max_length=100)
    bpubdate = models.DateField()
    bprice = models.FloatField()
    bnumber = models.IntegerField()

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    """"英雄表"""
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    hcomment = models.CharField(max_length=128)
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)

    def __str__(self):
        return self.hname