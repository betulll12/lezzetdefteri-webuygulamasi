# tarifler/urls.py

from django.urls import path
from . import views 

urlpatterns = [
    # 1. ÖNCE: Spesifik adres olan 'ekle/' gelir
    path('ekle/', views.tarif_ekle, name='tarif_ekle'),
    
    # YENİ EKLENEN URL'ler: Düzenleme ve Silme
    # pk kullanıldı (views.py'deki fonksiyonlara uygun olması için)
    path('<int:pk>/duzenle/', views.tarif_duzenle, name='tarif_duzenle'),
    path('<int:pk>/sil/', views.tarif_sil, name='tarif_sil'),
    
    # 2. SONRA: Genel adres olan <int:tarif_id>/ gelir (İsmi 'pk' olarak değiştirdim)
    # Detay sayfasının yolu, düzenleme ve silme yollarının ardından gelmelidir.
    path('<int:pk>/', views.tarif_detay, name='tarif_detay'),
]