# Kelompok 10 Kelas C
# Anggota Kelompok :
I0324094, Nazla Faradisa, nazlafrds
I0324101, Salma Salsabilla, salma1311
I0324111, Amira Malika Andalas, Amirandalas
I0324125, Zevira Maharani Sari Dewi, zeviramh

# Sistem Pembayaran Parkir di Pusat Perbelanjaan
# Deskripsi Singkat
Aplikasi Sistem Pembayaran Parkir adalah alat digital yang membantu Anda mengawasi parkir di pusat perbelanjaan. Aplikasi ini secara otomatis mencatat waktu masuk dan keluar kendaraan, menghitung tarif parkir berdasarkan durasi. Sistem ini dimaksudkan untuk meningkatkan kualitas pencatatan, mengurangi antrean, dan membuat parkir lebih nyaman bagi pengunjung.

# Fitur yang Tersedia
- Fitur login, menyimpan data login pada file VSC
- Menyimpan data jenis kendaraan, plat kendaraan, waktu masuk, waktu keluar, lama kendaraan parkir, tarif parkir pada file database.csv

# Gambar Flowchart




#  Penjelasan Flowchart
- Mulai, program dimulai dari menu ini
- Setelah itu akan masuk ke menu login yang terdapat 2 pilihan
- Setelah sudah menginput pilihan 
- Jika pengguna memilih Kendaraan Masuk, program akan mengarahkan ke Sub-program Kendaraan Masuk. Proses ini mencakup pencatatan kendaraan yang masuk ke area tertentu. Misalnya, mencatat nomor kendaraan, waktu masuk, dan detail lainnya terkait kendaraan.
- Jika pengguna memilih Kendaraan Keluar, program akan mengarahkan ke Sub-program Kendaraan Keluar. Proses ini mencakup pencatatan kendaraan yang meninggalkan area tertentu. Biasanya mencakup verifikasi kendaraan yang keluar (mencocokkan data masuk), pencatatan waktu keluar, dan menghitung biaya parkir (jika relevan).
- Jika pilihan tidak valid, program kemungkinan akan meminta ulang input.
- Setelah sub-program selesai dijalankan (baik kendaraan masuk maupun keluar), program akan kembali ke titik akhir dan menampilkan status Selesai.

- Mulai, awal sub-program untuk proses login.
- Setelah itu sistem membaca data login yang tersimpan di database atau file konfigurasi. Data ini mencakup informasi username dan password yang valid untuk proses otentikasi.
- Input username dan password,Pengguna diminta untuk memasukkan:
Username: Nama pengguna yang digunakan untuk identifikasi.
Password: Kata sandi untuk autentikasi.
- Validasi data, sistem memeriksa apakah username dan password yang dimasukkan sesuai dengan data login yang disimpan.
- Ya: Jika data cocok, pengguna diberikan akses, dan proses login dinyatakan berhasil. Pengguna diberikan akses ke sistem. Sistem melanjutkan proses atau mengakhiri sub-program login.
- Tidak: Jika data tidak cocok, sistem mengarahkan ke proses login gagal. Sistem menginformasikan bahwa login tidak berhasil. Pengguna diminta untuk mencoba lagi dengan memasukkan data yang benar (loop kembali ke langkah input).
- Selesai, proses login berakhir setelah status keberhasilan atau kegagalan ditentukan.

- Mulai, menandai dimulainya proses pencatatan kendaraan masuk.
- Input data kendaraan, Sistem akan meminta pengguna untuk memasukkan:
Jenis Kendaraan: Misalnya, mobil, motor, atau jenis lainnya.
Plat Kendaraan: Nomor plat kendaraan untuk identifikasi.
- Setelah data kendaraan dimasukkan, pengguna diminta untuk mengonfirmasi apakah ingin melanjutkan proses.
- Ya: Jika ingin melanjutkan, proses akan diteruskan ke langkah berikutnya.
- Tidak: Jika pengguna tidak ingin melanjutkan, sistem akan mengarahkan kembali ke menu utama (program utama).
- Jika pengguna memilih untuk melanjutkan, sistem akan menyimpan data berikut ke dalam database jenis kendaraan, plat kendaraan, waktu masuk
- Cetak karcis, setelah data berhasil disimpan, sistem mencetak karcis sebagai bukti masuk untuk pengguna. Karcis ini biasanya berisi nomor tiket, informasi waktu masuk, detail kendaraan.
- Setelah karcis dicetak, kendaraan dianggap telah terdaftar masuk ke area.

- Mulai, proses dimulai.
- Input data, pengguna diminta memasukkan jenis kendaraan, plat nomor kendaraan, dan waktu masuk kendaraan.
- Jika pengguna memutuskan untuk tidak melanjutkan, program kembali ke menu utama dan menampilkan pilihan menu lainnya.
- Jika pengguna memilih untuk melanjutkan, data yang dimasukkan (jenis kendaraan, plat nomor, dan waktu masuk) disimpan.
- Input Waktu Keluar, setelah data awal disimpan, pengguna diminta untuk memasukkan waktu keluar kendaraan.
- Penyimpanan Data, data yang meliputi jenis kendaraan, plat nomor, waktu masuk, dan waktu keluar disimpan ke dalam database.
Penghitungan dan Tampilan Hasil:

Sistem menghitung durasi parkir (lama parkir) dan biaya parkir berdasarkan data yang dimasukkan. Sistem menampilkan informasi lengkap, termasuk:
Jenis kendaraan
Plat nomor kendaraan
Waktu masuk
Waktu keluar
Lama parkir
Biaya parkir
- Selesai: Proses berakhir.