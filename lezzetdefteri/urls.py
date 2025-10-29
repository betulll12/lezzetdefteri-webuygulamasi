# lezzetdefteri/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Yönetim Paneli
    path('admin/', admin.site.urls),
    
    # anasayfa uygulamasının URL'lerini dahil et
    path('', include('anasayfa.urls')),
    
    # tarifler uygulamasının URL'lerini dahil et (Aktif edildi)
    path('tarifler/', include('tarifler.urls')),
    
    # Diğer uygulamalar şimdilik kapalı kalabilir:
    path('kullanici/', include('kullanici.urls')),
]