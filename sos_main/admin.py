from django.contrib import admin
<<<<<<< HEAD
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'description', 'created', ]
    list_filter = [ 'created', 'name']

admin.site.register(Order,OrderAdmin)
=======

# Register your models here.
>>>>>>> 95fb2f6d9db3ba68a3ef6b02c5d212208fb09f7f
