# kullanici/views.py

from django.shortcuts import render, redirect
# Django'nun hazır view'leri ve formları için importlar
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, login, logout # logout için gerekli
from django.contrib.auth.decorators import login_required # login_required için gerekli

# Favori modelini tarifler uygulamasından çekiyoruz
from tarifler.models import Favori, Tarif 


# Kayıt olma fonksiyonu
def kayit_ol(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            # Şu an 'login' URL'i olmadığı için anasayfaya yönlendiriyoruz.
            return redirect('/') 
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
        'title': 'Kullanıcı Kayıt',
    }
    return render(request, 'kullanici/kayit.html', context)


# Yeni eklenen: Giriş Sayfası (Django'nun hazır view'ini kullanıyoruz)
class KullaniciGirisView(LoginView):
    template_name = 'kullanici/giris.html'
    fields = '__all__'
    redirect_authenticated_user = True # Zaten giriş yapmışsa yönlendir
    
    # Başarılı girişten sonra gidilecek URL'i buraya yazmalısınız
    def get_success_url(self):
        return '/' # Başarılı giriş sonrası ana sayfaya yönlendir

# Eklenen: Çıkış Yap fonksiyonu (Kullanıcı tarafındaki temel işlemler için gereklidir)
def cikis_yap(request):
    logout(request)
    return redirect('anasayfa') 
    
    
# YENİ EKLENEN FAVORİ LİSTESİ FONKSİYONU
@login_required(login_url='/kullanici/giris/')
def favori_listesi(request):
    """
    Giriş yapmış kullanıcının favorilere eklediği tüm tarifleri listeler.
    """
    # 1. Kullanıcının tüm Favori objelerini çekiyoruz
    # select_related('tarif') ile veritabanı sorgusunu optimize ediyoruz.
    favoriler = Favori.objects.filter(kullanici=request.user).select_related('tarif')
    
    context = {
        'favoriler': favoriler,
        'title': 'Favori Tariflerim',
    }
    return render(request, 'kullanici/favori_listesi.html', context)