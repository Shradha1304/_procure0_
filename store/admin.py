from django.contrib import admin
from .models import product
from .category import Category
from .orders import Order
from .customer import Customer




# Register your models here.
admin.site.register(product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Customer)