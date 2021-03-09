from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as view_auth
from discount.views import register, index

# urls
# note: cyber security maybe can use uuid system?
urlpatterns = [
    path('', index),
    path('works', views.works, name='works'),
    path('work_discount', views.work_discount, name='work_discount'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('myaccount', views.myaccount, name='myaccount'),
    # 這啥= =?
    path('table', views.table, name='table'),
    path('accounts/register/', register),
    path('registration/login/', view_auth.LoginView.as_view(), name='login'),
    path('registration/logged_out', view_auth.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('accounts/profile/', index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)