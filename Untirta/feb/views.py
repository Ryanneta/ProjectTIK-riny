import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFEB(request):
    judul = "Fakultas Ekonomi dan Bisnis"
    h2 = "Terdiri dari Prodi-Prodi"
    fakultas = ["Program Sarjana Managemen", "Program Sarjana Akuntansi", "Program Sarjana Ilmu Ekonomi Pembangunan", "Program Sarjana Ekonomi Syariah",     "Program Diploma III Akuntansi", "Program Diploma III Marketing", "Program Diploma III Perpajakan", "Program Diploma III Keuangan Perbankan"]
    fotoFEB = "feb/img/feb.jpg"

    konteksFEB = {
        'judul' : judul,
        'terdiri' : h2,
        'fakultas' : fakultas,
        'banner' : fotoFEB
    }

    return render(request, 'index.html', konteksFEB)