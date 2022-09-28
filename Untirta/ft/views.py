import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFT(request):
    judul = "Fakultas Teknik"
    h2 = "Terdiri dari Prodi-Prodi"
    fakultas = ["Program Studi Teknik Elektro", "Program Studi Teknik Industri", "Program Studi Teknik Kimia", "Program Studi Teknik Mesin", "Program Studi Teknik Metalurgi", "Program Studi Teknik Sipil"]
    fotoFT = "ft/img/ft.png"

    konteksFT = {
        'judul' : judul,
        'terdiri' : h2,
        'fakultas' : fakultas,
        'banner' : fotoFT
    }    
    return render(request, 'index.html', konteksFT)