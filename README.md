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

### Membuat 3 File CSV di Dalam Folder
Dibutuhkan agar program dapat berjalan dengan semestinya dan memiliki database.

<img width="358" height="101" alt="image" src="https://github.com/user-attachments/assets/d7c5e441-0b6f-4acb-acfb-a20c5eb7cd35" />

## Panduan Penggunaan
### 1. Loading Welcome
Menunggu beberapa detik sebelum memulai program.

<img width="470" height="165" alt="image" src="https://github.com/user-attachments/assets/bab684a7-dad7-48ed-b688-86fd72f584a7" />

### 2. Tampilan Awal
Saat program dijalankan, akan muncul loading welcome lalu program akan menampilkan halaman menu utama.

<img width="470" height="186" alt="image" src="https://github.com/user-attachments/assets/f60c4638-b5d9-4982-ad97-cfe01dc8d2f8" />

### 3. Register Akun Baru
Jika belum punya akun:
1. Pilih ``2. Register``
2. Masukkan nama pengguna (tanpa spasi atau simbol)
3. Masukkan password
4. Akun baru otomatis disimpan ke users.csv dengan role user
5. Setelah berhasil, kembali ke menu utama untuk login

<img width="465" height="137" alt="image" src="https://github.com/user-attachments/assets/2d405b66-8a76-44b8-8340-deefd63a6a9e" />

### 4. Login Akun
Dari menu utama pilih ``1. Login``, lalu masukkan username dan password yang telah terdaftar.
- Jika akun admin → masuk ke menu admin.
  
<img width="467" height="162" alt="image" src="https://github.com/user-attachments/assets/b194ab09-1c54-4644-bc43-8052a597dcd0" />

- Jika akun user → masuk ke menu user.
  
<img width="467" height="156" alt="image" src="https://github.com/user-attachments/assets/833a1494-1a55-4d28-92b8-062a030608fa" />

### 4. Menu Admin
Setelah login sebagai admin (akun bawaan bisa dilihat di file ``users.csv`` seperti: ``admin, admin123, 0, admin``):

<img width="461" height="291" alt="image" src="https://github.com/user-attachments/assets/ddfdb74e-29d6-4911-9a2a-44c63ce807af" />

#### Jika Ingin Melihat Jadwal Pilih ``1``
Fungsi : Menampilkan seluruh jadwal dari ``jadwal.csv``.

Penjelasan : Sama seperti ``user``, tetapi ``admin`` dapat mengubah data.

<img width="647" height="502" alt="image" src="https://github.com/user-attachments/assets/1fd797ab-5ff1-4c56-86b0-e8d9114c9a51" />

#### Jika Ingin Menambah Jadwal Pilih ``2``
Fungsi : Menambahkan data kereta baru ke jadwal.

Penjelasan : Wajib isi ID kereta yang berbeda agar tidak duplikat.

<img width="466" height="413" alt="image" src="https://github.com/user-attachments/assets/6736d897-5105-4c16-a9d0-df65d5f508f4" />

#### Jika Ingin Mengupdate Jadwal Pilih ``3``
Fungsi : Mengubah data jadwal kereta yang sudah ada.

Penjelasan : Dapat mengubah nama kereta, asal kereta, tujuan kereta, jam keberangkatan, dan harga tiket kereta.

<img width="648" height="818" alt="image" src="https://github.com/user-attachments/assets/262a07a6-f5fe-44a0-8fd6-143a774bb536" />

#### Jika Ingin Menghapus Jadwal Pilih ``4``
Fungsi : Menghapus jadwal kereta berdasarkan ID kereta.

Penjelasan : Data akan dihapus dari file CSV.

<img width="647" height="567" alt="image" src="https://github.com/user-attachments/assets/9041b8dd-7574-4311-9bba-351d371d1d5d" />

#### Jika Ingin Melihat Semua Transaksi User Pilih ``5``
Fungsi : Melihat semua transaksi ``user``.

Penjelasan : Data diambil dari file CSV ``transaksi.csv``.

<img width="890" height="393" alt="image" src="https://github.com/user-attachments/assets/f6db98b8-fe4d-4ce3-a6d3-3802e66ced8f" />

#### Jika Ingin Menghapus Transaksi User Pilih ``6``
Fungsi : Menghapus transaksi tertentu jika diperlukan.

Penjelasan : Misalnya, pembatalan atau kesalahan input data.

<img width="888" height="442" alt="image" src="https://github.com/user-attachments/assets/2e0a9801-9520-4223-b71b-985f9de58cfa" />

#### Jika Ingin Logout Pilih Pilih ``0``
Fungsi : Kembali ke halaman menu.

Penjelasan : Untuk keluar dari mode pengguna sebagai admin.

<img width="466" height="271" alt="image" src="https://github.com/user-attachments/assets/9e67db5f-1aa5-4e8e-99dd-6bf815993a21" />
<img width="473" height="238" alt="image" src="https://github.com/user-attachments/assets/a8c9c6a4-e0b2-49dc-b5c2-e22724301174" />

### 5. Menu User
Setelah login sebagai ``user``:

<img width="467" height="280" alt="image" src="https://github.com/user-attachments/assets/2b2b236c-9418-4ca9-916a-d02910b41545" />

#### Jika Ingin Melihat Jadwal Pilih ``1``
Fungsi : Menampilkan semua jadwal kereta dari ``jadwal.csv``.

Penjelasan : Pengguna dapat melihat semua tiket kereta yang tersedia.

<img width="650" height="457" alt="image" src="https://github.com/user-attachments/assets/93ab4717-96fd-40f1-b94a-6f3fe43d2c91" />

#### Jika Ingin Top-Up Saldo Pilih ``2``
Fungsi : Menambahkan saldo ke akun ``user``.

Penjelasan : Saldo digunakan untuk membeli tiket kereta.

<img width="465" height="265" alt="image" src="https://github.com/user-attachments/assets/3fd3f2fd-35de-4b6e-82db-edb2091a0eff" />

#### Jika Ingin Membeli Tiket Pilih ``3``
Fungsi : Memilih dan membeli tiket kereta jika saldo cukup.

Penjelasan : Transaksi akan disimpan di dalam file ``transaksi.csv``.
<img width="842" height="657" alt="image" src="https://github.com/user-attachments/assets/70a432cf-8474-4e4f-b785-b0a262fb3bb8" />

#### JIka Ingin Membeli Tiket Pilih ``4``
Fungsi : Menampilkan semua tiket kereta yang telah dibeli.

Penjelasan : Data diambil dari file ``transaksi.csv``.
<img width="737" height="355" alt="image" src="https://github.com/user-attachments/assets/f550cd72-ae7d-415f-8cfc-edfbe124b134" />

#### Jika Ingin Logout Pilih  ``0``
Fungsi : Keluar dari akun user dan kembali ke halaman menu.

Penjelasan : Untuk berpindah role pengguna sebagai ``user`` atau ``admin``.

<img width="473" height="223" alt="image" src="https://github.com/user-attachments/assets/e005207a-453c-42e9-8b44-5ce19ba5ac17" />
<img width="463" height="217" alt="image" src="https://github.com/user-attachments/assets/24ddf761-d1ef-4c04-9a61-f05557feb1e4" />

### 6. Mengakhiri Program
Untuk mengakhiri sistem pemrograman, maka pilih:

<img width="467" height="217" alt="image" src="https://github.com/user-attachments/assets/68d887d5-42c5-4371-91bc-889da0464843" />


