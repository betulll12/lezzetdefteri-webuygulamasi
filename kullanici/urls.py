# kullanici/urls.py

from django.urls import path
from . import views 
from .views import KullaniciGirisView 
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    # Kullanıcı İşlemleri
    path('kayit/', views.kayit_ol, name='kayit_ol'),
    path('giris/', KullaniciGirisView.as_view(), name='giris'),

    # Kullanıcı çıkış sayfası (LogoutView kullanıldı)
    path('cikis/', LogoutView.as_view(next_page='/'), name='cikis'),
    
    # YENİ EKLENEN URL: Favori Listesi
    # Bu yol, views.py'deki favori_listesi fonksiyonunu çalıştırır.
    path('favorilerim/', views.favori_listesi, name='favori_listesi'),
]