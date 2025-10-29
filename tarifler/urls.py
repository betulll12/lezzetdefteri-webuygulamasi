# tarifler/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    # 1. ÖNCE: Spesifik adres olan 'ekle/' gelir
    path('ekle/', views.tarif_ekle, name='tarif_ekle'),
    
    # 2. SONRA: Genel adres olan <int:tarif_id>/ gelir
    path('<int:tarif_id>/', views.tarif_detay, name='tarif_detay'),
]