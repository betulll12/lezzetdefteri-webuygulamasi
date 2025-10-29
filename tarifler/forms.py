# tarifler/forms.py - GÜNCEL KOD (Bootstrap form stilleri eklendi)

from django import forms
from .models import Tarif

class TarifEkleForm(forms.ModelForm):
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

    # YENİ EKLENEN KOD: Tüm alanlara Bootstrap form-control sınıfını ekler
    def __init__(self, *args, **kwargs):
        super(TarifEkleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Tüm alanlara form-control sınıfını ekle
            field.widget.attrs['class'] = 'form-control'
            
            # Özellikle büyük metin kutularının (Textarea) satır sayısını ayarla
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['rows'] = 5