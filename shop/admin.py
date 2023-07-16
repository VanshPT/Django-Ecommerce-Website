from django.contrib import admin
from .models import Product,Contact,Orders
admin.site.register(Product)
# Register your models here.
admin.site.register(Contact)
admin.site.register(Orders)