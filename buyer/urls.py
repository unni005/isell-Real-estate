from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import VisitBookingViewSet 


router = DefaultRouter()
router.register(r'bookings', VisitBookingViewSet)

app_name = 'buyer'

urlpatterns = [
    path('login/', views.buyer_login, name='login'),
    path('logout/', views.buyer_logout, name='logout'),
    path('register/', views.buyer_register, name='register'),
    path('dashboard/', views.buyer_dashboard, name='dashboard'),
    path('book-visit/<int:property_id>/', views.book_visit, name='book_visit'),

    path('', include(router.urls)),
]
