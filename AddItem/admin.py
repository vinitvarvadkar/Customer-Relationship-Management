from django.contrib import admin
from . models import Item

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 3
    

admin.site.register(Item,ItemAdmin)
