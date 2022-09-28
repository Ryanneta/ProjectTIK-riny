from django.shortcuts import render

# Create your views here.
def riny(request):
    judul = "Informasi Pembuat"
    fotoRiny = "img/banner_about.png"
    me = "riny/img/riny.jpg"
    nama = "nama : Riny Anggrraeni"
    kelas = "kelas : 3A"
    nim = "NIM : 2225210007"
    jurusan = "Jurusan : Pendidikan Matematika"
    dosen = "Dosen Pengampu : Dr. Aan Hendrayana, S.Si., M.Pd."
    mk = "Mata Kuliah : Teknologi Informasi dan Komunikasi Untuk Pembelajaran"


    konteksRiny = {
        'judul' : judul,
        'banner' : fotoRiny,
        'me' : me,
        'nama' : nama,
        'kelas' : kelas,
        'nim' : nim,
        'jurusan' : jurusan,
        'dosen' : dosen,
        'mk' : mk
    }    
    return render(request, 'index.html', konteksRiny)