# anasayfa/views.py

from django.shortcuts import render
# Gerekli import: Favori modelini kullanmak için
from tarifler.models import Tarif, Favori 
from django.db.models import Q # YENİ IMPORT: Arama (kompleks sorgular) için Q nesnesi

# Ana sayfayı (index) yönetecek fonksiyon
def index(request):
    # KULLANICIDAN ARAMA SORGUSUNU ALMA
    arama_sorgusu = request.GET.get('q') # 'q' parametresini alır. Yoksa None olur.
    
    # 1. Tüm tarifleri başlangıçta çekiyoruz (sonra limit uygulanacak)
    tarifler_query = Tarif.objects.all().order_by('-yayinlanma_tarihi')

    # ARAMA MANTIĞI
    if arama_sorgusu:
        # Q objesi ile BAŞLIK VEYA AÇIKLAMA alanlarında arama yap
        tarifler_query = tarifler_query.filter(
            Q(baslik__icontains=arama_sorgusu) | 
            Q(aciklama__icontains=arama_sorgusu)
        ).distinct() # Tekrarlı sonuçları engelle
        
        # Arama yapıldığında, sonuçların tamamını gösteririz (limit koymayız)
        tarifler = tarifler_query
        
        # Sayfa başlığını arama sonuçlarına göre güncelle
        sayfa_basligi = f"'{arama_sorgusu}' için arama sonuçları ({tarifler.count()})"
    else:
        # Arama yapılmadıysa, sadece en son 5 tarifi göster
        tarifler = tarifler_query[:5]
        sayfa_basligi = "En Son Eklenen Tarifler"

    # 2. Giriş yapan kullanıcı varsa favori ID'lerini çek
    favori_tarif_idler = []
    if request.user.is_authenticated:
        # Kullanıcının favorilere eklediği tüm tariflerin ID'lerini liste olarak çek
        favori_tarif_idler = Favori.objects.filter(kullanici=request.user).values_list('tarif__id', flat=True)

    # 3. Her tarifin favori durumunu kontrol et ve listeye ekle
    tarif_listesi = []
    for tarif in tarifler:
        tarif_data = {
            'tarif': tarif,
            # Tarif ID'si, favori ID'leri listesinde varsa True döndür
            'is_favori': tarif.id in favori_tarif_idler 
        }
        tarif_listesi.append(tarif_data)

    # Şablona (template) göndereceğimiz veriler
    context = {
        'title': 'Lezzet Defteri | Ana Sayfa',
        'tarif_listesi': tarif_listesi, 
        'sayfa_basligi': sayfa_basligi,
        # Arama sorgusunu template'e geri gönderiyoruz ki, arama kutusunda kalsın
        'arama_sorgusu': arama_sorgusu if arama_sorgusu else '',
    }

    # index.html şablonunu render ediyoruz (oluşturuyoruz)
    return render(request, 'anasayfa/index.html', context)