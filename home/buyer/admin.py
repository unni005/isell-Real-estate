

from django.contrib import admin
from .models import VisitBooking

class VisitBookingAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'property', 'visit_date', 'created_at')
    list_filter = ('visit_date', 'created_at', 'property')
    search_fields = ('buyer__username', 'property__title', 'property__location')

admin.site.register(VisitBooking, VisitBookingAdmin)