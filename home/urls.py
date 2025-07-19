
from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_selection, name='role_selection'),
]
