import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFisip(request):
    judul = "Fakultas Ekonomi dan Bisnis"
    h2 = "Terdiri dari Prodi-Prodi"
    fakultas = ["Program Studi Administrasi Publik", "Program Studi Ilmu Komunikasi", "Program Studi Ilmu Pemerintahan"]
    fotoFISIP = "fisip/img/fisip.png"

    konteksFISIP = {
        'judul' : judul,
        'terdiri' : h2,
        'fakultas' : fakultas,
        'banner' : fotoFISIP
    }
    return render(request, 'index.html', konteksFISIP)