import datetime
from datetime import date
from django.db import models
from django.contrib.auth.models import User

import sqlite3


# Create your models here.
# supermarkets' name


# the card with special discount
class Card(models.Model):
    name = models.CharField(max_length=40)
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    def __str__(self):
        return self.name


# Link card id & user id together
class AuthUserCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)


# different discount %
class ExtraDiscount(models.Model):
    discount = models.FloatField()


# 如果有額外做delivery system 然後可以會員卡集點
# 先不寫進去，如果很閒再弄=.=
# member's Point
class MemberPoint(models.Model):
    point = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0, 0))
    create_time = models.DateTimeField(auto_now=True)


class Supermarket(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40, default='Berlin')
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# All Products
class Product(models.Model):
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    discount = models.FloatField()
    new_price = models.FloatField()
    old_price = models.FloatField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    extra_discount = models.ForeignKey(ExtraDiscount, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now=True)


class ContactPost(models.Model):
    email = models.EmailField()
    subject = models.TextField()
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)



# def scrap_info_from_super_market(self):
#     pass
