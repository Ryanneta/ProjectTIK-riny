import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def prodiFKIP(request):
    judul = "Fakultas Keguruan dan Ilmu Pendidikan"
    h2 = "Terdiri dari Prodi-Prodi"
    fakultas = ["Program Studi Pendidikan Nonformal", "Program Studi Pendidikan Bahasa Indonesia", "Program Studi Pendidikan Bahasa Inggris", "Program Studi Pendidikan Biologi", "Program Studi Pendidikan Matematika", "Program Studi Pendidikan Guru Sekolah Dasar", "Program Studi Pendidikan Guru PAUD", "Program Studi Bimbingan dan Konseling", "Program Studi Pendidikan Fisika", "Program Studi Pendidikan Ilmu Pengetahuan Alam", "Program Studi Pendidikan Kimia", "Program Studi Pendidikan Khusus", "Program Studi Pendidikan Pancasila dan Kewarganegaraan", "Program Studi Pendidikan Sejarah", "Program Studi Pendidikan Seni dan Pertunjukan", "Program Studi Pendidikan Sosiologi", "Program Studi Pendidikan Vokasional Teknik Elektro", "Program Studi Pendidikan Vokasional Teknik Mesin"]
    fotoFKIP = "fkip/img/fkip.jpg"

    konteksFKIP = {
        'judul' : judul,
        'terdiri' : h2,
        'fakultas' : fakultas,
        'banner' : fotoFKIP
    }


    return render(request, 'index.html', konteksFKIP)