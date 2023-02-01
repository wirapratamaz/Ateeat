from django.contrib import admin
from .models import BuyerUser, SellerUser

# Register your models here.
#models BuyerUser
class BuyerUserAdmin(admin.ModelAdmin):
    list_display = ['authority', 'name', 'email', 'phone_number', 'address', 'latitude', 'longitude']

class SellerUserAdmin(admin.ModelAdmin):
    list_display = ['authority', 'name', 'email', 'phone_number', 'address', 'latitude', 'longitude']

admin.site.register(BuyerUser, BuyerUserAdmin)
