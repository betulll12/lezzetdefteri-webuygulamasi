# anasayfa/urls.py
from django.urls import path
from . import views # views.py dosyasındaki fonksiyonları çekiyoruz

urlpatterns = [
    # Ana sayfa adresi ('')
    path('', views.index, name='anasayfa_index'),
]