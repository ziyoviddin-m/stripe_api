from django.contrib import admin

from item.models import Item



@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    list_filter =  ['name', 'price']
    search_fields = ['name', 'description']
    ordering = ['price', 'name']