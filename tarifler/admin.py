# tarifler/admin.py
from django.contrib import admin
from .models import Tarif # Tarif modelimizi import ediyoruz

# Modeli admin paneline kaydediyoruz
admin.site.register(Tarif)