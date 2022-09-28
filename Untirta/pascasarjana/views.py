import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiPC(request):
    judul = "Pascasarjana"
    h2 = "Terdiri dari Prodi-Prodi"
    fakultas = ["Doktor Pendidikan", "Doktor Ilmu Akuntansi", "Magister Ilmu Hukum", "Magister Ilmu Pertanian", "Magister Administrasi Publik", "Magister Akuntansi", "Magister Ilmu Komunikasi", "Magister Manajemen", "Magister Teknik Kimia", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Matematika", "Teknologi Pendidikan"]
    fotoPC = "ps/img/ps.jpg"

    konteksPC = {
        'judul' : judul,
        'terdiri' : h2,
        'fakultas' : fakultas,
        'banner' : fotoPC
    }
    return render(request, 'index.html', konteksPC)