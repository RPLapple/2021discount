from django.contrib import admin
from . import models

# Register your models here.
# so when we using http:../admin, we can adjust below datas
admin.site.register(models.ExtraDiscount)
admin.site.register(models.AuthUserCard)
admin.site.register(models.MemberPoint)
admin.site.register(models.Card)
admin.site.register(models.Supermarket)
admin.site.register(models.Product)