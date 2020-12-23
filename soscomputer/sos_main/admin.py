from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'description', 'created', ]
    list_filter = [ 'created', 'name']

admin.site.register(Order,OrderAdmin)