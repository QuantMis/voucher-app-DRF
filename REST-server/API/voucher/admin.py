from django.contrib import admin
from .models import Voucher, Product, Order, History

# Register your models here.
admin.site.register(Voucher)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(History)
