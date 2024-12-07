import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import math
from PIL import Image, ImageTk
import csv

# Variabel global untuk menyimpan data
data_parkir = {"jenis_kendaraan": None, "nomor_plat": None, "waktu_masuk": None, "waktu_keluar": None, "harga_parkir": None}

# Fungsi untuk memeriksa username dan password
def check_login(username, password):
    try:
        with open('logindata.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username and row['password'] == password:
                    return True
    except FileNotFoundError:
        messagebox.showerror("Error", "File logindata.csv tidak ditemukan.")
    return False

# Fungsi untuk menangani klik tombol Login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if check_login(username, password):
        messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
        kembali_ke_menu()
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah.")
    
# Fungsi kendaraan masuk
def kendaraan_masuk():
    for widget in root.winfo_children():
        widget.destroy()
    
    set_background(root)
    
    tk.Label(root, text="Kendaraan Masuk").pack()
    kendaraan_var = tk.StringVar(value="motor")
    
    tk.Radiobutton(root, text="Motor", variable=kendaraan_var, value="motor").pack()
    tk.Radiobutton(root, text="Mobil", variable=kendaraan_var, value="mobil").pack()

    tk.Label(root, text="Masukkan Nomor Plat").pack()
    nomor_plat_entry = tk.Entry(root)
    nomor_plat_entry.pack()

    def simpan_masuk():
        data_parkir["jenis_kendaraan"] = kendaraan_var.get()
        data_parkir["nomor_plat"] = nomor_plat_entry.get().strip()
        
        # Validasi nomor plat kendaraan
        if not data_parkir["nomor_plat"]:
            messagebox.showerror("Error", "Nomor plat kendaraan harus diisi.")
            return
        if len(data_parkir["nomor_plat"]) < 5 or len(data_parkir["nomor_plat"]) > 11:
            messagebox.showerror("Error", "Nomor plat kendaraan harus memiliki 5 hingga 11 karakter.")
            return
    
        waktu_masuk_pintu_masuk()
    tk.Button(root, text="Simpan", command=simpan_masuk).pack()
    tk.Button(root, text="Kembali", command=kembali_ke_menu).pack()
    
def waktu_masuk_pintu_masuk():
    for widget in root.winfo_children():
            widget.destroy()
            
    set_background(root)
        
    tk.Label(root, text="Waktu Masuk", bg= "#FFACC5", fg= "black").pack(pady=10)
    waktu_label = tk.Label(root, text="",bg= "pink", fg= "black")
    waktu_label.pack()
    
    def capture_waktu_masuk():
        now = datetime.now()
        waktu_masuk = now.strftime("%H.%M")
        tanggal_masuk = now.strftime("%d-%m-%Y")
        hari_masuk = now.strftime("%A")
        waktu_label.config(text=f"Tanggal: {tanggal_masuk}\nWaktu: {waktu_masuk}\nHari: {hari_masuk}")
        capture_button.destroy()
        cetak_button.config(state="normal")
        
        data_parkir["waktu_masuk"] = waktu_masuk
        data_parkir["tanggal_masuk"] = tanggal_masuk
        data_parkir["hari_masuk"] = hari_masuk
     
        
    capture_button = tk.Button(root, text="Tekan Tombol Masuk", command=capture_waktu_masuk)
    capture_button.pack(pady=10)
    
    cetak_button = tk.Button(text="Cetak Karcis", state="disabled", command=lambda: cetak_karcis())
      
    def cetak_karcis():
        jenis_kendaraan = data_parkir.get("jenis_kendaraan", "Tidak diketahui")
        nomor_plat = data_parkir.get("nomor_plat", "Tidak diketahui")
        waktu_masuk = data_parkir.get("waktu_masuk", "Tidak diketahui")
        tanggal_masuk = data_parkir.get("tanggal_masuk", "Tidak diketahui")
        hari_masuk = data_parkir.get("hari_masuk", "Tidak diketahui")
        # Tampilkan messagebox dengan informasi kendaraan
        messagebox.showinfo(
            "Karcis Parkir",
            f"Jenis Kendaraan: {jenis_kendaraan}\n"
            f"Nomor Plat: {nomor_plat}\n"
            f"Hari Masuk: {hari_masuk}\n"
            f"Tanggal Masuk: {tanggal_masuk}\n"
            f"Waktu Masuk: {waktu_masuk}")
        kembali_ke_menu()
    cetak_button.pack(pady=10)
    
def simpan_data(waktu_window):
    # Menyimpan data dan menutup jendela waktu
    messagebox.showinfo("Sukses", "Data kendaraan masuk berhasil disimpan.")
    waktu_window.destroy()
    kembali_ke_menu() 
    
# Fungsi untuk menyimpan data ke CSV
csv_file = "database.csv"
def simpan_ke_csv(jenis_kendaraan, nomor_plat, tanggal_masuk, waktu_masuk, waktu_keluar,lama_parkir, harga_parkir):
    # Jika file belum ada, buat file baru dengan header
    try:
        header = ["Jenis Kendaraan", "Nomor Plat", "Tanggal Masuk", "Waktu Masuk", "Waktu Keluar", "Lama Parkir", "Harga Parkir"]
        file_baru = False

        # Periksa apakah file CSV sudah ada
        try:
            with open(csv_file, "r") as f:
                pass
        except FileNotFoundError:
            file_baru = True

        # Tulis data ke file CSV
        with open(csv_file, "a", newline="") as f:
            writer = csv.writer(f)
            if file_baru:
                writer.writerow(header)  # Tulis header jika file baru
            writer.writerow([jenis_kendaraan, nomor_plat, tanggal_masuk, waktu_masuk, waktu_keluar, lama_parkir, harga_parkir])
        messagebox.showinfo("Sukses", f"Data berhasil disimpan ke {csv_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan data ke CSV: {str(e)}")
    
 # Fungsi untuk kendaraan keluar
def kendaraan_keluar():
    for widget in root.winfo_children():
        widget.destroy()
    
    set_background(root)
        
    tk.Label(root, text="Kendaraan Keluar").pack()
    kendaraan_var = tk.StringVar(value="motor")
    
    tk.Radiobutton(root, text="Motor", variable=kendaraan_var, value="motor").pack()
    tk.Radiobutton(root, text="Mobil", variable=kendaraan_var, value="mobil").pack()

    tk.Label(root, text="Masukkan Nomor Plat").pack()
    nomor_plat_entry = tk.Entry(root)
    nomor_plat_entry.pack()

    def simpan_1():
        data_parkir["jenis_kendaraan"] = kendaraan_var.get()
        data_parkir["nomor_plat"] = nomor_plat_entry.get().strip()
        
        # Validasi nomor plat kendaraan
        if not data_parkir["nomor_plat"]:
            messagebox.showerror("Error", "Nomor plat kendaraan harus diisi.")
            return
        if len(data_parkir["nomor_plat"]) < 5 or len(data_parkir["nomor_plat"]) > 11:
            messagebox.showerror("Error", "Nomor plat kendaraan harus memiliki 5 hingga 11 karakter.")
            return
    
        waktu_masuk_pintu_keluar()
    tk.Button(root, text="Simpan", command=simpan_1).pack()
    tk.Button(root, text="Kembali", command=kembali_ke_menu).pack()
        
def waktu_masuk_pintu_keluar():
    for widget in root.winfo_children():
            widget.destroy()
            
    set_background(root)
        
    # Label untuk waktu masuk
    tk.Label(root, text="Waktu Masuk (Manual)", bg="#FFACC5", fg="black").pack(pady=10)

    # Label untuk Tanggal dan Waktu
    tk.Label(root, text="Masukkan Tanggal (DD-MM-YYYY)").pack(pady=5)
    tanggal_entry = tk.Entry(root)
    tanggal_entry.pack(pady=5)

    tk.Label(root, text="Masukkan Waktu (HH.MM)").pack(pady=5)
    waktu_entry = tk.Entry(root)
    waktu_entry.pack(pady=5)

    def simpan_2():
        # Ambil input dari entri
        tanggal_masuk_manual = tanggal_entry.get().strip()
        waktu_masuk_manual = waktu_entry.get().strip()

        # Validasi input tanggal dan waktu
        try:
            # Cek format tanggal dan waktu yang benar
            datetime.strptime(tanggal_masuk_manual, "%d-%m-%Y")
            datetime.strptime(waktu_masuk_manual, "%H.%M")
            datetime.strptime(f"{tanggal_masuk_manual} {waktu_masuk_manual}", "%d-%m-%Y %H.%M")
        except ValueError:
            messagebox.showerror("Error", "Format tanggal atau waktu tidak valid. Gunakan format DD-MM-YYYY untuk tanggal dan HH.MM untuk waktu.")
            return

        # Simpan data ke dictionary
        data_parkir["tanggal_masuk"] = tanggal_masuk_manual
        data_parkir["waktu_masuk"] = waktu_masuk_manual
        
        waktu_keluar()
    tk.Button(root, text="Simpan", command=simpan_2).pack()
    
def waktu_keluar():
    for widget in root.winfo_children():
            widget.destroy() 
            
    set_background(root)
    
    tk.Label(root, text="Waktu Keluar", fg= "black", bg= "pink").pack(pady=10)

    waktu_keluar_entry = tk.Entry(root)
    tanggal_keluar_entry = tk.Entry(root)
    hari_label = tk.Label(root, text="")

    def capture_waktu_keluar():
        now = datetime.now()
        waktu_keluar_entry.delete(0, tk.END)
        tanggal_keluar_entry.delete(0, tk.END)
        waktu_keluar_entry.insert(0, now.strftime("%H.%M"))
        tanggal_keluar_entry.insert(0, now.strftime("%d-%m-%Y"))
        hari_label.config(text=f"Hari: {now.strftime('%A')}")

    capture_button = tk.Button(root, text="Serahkan Karcis", command=capture_waktu_keluar)
    capture_button.pack(pady=10)

    tk.Label(root, text="Waktu Keluar (HH.MM)",bg= "pink", fg= "black").pack()
    waktu_keluar_entry= tk.Entry(root, bg= "lightgrey", fg= "black")
    waktu_keluar_entry.pack()

    tk.Label(root, text="Tanggal Keluar (DD-MM-YYYY)",bg= "pink", fg= "black").pack()
    tanggal_keluar_entry= tk.Entry(root, bg= "lightgrey", fg= "black")
    tanggal_keluar_entry.pack()

    hari_label.pack()   
 
    def simpan_waktu_keluar():
        tanggal_masuk = data_parkir.get("tanggal_masuk", "")
        waktu_masuk = data_parkir.get("waktu_masuk", "")
        waktu = waktu_keluar_entry.get()
        tanggal = tanggal_keluar_entry.get()
        try:
            datetime_keluar = datetime.strptime(f"{tanggal} {waktu}", "%d-%m-%Y %H.%M")
            datetime_masuk = datetime.strptime(f"{tanggal_masuk} {waktu_masuk}", "%d-%m-%Y %H.%M")

            if datetime_keluar <= datetime_masuk:
                messagebox.showerror("Error", "Waktu keluar harus lebih besar dari waktu masuk.")
                return

            data_parkir["waktu_keluar"] = f"{tanggal} {waktu}"
            hitung_biaya_parkir()
        except ValueError:
            messagebox.showerror("Error", "Format waktu atau tanggal tidak valid.")

    tk.Button(root, text="Hitunglah Biaya Parkir", command=simpan_waktu_keluar).pack(pady=10)  
    
 # Fungsi untuk menghitung biaya parkir
def hitung_biaya_parkir():
    try:
        # Ambil data dari variabel global
        jenis_kendaraan = data_parkir["jenis_kendaraan"]
        nomor_plat = data_parkir["nomor_plat"]
        tanggal_masuk = data_parkir["tanggal_masuk"]  # Tanggal masuk
        waktu_masuk = data_parkir["waktu_masuk"]  # Waktu masuk
        waktu_keluar = data_parkir["waktu_keluar"]  # Waktu keluar

        # Gabungkan tanggal dan waktu untuk datetime masuk dan keluar
        datetime_masuk = datetime.strptime(f"{tanggal_masuk} {waktu_masuk}", "%d-%m-%Y %H.%M")
        datetime_keluar = datetime.strptime(waktu_keluar, "%d-%m-%Y %H.%M")

        # Hitung durasi parkir dalam jam
        selisih_waktu = datetime_keluar - datetime_masuk
        lama_parkir = math.ceil(selisih_waktu.total_seconds() / 3600)

        # Validasi jika durasi negatif
        if lama_parkir <= 0:
            messagebox.showerror("Error", "Waktu keluar harus lebih besar dari waktu masuk.")
            return

        # Hitung biaya parkir berdasarkan jenis kendaraan
        if jenis_kendaraan == "motor":
            harga_parkir = 2000 + max(0, lama_parkir - 1) * 1000
        elif jenis_kendaraan == "mobil":
            harga_parkir = 3000 + max(0, lama_parkir - 1) * 2000
        else:
            messagebox.showerror("Error", "Jenis kendaraan tidak valid.")
            return
        simpan_ke_csv (jenis_kendaraan, nomor_plat, data_parkir["tanggal_masuk"], data_parkir["waktu_masuk"], data_parkir["waktu_keluar"], lama_parkir, harga_parkir)
        
        # Tampilkan hasil
        messagebox.showinfo("Hasil",
            f"Jenis Kendaraan: {jenis_kendaraan.capitalize()}\n"
            f"Nomor Plat: {nomor_plat}\n"
            f"Waktu Masuk: {waktu_masuk} ({datetime_masuk.strftime('%A')})\n"
            f"Tanggal Masuk: {tanggal_masuk}\n\n"
            f"Waktu Keluar: {datetime_keluar.strftime('%H.%M')} ({datetime_keluar.strftime('%A')})\n"
            f"Tanggal Keluar: {datetime_keluar.strftime('%d-%m-%Y')}\n\n"
            f"Lama Parkir: {lama_parkir} jam\n"
            f"Biaya Parkir: Rp{harga_parkir}")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
    kembali_ke_menu()
           
# Fungsi untuk kembali ke menu utama
def kembali_ke_menu():
    for widget in root.winfo_children():
        widget.destroy()
        
    set_background(root)

    tk.Label(root, text="Sistem Parkir", font=("Arial", 16)).pack()
    tk.Button(root, text="Kendaraan Masuk", command=kendaraan_masuk).pack()
    tk.Button(root, text="Kendaraan Keluar", command=kendaraan_keluar).pack()   
                
def set_background(window):
    image_path = "pink.png"  # Ganti dengan nama file gambar Anda
    img = Image.open(image_path)
    img = img.resize((500, 300))  # Sesuaikan ukuran dengan window
    bg_image = ImageTk.PhotoImage(img)
    bg_label = tk.Label(window, image=bg_image)
    bg_label.image = bg_image  # Simpan referensi agar gambar tidak hilang
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
# Main window
root = tk.Tk()
root.title("Sistem Parkir")
root.geometry("500x300")

set_background(root)

# Membuat form login
tk.Label(root, text="Username:", bg= "#FFACC5", fg= "black").pack(pady=10, padx=50)
username_entry = tk.Entry(root)
username_entry.pack(pady=10, padx=50)

tk.Label(root, text="Password:", bg= "#FFACC5", fg= "black").pack(pady=10, padx=50)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10, padx=50)

login_button = tk.Button(root, text="Login", bg= "lightgrey", fg= "black", command=login)
login_button.pack(pady=10, padx=50)

root.mainloop()   