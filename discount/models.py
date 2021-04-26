import datetime
from django.db import models
from django.contrib.auth.models import User
import sqlite3 as lite

con = lite.connect('db.sqlite3')
cur = con.cursor()
sql = "INSERT INTO contactpost (`email`, `subject`, `content`, `time`)"


# the card with special discount
class Card(models.Model):
    name = models.CharField(max_length=40)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Link card id & user id together
class AuthUserCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)


# different discount %
class ExtraDiscount(models.Model):
    discount = models.FloatField()


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
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)


# def scrap_info_from_super_market(self):
#     pass
