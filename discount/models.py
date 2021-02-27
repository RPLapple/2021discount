import datetime
from datetime import date
from django.db import models
from django.contrib.auth.models import User

import sqlite3
# Create your models here.
# supermarkets' name


class Supermarket(models.Model):
    name = models.CharField(max_length=40)


# the card with special discount
class Card(models.Model):
    name = models.CharField(max_length=40)


# different discount %
class ExtraDiscount(models.Model):
    discount = models.FloatField()


# Link card id & user id together
class AuthUserCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)


# 如果有額外做delivery system 然後可以會員卡集點
# 先不寫進去，如果很閒再弄=.=
# member's Point
class MemberPoint(models.Model):
    point = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0, 0))

    # def get_point_by_date(self):
    #     if self.date < date(2021, 1, 1):
    #         return self.point * 2
    #     else:
    #         return self.point


# All Products
class Product(models.Model):
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    discount = models.FloatField()
    new_price = models.FloatField()
    old_price = models.FloatField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    extra_discount = models.ForeignKey(ExtraDiscount, on_delete=models.CASCADE)


def scrap_info_from_super_market(self):
    pass












