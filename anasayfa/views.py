# anasayfa/views.py
from django.shortcuts import render
from tarifler.models import Tarif # Tarif modelini kullanmak için import ettik

# Ana sayfayı (index) yönetecek fonksiyon
def index(request):
    # En son yayınlanan 5 tarifi çekiyoruz
    son_tarifler = Tarif.objects.all().order_by('-yayinlanma_tarihi')[:5]

    # Şablona (template) göndereceğimiz veriler
    context = {
        'title': 'Lezzet Defteri | Ana Sayfa',
        'tarifler': son_tarifler,
        'sayfa_basligi': 'En Son Eklenen Tarifler'
    }

    # index.html şablonunu render ediyoruz (oluşturuyoruz)
    return render(request, 'anasayfa/index.html', context)