from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='transferler'),
    path('<int:transfer_id>', views.detail, name='detail'),
    path('search', views.search, name='search'),
    path('addTransfer', views.transEkle, name='addTransfer'),

]