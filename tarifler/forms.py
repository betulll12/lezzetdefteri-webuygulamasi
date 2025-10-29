# tarifler/forms.py - GÜNCEL KOD

from django import forms
# Yorum modelini import etmeyi unutmayın
from .models import Tarif, Yorum 

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


# YENİ EKLENEN SINIF: Yorum Formu
class YorumForm(forms.ModelForm):
    # Formdaki 'icerik' alanının yer tutucusunu (placeholder) değiştirelim
    icerik = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Yorumunuzu buraya yazın...', 'rows': 4}),
        label='Yorumunuz'
    )
    
    class Meta:
        model = Yorum
        # Sadece yorum içeriğini kullanıcıdan almamız yeterli
        fields = ('icerik',)
        
    # Yorum formuna da Bootstrap form-control sınıfını ekleyelim
    def __init__(self, *args, **kwargs):
        super(YorumForm, self).__init__(*args, **kwargs)
        self.fields['icerik'].widget.attrs['class'] = 'form-control'