# tarifler/views.py - GÜNCEL VE TAM KOD

from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required 
from .models import Tarif
from .forms import TarifEkleForm 

# Var olan tarif_detay fonksiyonu (URL'deki <int:pk> ile uyumlu hale getirildi)
def tarif_detay(request, pk):
    tarif = get_object_or_404(Tarif, pk=pk)
    context = {
        'tarif': tarif,
        'title': tarif.baslik,
    }
    return render(request, 'tarifler/tarif_detay.html', context)

# Tarif Ekleme fonksiyonu (URL'deki <int:pk> ile uyumlu hale getirildi)
@login_required(login_url='/kullanici/giris/')
def tarif_ekle(request):
    if request.method == 'POST':
        form = TarifEkleForm(request.POST)
        if form.is_valid():
            tarif = form.save(commit=False)
            tarif.yazar = request.user 
            tarif.save()
            # Yönlendirme, URL'deki 'pk' parametresini kullanacak şekilde güncellendi
            return redirect('tarif_detay', pk=tarif.pk) 
    else:
        form = TarifEkleForm()
        
    context = {
        'form': form,
        'title': 'Yeni Tarif Ekle',
    }
    return render(request, 'tarifler/tarif_ekle.html', context)


# YENİ EKLENEN FONKSİYON: Tarifi Düzenleme
@login_required
def tarif_duzenle(request, pk):
    # pk (primary key) ile tarife ulaş
    tarif = get_object_or_404(Tarif, pk=pk)
    
    # GÜVENLİK KONTROLÜ: Sadece tarifi oluşturan kullanıcı düzenleyebilir
    if tarif.yazar != request.user:
        return redirect('tarif_detay', pk=pk) 

    if request.method == 'POST':
        form = TarifEkleForm(request.POST, instance=tarif)
        if form.is_valid():
            form.save()
            return redirect('tarif_detay', pk=tarif.pk)
    else:
        # Sayfa ilk açıldığında, formun içini mevcut verilerle doldur
        form = TarifEkleForm(instance=tarif)
    
    # Düzenleme için de tarif_ekle.html şablonunu kullanıyoruz
    return render(request, 'tarifler/tarif_ekle.html', {'form': form, 'title': 'Tarifi Düzenle'})


# YENİ EKLENEN FONKSİYON: Tarifi Silme
@login_required
def tarif_sil(request, pk):
    # pk ile tarife ulaş
    tarif = get_object_or_404(Tarif, pk=pk)
    
    # GÜVENLİK KONTROLÜ: Sadece tarifi oluşturan kullanıcı silebilir
    if tarif.yazar != request.user:
        return redirect('tarif_detay', pk=pk) 
        
    # Kullanıcıdan silme onayı geldiyse
    if request.method == 'POST':
        tarif.delete() # Tarifi sil
        return redirect('/') # Ana sayfaya yönlendir
    
    # POST gelmediyse, silme onay sayfasını göster
    return render(request, 'tarifler/tarif_sil.html', {'tarif': tarif, 'title': 'Tarifi Sil'})