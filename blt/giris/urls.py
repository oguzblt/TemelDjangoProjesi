from django.urls import path
from . import views

urlpatterns = [
    path('', views.ilksayfa, name='anasayfa'),
    path('menu3', views.ucuncusayfa, name='hakkmizda'),
]