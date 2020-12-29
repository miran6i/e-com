from django.contrib import admin

# Register your models here.
from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)




#TODO: admin for products
#TODO: select for category in products
#TODO: filtering in categories
