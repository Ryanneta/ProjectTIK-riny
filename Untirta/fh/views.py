import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFH(request):
    judul = "Fakultas Hukum"
    h2 = "Terdiri dari Prodi-Prodi"
    fakultas = ["Program Sarjana Ilmu Hukum"]
    fotoFH = "fh/img/FH.jpg"

    konteksFH = {
        'judul' : judul,
        'terdiri' : h2,
        'fakultas' : fakultas,
        'banner' : fotoFH
    }

    return render(request, 'index.html', konteksFH)