from django.db import models
from django.contrib.auth.models import User
import time
import os

class Siswa(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    PRIA = 'PR'
    WANITA = 'WN'
    JK_CHOICES  = (
        (PRIA, 'Pria'),
        (WANITA, 'Wanita'),
    )
    jenis_kelamin = models.CharField(
        max_length=2,
        choices=JK_CHOICES,
        default=PRIA,
    )
    alamat = models.TextField(blank=True, null=True)
    tanggal_lahir = models.DateField(auto_now=False, auto_now_add=False)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'Siswa'
        ordering = ['id']

class Akademik(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE, related_name='akademiks')   
    nama = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama
        

    class Meta:
        db_table = 'Akademik'
        ordering = ['id']

class Hasiltes(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE, related_name='hasiltess')   
    nama = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Hasiltes'
        ordering = ['id']

class Kelas(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE)   
    jenjang = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)
  
    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Kelas'
        ordering = ['id']


class Karakter(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE)
    sikap = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Karakter'
        ordering = ['id']

class Plomba(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE)
    intensitas = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Plomba'
        ordering = ['id']

