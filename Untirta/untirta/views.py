from django.shortcuts import render
from django.template import loader

def index(request):
    judul = "UNIVERSITAS SULTAN AGENG TIRTAYASA"
    p1 = "Universitas Sultan Ageng Tirtayasa disingkat Untirta, adalah perguruan tinggi negeri yang terdapat di Provinsi Banten, Indonesia. Dengan kampus utama Untirta di Kabupaten Serang, kampus Fakultas Teknik di Kota Cilegon, dan Fakultas Keguruan dan Ilmu Pendidikan di Ciwaru, Kota Serang. Alamat: Jl. Raya Palka No.Km 3, Panancangan, Kec. Cipocok Jaya, Kabupaten Serang, Banten 42124, Indonesia"
    p2 = "Nama Kampus Untirta ini berasal dari nama Sultan Ageng Tirtayasa, yaitu pemimpin  di Banten periode 1651-1683.  Sultan Ageng Tirtayasa juga diberi anugerah oleh Pemerintah sebagai Pahlawan Nasional sesuai SK Presiden RI No. 045/TK/Th 1970, pada 1 Agustus 1970. Lahirnya Untirta (Universitas Sultan Ageng Tirtayasa) berawal dari dibangunnya Yayasan Pendidikan Tirtayasa pada 1 Oktober 1980. Mulanya, Yayasan Pendidikan Tirtayasa membangung Sekolah Tinggi Ilmu Hukum (STIH) tahun 1981, lalu pada tahun 1982 didirikan Sekolah Tinggi Keguruan dan Ilmu Pendidikan (STKIP)."
    p3 = "Bersamaan dengan didirikannya STKIP, didirikan pula Sekolah Tinggi Teknik (STT) oleh Yayasan Krakatau Steel Cilegon. STT ini kemudian bergabung bersama Yayasan Pendidikan Tirtayasa, hingga akhirnya beridiri Universitas Tirtayasa Serang, Banten. Jadi, Untirta ini merupakan gabungan antara STIH, STT dan STKIP. Setelah bergabung, masing-masing status sekolah tingging berubah menjadi fakultas. Hal ini tertuang dalam SK Mendikbud RI pada 28 November 1984. Adapun Fakultas-Fakultas tersebut yaitu Fakultas Teknik, Fakultas Hukum serta Fakultas Ilmu Keguruan dan Ilmu Pendidikan (FKIP). Lalu, pada tahun 1989, Untirta menambah Fakultas Ekonomi dan Fakultas Pertanian. Dan pada tahun-tahun berikutnya, ada penambahan beberapa fakultas."
    fotoFT = "img/sindang.jpg"
    footer = "2022 UNTIRTA by Riny Anggraeni"

    konteksUntirta = {
        'judul' : judul,
        'p1' : p1,
        'p2' : p2,
        'p3' : p3,
        'banner' : fotoFT,
        'footer' : footer
    }    
    return render(request, 'index.html', konteksUntirta)