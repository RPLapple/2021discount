from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from .models import Product, Supermarket, Card, ExtraDiscount


# Create your views here.
# urls.py那邊的 等等要刪掉
# from discount.views import register, index
# homepage/indexpage
def index(request):
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })


# all projects
def works(request):
    return render(request, 'works.html')


# discount page
def work_discount(request):
    items = Product.objects.values()
    super_name = Supermarket.objects.values()
    card_name = Card.objects.values()
    extra_dis = ExtraDiscount.objects.values()
    context = {'items': items, 'super_name': super_name, 'card_name': card_name, 'extra_dis': extra_dis, }
    return render(request, 'work_discount.html', context)


# 這邊要再看一次
# table是用來幹嘛的＝＝？
# show 資料在額外頁面
def table(request):
    data = Product.objects.values(
        'supermarket__name',
        'name',
        'discount',
        'new_price',
        'old_price',
        'discount__card__name',
        'discount__extradiscount__name',
    )
    return JsonResponse(list(data), safe=False)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def myaccount(request):
    return render(request, 'myaccount.html')


# 這邊要再看一次, 還有render的最後一個值是什麼？
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/account/login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())


# 這邊要再看一次, 還有render的最後一個值是什麼？
def login(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.ise_active:
        auth.login(request, user)
        return render(request, 'index.html')
    else:
        return render(request, 'registration/login.html', locals())


# 這邊要再看一次
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')