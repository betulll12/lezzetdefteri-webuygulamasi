# kullanici/views.py
from django.shortcuts import render, redirect
# Yeni importlar:
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm 

# Kayıt olma fonksiyonu (Değişmedi, sadece ekliyoruz)
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