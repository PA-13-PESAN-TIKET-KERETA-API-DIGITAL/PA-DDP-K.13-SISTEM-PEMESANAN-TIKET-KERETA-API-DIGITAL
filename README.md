# PA-DDP-K.13-SISTEM-PEMESANAN-TIKET-KERETA-API-DIGITAL

## Deskripsi
Program ini merupakan simulasi sistem pemesanan tiket kereta api digital berbasis terminal/CLI yang menggunakan bahasa pemrograman Python. Sistem ini menyediakan fitur **login atau register akun, pembelian tiket kereta, top-up saldo, serta manajemen jadwal kereta dan transaksi**, yang mana nantinya data tersebut akan tersimpan ke dalam file CSV.

## Nama Kelompok & Anggota
Kelompok : 13

Anggota :
1. Sabrina Azhmalia Nisa **(2509116051)**
2. Awang Rifky Muhadzib **(2509116059)**
3. Nabila Salma Putri **(2509116065)**

## Flowchart
### Flowchart Menu Login
![Flowchart PA 100-Menu Login](https://github.com/user-attachments/assets/35e43369-02e5-44bb-ab94-11bf1320ab27)

### Flowchart Menu Sebagai Admin
![Flowchart PA 100-Login User](https://github.com/user-attachments/assets/d14d9d9f-d81d-4c29-a539-5db132753476)


### Flowchart Menu Sebagai User
![Flowchart PA 100-Login Admin](https://github.com/user-attachments/assets/c8c88db0-9b25-42bc-898f-308d8bdedc2a)

## Instalasi & Persiapan
### Install Library
Sebelum menjalankan program, install beberapa library berikut:

<img width="1475" height="416" alt="image" src="https://github.com/user-attachments/assets/6f1d28ef-0646-4d8e-b900-367a7e0977b7" />

### Jalankan Program
Tekan run di Visual Studio Code untuk memulai program.

<img width="652" height="368" alt="image" src="https://github.com/user-attachments/assets/d116e2da-297b-427f-bb2b-fce3bb69fb9c" />

### Menambahkan 3 File CSV di Dalam Folder
Dibutuhkan agar program berjalan dengan semestinya dan memiliki database.

<img width="358" height="101" alt="image" src="https://github.com/user-attachments/assets/d7c5e441-0b6f-4acb-acfb-a20c5eb7cd35" />

## Panduan Penggunaan
### 1. Loading Welcome
Menunggu beberapa detik sebelum memulai program.

<img width="470" height="165" alt="image" src="https://github.com/user-attachments/assets/bab684a7-dad7-48ed-b688-86fd72f584a7" />

### 2. Tampilan Awal
Saat program dijalankan, akan muncul loading welcome lalu menu utama.

<img width="470" height="186" alt="image" src="https://github.com/user-attachments/assets/f60c4638-b5d9-4982-ad97-cfe01dc8d2f8" />

### 3. Register Akun Baru
Jika belum punya akun:
1. Pilih ``2. Register``
2. Masukkan nama pengguna (tanpa spasi/simbol)
3. Masukkan password
4. Akun baru otomatis disimpan ke users.csv dengan role user
5. Setelah berhasil, kembali ke menu utama untuk login

<img width="465" height="137" alt="image" src="https://github.com/user-attachments/assets/2d405b66-8a76-44b8-8340-deefd63a6a9e" />

### 4. Login Akun
Dari menu utama pilih ``1. Login``, lalu masukkan username dan password yang sudah terdaftar.
- Jika akun admin → masuk ke menu admin.
  
<img width="472" height="150" alt="image" src="https://github.com/user-attachments/assets/1b9ae97a-c309-4180-9d79-63d085a3941d" />

- Jika akun user → masuk ke menu user.
  
<img width="467" height="156" alt="image" src="https://github.com/user-attachments/assets/833a1494-1a55-4d28-92b8-062a030608fa" />

### 4. Menu Admin
Setelah login sebagai admin (akun bawaan bisa dibuat di ``users.csv`` seperti: ``admin, admin123, 0, admin``):

<img width="471" height="291" alt="image" src="https://github.com/user-attachments/assets/cf549bc4-f6e3-4514-8bfe-d7fd496fe80c" />

#### Jika Ingin Melihat Jadwal Pilih ``1``
Fungsi : Menampilkan seluruh jadwal dari ``jadwal.csv``

Penjelasan : Sama seperti user, tetapi admin dapat mengubah data.
<img width="651" height="477" alt="image" src="https://github.com/user-attachments/assets/5b3f3138-6588-4b87-8d60-16d30130ae44" />

#### Jika Ingin Menambah Jadwal Pilih ``2``
Fungsi : Menambahkan data kereta baru ke jadwal.

Penjelasan : Wajib isi ID kereta yang berbeda agar tidak duplikat.

<img width="471" height="413" alt="image" src="https://github.com/user-attachments/assets/6cceb3df-6080-43ea-a3a2-496fe9867a6a" />

#### Jika Ingin Mengupdate Jadwal Pilih ``3``
Fungsi : Mengubah data jadwal kereta yang sudah ada.

Penjelasan : Dapat mengubah nama kereta, asal kereta, tujuan kereta, jam keberangkatan, dan harga tiket kereta.

<img width="642" height="552" alt="image" src="https://github.com/user-attachments/assets/9589f972-a349-4429-a3c9-d92257c829a7" />

#### Jika Ingin Menghapus Jadwal Pilih ``4``
Fungsi : Menghapus jadwal kereta berdasarkan ID kereta.

Penjelasan : Data akan dihapus dari file CSV.


#### Jika Ingin Melihat Semua Transaksi User Pilih ``5``
Fungsi : Melihat semua transaksi user.

Penjelasan : Data diambil dari file CSV transaksi.csv.

#### Jika Ingin Menghapus Transaksi User Pilih ``6``
Fungsi : Menghapus transaksi tertentu jika diperlukan.

Penjelasan : Misalnya, pembatalan atau kesalahan input data.

#### Jika Ingin Logout Pilih Pilih ``7``
Fungsi : Kembali ke menu awal.

Penjelasan : Untuk keluar dari mode admin.
