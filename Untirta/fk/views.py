import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFK(request):
    judul = "Fakultas Kedokteran"
    h2 = "Terdiri dari Prodi-Prodi"
    fakultas = ["Program Studi Kedokteran", "Program Studi Keperawatan S1", "Program Studi Keperawatan D3", "Program Studi S1 Gizi", "Program Studi Ilmu Keolahragaan"]
    fotoFK = "fk/img/fk.jpg"

    konteksFK = {
        'judul' : judul,
        'terdiri' : h2,
        'fakultas' : fakultas,
        'banner' : fotoFK
    }

    return render(request, 'index.html', konteksFK)