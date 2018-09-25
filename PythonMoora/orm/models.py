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

class Matematika(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='matematikas', blank=True, null=True)   
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.nilai,self.siswa.nama

    class Meta:
        db_table = 'Matematika'
        ordering = ['id']

class Fisika(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='fisikas', blank=True, null=True)   
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Fisika'
        ordering = ['id']

class Kimia(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='kimias', blank=True, null=True)   
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Kimia'
        ordering = ['id']

class Biologi(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='biologis', blank=True, null=True)   
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Biologi'
        ordering = ['id']

class HasilTes_Matematika(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='hasiltes_matematikas', blank=True, null=True)   
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'HasilTes_Matematika'
        ordering = ['id']

class HasilTes_Fisika(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='hasiltes_fisikas', blank=True, null=True)   
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'HasilTes_Fisika'
        ordering = ['id']

class HasilTes_Kimia(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='hasiltes_kimias', blank=True, null=True)   
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'HasilTes_Kimia'
        ordering = ['id']

class HasilTes_Biologi(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='hasiltes_biologis', blank=True, null=True)   
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'HasilTes_Biologi'
        ordering = ['id']

class Kelas(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='kelass', blank=True, null=True)   
    jenjang = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

  
    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Kelas'
        ordering = ['id']


class Karakter(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='karakters', blank=True, null=True)
    sikap = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama, self.sikap
    


    class Meta:
        db_table = 'Karakter'
        ordering = ['id']

class Plomba(models.Model):
    siswa = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='plombas', blank=True, null=True)
    intensitas = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return self.siswa.nama

    class Meta:
        db_table = 'Plomba'
        ordering = ['id']

