# tarifler/urls.py

from django.urls import path
from . import views 

urlpatterns = [
    # 1. ÖNCE: Spesifik adres olan 'ekle/' gelir
    path('ekle/', views.tarif_ekle, name='tarif_ekle'),
    
    # Düzenleme, Silme ve Favori yolları
    path('<int:pk>/duzenle/', views.tarif_duzenle, name='tarif_duzenle'),
    path('<int:pk>/sil/', views.tarif_sil, name='tarif_sil'),
    
    # YENİ EKLENEN SATIR: Favori Ekle/Kaldır İşlemi
    # <int:tarif_id> kullanıldı (views.py'deki fonksiyona uygun olması için)
    path('favori/<int:tarif_id>/', views.favori_ekle_kaldir, name='favori_ekle_kaldir'), 
    
    # 2. SONRA: Genel adres olan <int:pk>/ gelir
    path('<int:pk>/', views.tarif_detay, name='tarif_detay'),
]