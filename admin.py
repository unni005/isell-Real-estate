
from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'seller')
    search_fields = ('title', 'location', 'seller__username')
    list_filter = ('location',)

admin.site.register(Property, PropertyAdmin)