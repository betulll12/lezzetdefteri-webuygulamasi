# tarifler/models.py
from django.db import models
from django.contrib.auth.models import User  # YENİ IMPORT: Kullanıcı modelini çekiyoruz

class Tarif(models.Model):
    # Temel Tarif Alanları
    baslik = models.CharField(max_length=200) # Tarifin başlığı
    aciklama = models.TextField() # Tarifin kısa açıklaması
    malzemeler = models.TextField() # Malzemeler listesi
    hazirlama_suresi = models.IntegerField(help_text="Dakika")
    pisme_suresi = models.IntegerField(help_text="Dakika")
    porsiyon_sayisi = models.IntegerField(default=1)

    # Yönetimsel Alanlar
    yayinlanma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)
    
    # YENİ EKLENEN SATIR:
    # Tarifin kim tarafından eklendiğini tutar. 
    # models.CASCADE: Kullanıcı silinirse, onun tüm tarifleri de silinir.
    # default=1: Mevcut tariflere (Admin'den eklenenlere) varsayılan olarak ID'si 1 olan kullanıcıyı atar.
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 

    class Meta:
        verbose_name = "Tarif"
        verbose_name_plural = "Tarifler"
        ordering = ['-yayinlanma_tarihi']

    def __str__(self):
        return self.baslik