# anasayfa/urls.py - GÜNCEL KOD (URL ismi 'anasayfa' olarak düzeltildi)

from django.urls import path
from . import views # views.py dosyasındaki fonksiyonları çekiyoruz

urlpatterns = [
    # Ana sayfa adresi ('')
    # İsmi 'anasayfa' olarak değiştirdik, böylece şablonlarla eşleşti.
    path('', views.index, name='anasayfa'), 
]