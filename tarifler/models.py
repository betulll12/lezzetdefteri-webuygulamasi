# tarifler/models.py

from django.db import models
from django.contrib.auth.models import User 

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
    
    # Tarifin kim tarafından eklendiğini tutar. 
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 

    class Meta:
        verbose_name = "Tarif"
        verbose_name_plural = "Tarifler"
        ordering = ['-yayinlanma_tarihi']

    def __str__(self):
        return self.baslik
    
# YENİ EKLENEN FAVORİ MODELİ
class Favori(models.Model):
    """
    Kullanıcının hangi tarifi favorilere eklediğini tutan model.
    """
    # Hangi kullanıcı favori ekledi?
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Hangi tarife favori eklendi?
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE)
    
    # Aynı kullanıcının aynı tarifi iki kez favorilere eklemesini engeller.
    class Meta:
        unique_together = ('kullanici', 'tarif')
        verbose_name_plural = "Favoriler"
        
    def __str__(self):
        return f'{self.kullanici.username} favorilere ekledi: {self.tarif.baslik}'
    # YENİ EKLENEN MODEL: Yorum
class Yorum(models.Model):
    # Hangi kullanıcı yorum yaptı
    yazar = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Hangi tarife yorum yapıldı (Tarif silinirse yorumlar da silinsin)
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE, related_name='yorumlar')
    
    # Yorumun içeriği
    icerik = models.TextField()
    
    # Yorumun ne zaman yapıldığı
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"
        # Yorumları en yenisi en üstte olacak şekilde sırala
        ordering = ['-olusturma_tarihi'] 

    def __str__(self):
        return f'{self.yazar.username} - {self.tarif.baslik[:20]}'