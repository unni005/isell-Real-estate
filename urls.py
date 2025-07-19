from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)

app_name = 'seller'

urlpatterns = [
    path('login/', views.seller_login, name='login'),
    path('logout/', views.seller_logout, name='logout'),
    path('register/', views.seller_register, name='register'),
    path('dashboard/', views.seller_dashboard, name='dashboard'),
    path('add-property/', views.add_property, name='add_property'),
    path('edit-property/<int:property_id>/', views.edit_property, name='edit_property'),
    path('delete-property/<int:property_id>/', views.delete_property, name='delete_property'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('view-bookings/', views.view_bookings, name='view_bookings'),
    path('complete-booking/<int:booking_id>/', views.complete_booking, name='complete_booking'),
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('', include(router.urls)),
    
]