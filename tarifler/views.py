# tarifler/views.py - GÜNCEL VE TAM KOD

from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from .models import Tarif, Favori, Yorum 
from .forms import TarifEkleForm, YorumForm 

# GÜNCELLENEN FONKSİYON: Tarif Detay Sayfası
def tarif_detay(request, pk):
    tarif = get_object_or_404(Tarif, pk=pk)
    is_favori = False
    
    # 1. Favori kontrolü
    if request.user.is_authenticated:
        if Favori.objects.filter(kullanici=request.user, tarif=tarif).exists():
            is_favori = True

    # 2. Yorum Formu ve İşlemi (Aynı URL'e POST yapıyoruz)
    if request.method == 'POST':
        # Sadece giriş yapmış kullanıcılar yorum yapabilir
        if not request.user.is_authenticated:
            messages.error(request, "Yorum yapabilmek için lütfen giriş yapın.")
            return redirect('giris')
            
        # Yorum formundan gelen POST verisini kontrol et
        # Eğer bu POST isteği favori butonu değilse, yorum formu olarak işle
        if 'icerik' in request.POST:
            form = YorumForm(request.POST)
            if form.is_valid():
                yeni_yorum = form.save(commit=False)
                yeni_yorum.tarif = tarif
                yeni_yorum.yazar = request.user
                yeni_yorum.save()
                
                messages.success(request, "Yorumunuz başarıyla eklendi.")
                
                # Sayfayı yenilemeden hemen sonra yorumu göstermek için redirect
                return redirect('tarif_detay', pk=tarif.pk)
        
        # NOT: Eğer POST isteği favori butonu ise (csrf_token ve hidden input olmadan),
        # form kontrolü atlanıp aşağıdaki GET/Context bloğuna geçecektir.

    else:
        # GET isteği ise boş formu göster
        form = YorumForm()

    # 3. Yorumları Listeleme
    yorumlar = tarif.yorumlar.all() # Modeldeki related_name='yorumlar' ile çekiliyor

    context = {
        'tarif': tarif,
        'is_favori': is_favori,
        'yorumlar': yorumlar,
        'yorum_formu': form,
        'title': tarif.baslik,
    }
    return render(request, 'tarifler/tarif_detay.html', context)


# EKSİK OLAN FONKSİYON 1: Tarif Ekleme
@login_required(login_url='/kullanici/giris/')
def tarif_ekle(request):
    if request.method == 'POST':
        form = TarifEkleForm(request.POST)
        if form.is_valid():
            tarif = form.save(commit=False)
            tarif.yazar = request.user 
            tarif.save()
            messages.success(request, "Tarif başarıyla eklendi!")
            return redirect('tarif_detay', pk=tarif.pk) 
    else:
        form = TarifEkleForm()
        
    context = {
        'form': form,
        'title': 'Yeni Tarif Ekle',
    }
    return render(request, 'tarifler/tarif_ekle.html', context)


# EKSİK OLAN FONKSİYON 2: Tarifi Düzenleme
@login_required
def tarif_duzenle(request, pk):
    tarif = get_object_or_404(Tarif, pk=pk)
    
    # GÜVENLİK KONTROLÜ
    if tarif.yazar != request.user:
        messages.error(request, "Bu tarifi düzenleme yetkiniz yok.")
        return redirect('tarif_detay', pk=pk) 

    if request.method == 'POST':
        form = TarifEkleForm(request.POST, instance=tarif)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarif başarıyla güncellendi.")
            return redirect('tarif_detay', pk=tarif.pk)
    else:
        form = TarifEkleForm(instance=tarif)
    
    return render(request, 'tarifler/tarif_ekle.html', {'form': form, 'title': 'Tarifi Düzenle'})


# EKSİK OLAN FONKSİYON 3: Tarifi Silme
@login_required
def tarif_sil(request, pk):
    tarif = get_object_or_404(Tarif, pk=pk)
    
    # GÜVENLİK KONTROLÜ
    if tarif.yazar != request.user:
        messages.error(request, "Bu tarifi silme yetkiniz yok.")
        return redirect('tarif_detay', pk=pk) 
        
    if request.method == 'POST':
        tarif.delete() 
        messages.success(request, "Tarif başarıyla silindi.")
        return redirect('anasayfa') # Ana sayfaya yönlendir
    
    return render(request, 'tarifler/tarif_sil.html', {'tarif': tarif, 'title': 'Tarifi Sil'})


# EKSİK OLAN FONKSİYON 4: FAVORİ FONKSİYONU
@login_required 
def favori_ekle_kaldir(request, tarif_id):
    """
    Bir tarife favori ekler veya var olan favoriyi kaldırır.
    """
    if request.method == 'POST':
        tarif = get_object_or_404(Tarif, id=tarif_id)
        
        favori_var_mi = Favori.objects.filter(kullanici=request.user, tarif=tarif).exists()
        
        if favori_var_mi:
            Favori.objects.filter(kullanici=request.user, tarif=tarif).delete()
            messages.info(request, "Favorilerden kaldırıldı.")
        else:
            Favori.objects.create(kullanici=request.user, tarif=tarif)
            messages.success(request, "Favorilere eklendi!")
            
        # Kullanıcının geldiği sayfaya yönlendir
        return redirect(request.META.get('HTTP_REFERER', 'anasayfa'))
        
    # POST isteği değilse
    return redirect('anasayfa')