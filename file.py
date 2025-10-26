import csv
import os
import pwinput
from datetime import datetime
from prettytable import PrettyTable
import time
from colorama import init, Fore

init(autoreset=True)

USER_FILE = "users.csv"
JADWAL_FILE = "jadwal.csv"
TRANSAKSI_FILE = "transaksi.csv"

def loading_welcome():
    clear()
    print(Fore.RED +"===================================================")
    print(Fore.RED +"|",Fore.LIGHTYELLOW_EX +"                  SELAMAT DATANG               ",Fore.RED +"|")
    print(Fore.RED +"|",Fore.LIGHTYELLOW_EX +"  DI SISTEM PEMESANAN TIKET KERETA API DIGITAL ",Fore.RED +"|")
    print(Fore.RED +"===================================================")
    print("\nLoading", end="")
    time.sleep(0.5)
    print(".", end="", flush=True)
    time.sleep(0.5)
    print(".", end="", flush=True)
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)

    clear()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def load_csv(filename):
    data = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data

def save_csv(filename, data, fieldnames):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# --> untuk login akun

def login():
    users = load_csv(USER_FILE)
    clear()
    print(Fore.RED +"===================================================")
    print(Fore.RED +"|",Fore.LIGHTYELLOW_EX +"                      LOGIN                    ",Fore.RED +"|")
    print(Fore.RED +"===================================================")
    while True :
        try:
            username = input("Masukkan username: ")
            password = pwinput.pwinput("Masukkan password: ")
        except KeyboardInterrupt:
            print(Fore.RED + "\nERROR, Jangan Tekan CRTL+C")
            continue
        except EOFError:
            print(Fore.RED +"\nERROR, Jangan Tekan CRTL+Z")
            continue

        if not username.isalnum():
            print(Fore.RED + "\nNama hanya boleh huruf dan angka, tanpa simbol atau spasi!")
            continue

        break

    print("\nMemverifikasi akun...", end="")
    time.sleep(1)
    print(".", end="", flush=True)
    time.sleep(1)
    print(".", end="", flush=True)
    time.sleep(1)
    print(".")
    time.sleep(0.5)

    for user in users:
        if user["Nama"] == username and user["Password"] == password:
            clear()
            print(f"\nLogin berhasil! Selamat datang, {username}.")
            if user["Role"] == "admin":
                menu_admin()
            else:
                menu_user(user)
            return
    print(Fore.RED +"\nUsername atau password salah!")

# --> untuk daftar akun

def register():
    users = load_csv(USER_FILE)
    clear()
    print(Fore.RED +"===================================================")
    print(Fore.RED +"|",Fore.LIGHTYELLOW_EX +"                    REGISTER                   ",Fore.RED +"|")
    print(Fore.RED +"===================================================")
    while True:
        try:
            username = input("Masukkan nama user baru: ")
        except KeyboardInterrupt:
            print(Fore.RED + "\n\nERROR, Jangan Tekan CRTL+C")
            continue
        except EOFError:
            print(Fore.RED +"\nERROR, Jangan Tekan CRTL+Z")
            continue
    
        if len(username) > 10:
            print(Fore.RED + "Nama terlalu panjang! Maksimal 10 karakter.")
            continue

        if not username.isalnum():
            print(Fore.RED + "Nama hanya boleh huruf dan angka, tanpa simbol atau spasi!")
            continue

        if any(u["Nama"] == username for u in users):
            print(Fore.RED +"Nama sudah terdaftar! Silakan login.")
            return
    
        break

    password = pwinput.pwinput("Masukkan password: ")
    saldo_awal = "0"
    role = "user"

    users.append({"Nama": username, "Password": password, "Saldo": saldo_awal, "Role": role})
    save_csv(USER_FILE, users, ["Nama", "Password", "Saldo", "Role"])
    print(f"User '{username}' berhasil dibuat! Silakan login.")

# --> untuk lihat jadwal

def lihat_jadwal():
    jadwal = load_csv(JADWAL_FILE)
    if not jadwal:
        print("Belum ada jadwal.")
        return
    table = PrettyTable(["ID", "Nama Kereta", "Asal", "Tujuan", "Jam", "Harga"])
    for j in jadwal:
        table.add_row([j["ID_Kereta"], j["Nama_Kereta"], j["Asal"], j["Tujuan"], j["Jam_Berangkat"], j["Harga"]])
    print(table)

# --> untuk tambah jadwal

def tambah_jadwal():
    try:
        jadwal = load_csv(JADWAL_FILE)
        new_id = input("Masukkan ID Kereta: ").strip()
        for j in jadwal:
            if j["ID_Kereta"].lower() == new_id.lower():
                print(Fore.RED + f"ID '{new_id}' sudah digunakan! Gunakan ID lain.")
                time.sleep(2)
                return

        nama = input("Nama Kereta: ").strip()
        asal = input("Asal: ").strip()
        tujuan = input("Tujuan: ").strip()

        while True:
            jam_input = input("Masukkan jam berangkat (hh:mm): ").strip()
            try:
                jam_h, jam_m = jam_input.split(":")
                jam_h, jam_m = int(jam_h), int(jam_m)
                if 0 <= jam_h <= 23 and 0 <= jam_m <= 59:
                    jam = f"{jam_h:02d}:{jam_m:02d}"
                    break
                else:
                    print(Fore.RED + "Jam tidak valid! Harus antara 00:00 sampai 23:59.")
            except ValueError:
                print(Fore.RED + "Format jam salah! Gunakan format hh:mm, contoh 07:30.")

        while True:
            harga = input("Harga: ").strip()
            if harga.isdigit():
                harga = int(harga)
                break
            else:
                print(Fore.RED + "Input tidak valid! Masukkan angka untuk harga.")

    except KeyboardInterrupt:
        print(Fore.RED + "\nERROR: Jangan Tekan CTRL+C")
        return
    except EOFError:
        print(Fore.RED + "\nERROR: Jangan Tekan CTRL+Z")
        return

    jadwal.append({
        "ID_Kereta": new_id,
        "Nama_Kereta": nama,
        "Asal": asal,
        "Tujuan": tujuan,
        "Jam_Berangkat": jam,
        "Harga": harga
    })
    save_csv(JADWAL_FILE, jadwal, ["ID_Kereta", "Nama_Kereta", "Asal", "Tujuan", "Jam_Berangkat", "Harga"])
    print(Fore.GREEN + "Jadwal berhasil ditambahkan!")


def hapus_jadwal():
    jadwal = load_csv(JADWAL_FILE)
    lihat_jadwal()

    target = input("Masukkan ID kereta yang ingin dihapus: ").strip().lower()

    ada = False
    for j in jadwal:
        if j["ID_Kereta"].lower() == target:
            ada = True
            jadwal.remove(j)
            break

    if ada:
        save_csv(JADWAL_FILE, jadwal, ["ID_Kereta", "Nama_Kereta", "Asal", "Tujuan", "Jam_Berangkat", "Harga"])
        print("Jadwal berhasil dihapus!")
    else:
        print(Fore.RED + f"ID kereta '{target}' tidak ditemukan.")

def update_jadwal():
    jadwal = load_csv(JADWAL_FILE)
    if not jadwal:
        print(Fore.RED + "Belum ada jadwal untuk diupdate.")
        return

    lihat_jadwal()
    try:
        target = input("\nMasukkan ID kereta yang mau diupdate: ").strip()
    except KeyboardInterrupt:
        print(Fore.RED + "\nERROR: Jangan Tekan CTRL+C")
        return
    except EOFError:
        print(Fore.RED + "\nERROR: Jangan Tekan CTRL+Z")
        return

    for j in jadwal:
        if j["ID_Kereta"].lower() == target.lower():
            print("\nTekan Enter kalau tidak mau ubah kolom tertentu.")
            try:
                nama_baru = input(f"Nama Kereta [{j['Nama_Kereta']}]: ").strip()
                if nama_baru:
                    j["Nama_Kereta"] = nama_baru

                asal_baru = input(f"Asal [{j['Asal']}]: ").strip()
                if asal_baru:
                    j["Asal"] = asal_baru

                tujuan_baru = input(f"Tujuan [{j['Tujuan']}]: ").strip()
                if tujuan_baru:
                    j["Tujuan"] = tujuan_baru

                jam_input = input(f"Jam Berangkat [{j['Jam_Berangkat']}]: ").strip()
                if jam_input:
                    while True:
                        try:
                            jam_h, jam_m = jam_input.split(":")
                            jam_h, jam_m = int(jam_h), int(jam_m)
                            if 0 <= jam_h <= 23 and 0 <= jam_m <= 59:
                                j["Jam_Berangkat"] = f"{jam_h:02d}:{jam_m:02d}"
                                break
                            else:
                                print(Fore.RED + "Jam tidak valid! Harus antara 00:00 sampai 23:59.")
                        except ValueError:
                            print(Fore.RED + "Format jam salah! Gunakan format hh:mm, contoh 07:30.")
                        jam_input = input("Masukkan jam baru (hh:mm) atau tekan Enter untuk batal: ").strip()
                        if not jam_input:
                            break

                harga_baru = input(f"Harga [{j['Harga']}]: ").strip()
                if harga_baru:
                    if harga_baru.isdigit():
                        j["Harga"] = harga_baru
                    else:
                        print(Fore.RED + "Input harga tidak valid! Harga lama dipertahankan.")
            except KeyboardInterrupt:
                print(Fore.RED + "\nERROR: Jangan Tekan CTRL+C")
                return
            except EOFError:
                print(Fore.RED + "\nERROR: Jangan Tekan CTRL+Z")
                return

            save_csv(JADWAL_FILE, jadwal, ["ID_Kereta", "Nama_Kereta", "Asal", "Tujuan", "Jam_Berangkat", "Harga"])
            print(Fore.GREEN + "\nJadwal berhasil diupdate!\n")
            return

    print(Fore.RED + f"ID kereta '{target}' tidak ditemukan.")

def lihat_semua_transaksi():
    transaksi = load_csv(TRANSAKSI_FILE)
    if not transaksi:
        print("Belum ada transaksi.")
        return
    table = PrettyTable(["User", "ID", "Kereta", "Asal", "Tujuan", "Jam", "Harga", "Tanggal"])
    for t in transaksi:
        table.add_row([t["Nama_User"], t["ID_Kereta"], t["Nama_Kereta"], t["Asal"], t["Tujuan"], t["Jam_Berangkat"], t["Harga"], t["Tanggal_Transaksi"]])
    print(table)

def hapus_transaksi_user():
    transaksi = load_csv(TRANSAKSI_FILE)
    lihat_semua_transaksi()
    try:
        target = input("Masukkan nama user yang ingin dihapus transaksinya: ")
    except KeyboardInterrupt:
        print(Fore.RED + "\nERROR: Jangan Tekan CTRL+C")
        return
    except EOFError:
        print(Fore.RED + "\nERROR: Jangan Tekan CTRL+Z")
        return
    baru = [t for t in transaksi if t["Nama_User"] != target]
    save_csv(TRANSAKSI_FILE, baru, ["Nama_User", "ID_Kereta", "Nama_Kereta", "Asal", "Tujuan", "Jam_Berangkat", "Harga", "Tanggal_Transaksi"])
    print("Transaksi user berhasil dihapus!")

# --> ini buat pengguna/user

def beli_tiket(user):
    users = load_csv(USER_FILE)
    jadwal = load_csv(JADWAL_FILE)
    transaksi = load_csv(TRANSAKSI_FILE)

    lihat_jadwal()
    
    try:
        pilih = input("Masukkan ID Kereta yang ingin dibeli: ")
    except KeyboardInterrupt:
        print(Fore.RED + "\nERROR, Jangan Tekan CRTL+C")
        return beli_tiket(user)
    except EOFError:
        print(Fore.RED +"\nERROR, Jangan Tekan CRTL+Z")
        return beli_tiket(user)

    for j in jadwal:
        if j["ID_Kereta"] == pilih:
            harga = int(j["Harga"])
            saldo = int(user["Saldo"])
            if saldo < harga:
                print("Saldo tidak cukup!")
                return
            user["Saldo"] = str(saldo - harga)
            tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaksi.append({
                "Nama_User": user["Nama"],
                "ID_Kereta": j["ID_Kereta"],
                "Nama_Kereta": j["Nama_Kereta"],
                "Asal": j["Asal"],
                "Tujuan": j["Tujuan"],
                "Jam_Berangkat": j["Jam_Berangkat"],
                "Harga": j["Harga"],
                "Tanggal_Transaksi": tanggal
            })
            for u in users:
                if u["Nama"] == user["Nama"]:
                    u["Saldo"] = user["Saldo"]
            save_csv(USER_FILE, users, ["Nama", "Password", "Saldo", "Role"])
            save_csv(TRANSAKSI_FILE, transaksi, ["Nama_User", "ID_Kereta", "Nama_Kereta", "Asal", "Tujuan", "Jam_Berangkat", "Harga", "Tanggal_Transaksi"])
            print("Tiket berhasil dibeli!")
            return
    print("ID Kereta tidak ditemukan.")

def lihat_transaksi_user(user):
    transaksi = load_csv(TRANSAKSI_FILE)
    user_transaksi = [t for t in transaksi if t["Nama_User"] == user["Nama"]]
    if not user_transaksi:
        print("Belum ada transaksi.")
        return
    table = PrettyTable(["ID", "Kereta", "Asal", "Tujuan", "Jam", "Harga", "Tanggal"])
    for t in user_transaksi:
        table.add_row([t["ID_Kereta"], t["Nama_Kereta"], t["Asal"], t["Tujuan"], t["Jam_Berangkat"], t["Harga"], t["Tanggal_Transaksi"]])
    print(table)

def top_up(user):
    users = load_csv(USER_FILE)
    
    try:
        tambah = int(input("Masukkan jumlah top up: "))
    except ValueError:
        print(Fore.RED + "Input tidak valid! Masukkan angka.")
        return
    except KeyboardInterrupt:
        print(Fore.RED + "\nERROR, Jangan Tekan CRTL+C")
        return top_up(user)
    except EOFError:
        print(Fore.RED +"\nERROR, Jangan Tekan CRTL+Z")
        return top_up(user)
    
    if tambah <= 0:
        print(Fore.RED + "ERROR, Jangan -!")
        return top_up(user)
    
    saldo_sekarang = int(user["Saldo"])
    saldo_baru = saldo_sekarang + tambah

    if saldo_baru > 1000000:
        print(Fore.RED + "Saldo tidak boleh melebihi Rp1.000.000!")
        print(Fore.YELLOW + f"Saldo saat ini: Rp{saldo_sekarang:,}")
        print(Fore.YELLOW + f"Jumlah maksimal yang bisa ditambahkan: Rp{10_000_000 - saldo_sekarang:,}")
        return
    
    user["Saldo"] = str(saldo_baru)
    for u in users:
        if u["Nama"] == user["Nama"]:
            u["Saldo"] = user["Saldo"]
    save_csv(USER_FILE, users, ["Nama", "Password", "Saldo", "Role"])
    print(f"Top up berhasil! Saldo Anda sekarang: Rp{int(user['Saldo']):,}")

# ===== MENU ADMIN =====

def menu_admin():
    while True:
        print(Fore.RED +"===================================================")
        print(Fore.LIGHTYELLOW_EX +"                   MENU ADMIN                      ")
        print(Fore.RED +"===================================================")
        print(Fore.RED +"|"," 1. Lihat Jadwal Kereta                        ",Fore.RED +"|")
        print(Fore.RED +"|"," 2. Tambah Jadwal Kereta                       ",Fore.RED +"|")
        print(Fore.RED +"|"," 3. Update Jadwal Kereta                       ",Fore.RED +"|")
        print(Fore.RED +"|"," 4. Hapus Jadwal Kereta                        ",Fore.RED +"|")
        print(Fore.RED +"|"," 5. Lihat Semua Transaksi                      ",Fore.RED +"|")
        print(Fore.RED +"|"," 6. Hapus Transaksi User                       ",Fore.RED +"|")
        print(Fore.RED +"|"," 0. Logout                                     ",Fore.RED +"|")
        print(Fore.RED +"===================================================")
        try:
            pilih = input("Pilih menu: ")
        except KeyboardInterrupt:
            print(Fore.RED + "\nERROR, Jangan Tekan CRTL+C")
            continue
        except EOFError:
            print(Fore.RED +"\nERROR, Jangan Tekan CRTL+Z")
            continue

        if pilih == "1":
            lihat_jadwal()
        elif pilih == "2":
            tambah_jadwal()
        elif pilih == "3":
            update_jadwal()
        elif pilih == "4":
            hapus_jadwal()
        elif pilih == "5":
            lihat_semua_transaksi()
        elif pilih == "6":
            hapus_transaksi_user()
        elif pilih == "0":
            clear()
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid!")

# ===== MENU USER =====
def menu_user(user):
    while True:
        print(Fore.RED +"\n===================================================")
        print(Fore.LIGHTYELLOW_EX + f"         Silahkan Memesan Tiket ({user['Nama']})            ")
        print(Fore.LIGHTYELLOW_EX + f"           Saldo Anda: Rp{int(user['Saldo']):,}           ")
        print(Fore.RED +"===================================================")
        print("1. Lihat Jadwal Kereta")
        print("2. Top Up saldo")
        print("3. Beli Tiket Kereta")
        print("4. Lihat Riwayat Transaksi")
        print("0. Logout")
        try:
            pilih = input("Pilih menu: ")
        except KeyboardInterrupt:
            print(Fore.RED + "\n\nERROR, Jangan Tekan CRTL+C")
            continue
        except EOFError:
            print(Fore.RED +"\nERROR, Jangan Tekan CRTL+Z")
            continue

        if pilih == "1":
            lihat_jadwal()
        elif pilih == "2":
            top_up(user)
        elif pilih == "3":
            beli_tiket(user)
        elif pilih == "4":
            lihat_transaksi_user(user)
        elif pilih == "0":
            clear()
            print("Logout berhasil.")
            break
        else:
            print(Fore.RED +"Pilihan tidak valid!")

def main():
    while True:
        print(Fore.RED +"\n===================================================")
        print(Fore.RED +"|",Fore.LIGHTYELLOW_EX +"        PEMESANAN TIKET KERETA API DIGTAL      ",Fore.RED +"|")
        print(Fore.RED +"===================================================")
        print(Fore.RED +"|"," 1. Login                                      ",Fore.RED +"|")
        print(Fore.RED +"|"," 2. Register                                   ",Fore.RED +"|")
        print(Fore.RED +"|"," 3. Keluar                                     ",Fore.RED +"|")
        print(Fore.RED +"===================================================")
        try:
            pilih = input("Pilih menu: ")
        except KeyboardInterrupt:
            time.sleep(0.5)
            print(Fore.RED + "\n\nERROR, Jangan Tekan CRTL+C")
            continue
        except EOFError:
            time.sleep(0.5)
            print(Fore.RED +"\nERROR, Jangan Tekan CRTL+Z")
            continue

        if pilih == "1":
            login()
        elif pilih == "2":
            register()
        elif pilih == "3":
            print(Fore.YELLOW +"\nTerima kasih, program selesai.")
            break
        else:
            time.sleep(0.5)
            print(Fore.RED +"\nPilihan tidak valid!")

loading_welcome()
main()
