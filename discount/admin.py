from django.contrib import admin

from .models import AuthUserCard, Card, ExtraDiscount, MemberPoint, Supermarket, Product


# from . import models  # NameError: name 'Card' is not defined
## reorganize the datas
# admin.site.register(models.ExtraDiscount)
# admin.site.register(models.AuthUserCard)
# admin.site.register(models.MemberPoint)
# admin.site.register(models.Card)
# admin.site.register(models.Supermarket)
# admin.site.register(models.Product)


class AuthUserCardAdmin(admin.ModelAdmin):
    list_display = ['user', 'card']


class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time']


class ExtraDiscountAdmin(admin.ModelAdmin):
    list_display = ['discount']


class MemberPointAdmin(admin.ModelAdmin):
    list_display = ['point', 'user', 'date', 'create_time']


class SupermarketAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'create_time']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['supermarket', 'name', 'discount', 'old_price', 'card', 'extra_discount', 'create_time']
    search_fields = ['supermarket', 'name', 'discount', 'old_price', 'card', 'extra_discount', 'create_time']


admin.site.register(AuthUserCard, AuthUserCardAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(ExtraDiscount, ExtraDiscountAdmin)
admin.site.register(MemberPoint, MemberPointAdmin)
admin.site.register(Supermarket, SupermarketAdmin)
admin.site.register(Product, ProductAdmin)
