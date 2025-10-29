# tarifler/forms.py
from django import forms
from .models import Tarif

class TarifEkleForm(forms.ModelForm):
    # Bu form, Tarif modeline dayanarak otomatik olarak alanları oluşturacak
    class Meta:
        model = Tarif
        # Yazar, tarih gibi alanlar otomatik doldurulacağı için listeye almıyoruz.
        fields = ['baslik', 'aciklama', 'malzemeler', 'hazirlama_suresi', 'pisme_suresi', 'porsiyon_sayisi']
        
        # Kullanıcı arayüzünde görünen isimleri (verbose_name) tanımlama
        labels = {
            'baslik': 'Tarif Başlığı',
            'aciklama': 'Tarifin Hazırlanışı',
            'malzemeler': 'Malzemeler (Her satıra bir malzeme yazın)',
            'hazirlama_suresi': 'Hazırlama Süresi (dk)',
            'pisme_suresi': 'Pişme Süresi (dk)',
            'porsiyon_sayisi': 'Kaç Kişilik?',
        }