# kullanici/urls.py
from django.urls import path
from . import views 
from .views import KullaniciGirisView # Bu zaten vardı
from django.contrib.auth.views import LogoutView # YENİ IMPORT

urlpatterns = [
    path('kayit/', views.kayit_ol, name='kayit_ol'),
    path('giris/', KullaniciGirisView.as_view(), name='giris'),

    # YENİ EKLENEN: Kullanıcı çıkış sayfası
    path('cikis/', LogoutView.as_view(next_page='/'), name='cikis'),
]