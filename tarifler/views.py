# tarifler/views.py
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required 
from .models import Tarif
from .forms import TarifEkleForm # Bu satırın var olduğundan emin olun!

# Var olan tarif_detay fonksiyonu
def tarif_detay(request, tarif_id):
    tarif = get_object_or_404(Tarif, pk=tarif_id)
    context = {
        'tarif': tarif,
        'title': tarif.baslik,
    }
    return render(request, 'tarifler/tarif_detay.html', context)

# Hatanın Kaynağı Olan YENİ FONKSİYON (Bu fonksiyonun TAM olması gerekiyor!):
@login_required(login_url='/kullanici/giris/')
def tarif_ekle(request):
    if request.method == 'POST':
        form = TarifEkleForm(request.POST)
        if form.is_valid():
            tarif = form.save(commit=False)
            # Bu satır artık çalışmalı
            tarif.yazar = request.user 
            tarif.save()
            return redirect('tarif_detay', tarif_id=tarif.pk)
    else:
        form = TarifEkleForm()
        
    context = {
        'form': form,
        'title': 'Yeni Tarif Ekle',
    }
    return render(request, 'tarifler/tarif_ekle.html', context)