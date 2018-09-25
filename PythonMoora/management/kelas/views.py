from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Kelas
from management.kelas import helpers
# Create your views here.

class ListKelasView(View):
    def get(self, request):
        template = 'kelas/index.html'
        kelas = Kelas.objects.all()
        data = {
            
            'kelas' : kelas,
        }
        return render(request, template, data)

class ListMatrixkelasView(View):
    def get(self, request):
        template = 'kelas/matrix_kelas.html'
        kelas = Kelas.objects.all()
        mtkelas = helpers.Hasil_Kelas().as_matrix()
        data = {
            'mtkelas' : mtkelas,
        }
        return render(request, template, data)

class ListPembobotankelasView(View):
    def get(self, request):
        template = 'kelas/matrix_pembobotan.html'
        kelas = Kelas.objects.all()
        mtpkelas = helpers.HasilKelas_Pembobotan().as_matrix()
        data = {
            'mtpkelas' : mtpkelas,
        }
        return render(request, template, data)