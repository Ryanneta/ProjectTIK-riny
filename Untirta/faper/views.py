import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFaper(request):
    FP = "Fakultas Pertanian"
    h2 = "Terdiri dari Prodi-Prodi"
    fakultas = ["Program Studi Agribisnis", "Program Studi Agroekoteknologi", "Program Studi Ilmu Perikanan", "Program Studi Teknologi Pangan"]
    fotoFP = "faper/img/faper.png"

    konteksFAPER = {
        'judul' : FP,
        'terdiri' : h2,
        'fakultas' : fakultas,
        'banner' : fotoFP
    }

    return render(request, 'index.html', konteksFAPER)