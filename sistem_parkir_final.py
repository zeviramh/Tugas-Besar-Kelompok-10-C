import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import math
from PIL import Image, ImageTk
import random
import csv

def generate_nomor_karcis():
    """Generate nomor karcis unik."""
    return f"K-{random.randint(1000, 9999)}"

# Variabel global untuk menyimpan data
data_parkir = {"jenis_kendaraan": None, "nomor_plat": None, "waktu_masuk": None, "waktu_keluar": None, "harga_parkir": None}
# Variabel global untuk menyimpan data kendaraan yang tercatat
data_parkir_tercatat = {}

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
    
    kendaraan_masuk_label = tk.Label(root, text="Kendaraan Masuk", font=("Cascadia Code", 20, "bold"), bg= "#FFACC5", fg= "black")
    kendaraan_masuk_label.place(relx=0.5, rely=0.1, anchor='center')
    kendaraan_var = tk.StringVar(value="motor")
    
    radio_motor = tk.Radiobutton(root, text="Motor",font=("Cascadia Code", 16), variable=kendaraan_var, value="motor", bg= "#FFACC5", fg= "black")
    radio_motor.place(relx=0.5, rely=0.2, anchor='center')
    radio_mobil = tk.Radiobutton(root, text="Mobil",font=("Cascadia Code", 16), variable=kendaraan_var, value="mobil", bg= "#FFACC5", fg= "black")
    radio_mobil.place(relx=0.5, rely=0.3, anchor='center')

    nomor_plat_label = tk.Label(root, text="Masukkan Nomor Plat", font=("Cascadia Code", 18, ), bg= "#FFACC5", fg= "black")
    nomor_plat_label.place(relx=0.5, rely=0.4, anchor='center')
    nomor_plat_entry = tk.Entry(root, font=("Cascadia Code", 16))
    nomor_plat_entry.place(relx=0.5, rely=0.5, anchor='center')
    
    # Generate nomor karcis dan simpan di data_parkir
    nomor_karcis = generate_nomor_karcis()
    data_parkir["nomor_karcis"] = nomor_karcis
    

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
        
        # Simpan tanggal dan waktu masuk
        now = datetime.now()
        data_parkir["tanggal_masuk"] = now.strftime("%d-%m-%Y")
        data_parkir["waktu_masuk"] = now.strftime("%H.%M")
        data_parkir["hari_masuk"] = now.strftime("%A")
            
        # Simpan data berdasarkan nomor karcis
        data_parkir_tercatat[data_parkir["nomor_karcis"]] = {
        "jenis_kendaraan": data_parkir["jenis_kendaraan"],
        "nomor_plat": data_parkir["nomor_plat"],
        "tanggal_masuk": data_parkir.get("tanggal_masuk", ""),
        "waktu_masuk": data_parkir.get("waktu_masuk", "")
        }
    
        waktu_masuk_pintu_masuk()
    simpan_button = tk.Button(root, text="Simpan", font=("Cascadia Code", 14), command=simpan_masuk)
    simpan_button.place(relx=0.5, rely=0.6, anchor='center')
    kembali_button = tk.Button(root, text="Kembali",font=("Cascadia Code", 14), command=kembali_ke_menu)
    kembali_button.place(relx=0.5, rely=0.7, anchor='center')
    
def waktu_masuk_pintu_masuk():
    for widget in root.winfo_children():
            widget.destroy()
            
    set_background(root)
        
    waktu_masuk_label = tk.Label(root, text="Waktu Masuk", font=("Cascadia Code", 20, "bold"), bg= "#FFACC5", fg= "black")
    waktu_masuk_label.place(relx=0.5, rely=0.2, anchor='center')
    waktu_label = tk.Label(root, text="",font=("Cascadia Code", 16),bg= "pink", fg= "black")
    waktu_label.place(relx=0.5, rely=0.3, anchor='center')
    
    def capture_waktu_masuk():
        now = datetime.now()
        waktu_masuk = now.strftime("%H.%M")
        tanggal_masuk = now.strftime("%d-%m-%Y")
        hari_masuk = now.strftime("%A")
        nomor_karcis = data_parkir["nomor_karcis"]
        waktu_label.config(text=f"Tanggal: {tanggal_masuk}\nWaktu: {waktu_masuk}\nHari: {hari_masuk}")
        capture_button.destroy()
        cetak_button.config(state="normal")
        
        data_parkir["waktu_masuk"] = waktu_masuk
        data_parkir["tanggal_masuk"] = tanggal_masuk
        data_parkir["hari_masuk"] = hari_masuk
     
        
    capture_button = tk.Button(root, text="Tekan Tombol Masuk",font=("Cascadia Code", 16), command=capture_waktu_masuk)
    capture_button.place(relx=0.5, rely=0.4, anchor='center')
    
    cetak_button = tk.Button(text="Cetak Karcis",font=("Cascadia Code", 16), state="disabled", command=lambda: cetak_karcis())
    cetak_button.place(relx=0.5, rely=0.5, anchor='center')
      
    def cetak_karcis():
        jenis_kendaraan = data_parkir.get("jenis_kendaraan", "Tidak diketahui")
        nomor_plat = data_parkir.get("nomor_plat", "Tidak diketahui")
        waktu_masuk = data_parkir.get("waktu_masuk", "Tidak diketahui")
        tanggal_masuk = data_parkir.get("tanggal_masuk", "Tidak diketahui")
        hari_masuk = data_parkir.get("hari_masuk", "Tidak diketahui")
        nomor_karcis = data_parkir.get("nomor_karcis", "Tidak diketahui")
        
        # Tampilkan messagebox dengan informasi kendaraan
        messagebox.showinfo(
            "Karcis Parkir",
            f"Jenis Kendaraan: {jenis_kendaraan}\n"
            f"Nomor Plat: {nomor_plat}\n"
            f"Hari Masuk: {hari_masuk}\n"
            f"Tanggal Masuk: {tanggal_masuk}\n"
            f"Waktu Masuk: {waktu_masuk}\n"
            f"Nomor Karcis: {nomor_karcis}")
        
        kembali_ke_menu()
    
def simpan_data(waktu_window):
    # Menyimpan data dan menutup jendela waktu
    messagebox.showinfo("Sukses", "Data kendaraan masuk berhasil disimpan.")
    waktu_window.destroy()
    kembali_ke_menu() 
    
# Fungsi untuk menyimpan data ke CSV
csv_file = "database.csv"
def simpan_ke_csv(nomor_karcis,jenis_kendaraan, nomor_plat, tanggal_masuk, waktu_masuk, waktu_keluar,lama_parkir, harga_parkir):
    # Jika file belum ada, buat file baru dengan header
    try:
        header = ["Nomor Karcis", "Jenis Kendaraan", "Nomor Plat", "Tanggal Masuk", "Waktu Masuk", "Waktu Keluar", "Lama Parkir", "Harga Parkir"]
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
            writer.writerow([nomor_karcis,jenis_kendaraan, nomor_plat, tanggal_masuk, waktu_masuk, waktu_keluar, lama_parkir, harga_parkir])
        messagebox.showinfo("Sukses", f"Data berhasil disimpan")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan data")
    
 # Fungsi untuk kendaraan keluar
def kendaraan_keluar():
    for widget in root.winfo_children():
        widget.destroy()
    
    set_background(root)
        
    kendaraan_keluar_label = tk.Label(root, text="Kendaraan Keluar", font=("Cascadia Code", 20 , "bold"), bg= "#FFACC5", fg= "black")
    kendaraan_keluar_label.place(relx=0.5, rely=0.2, anchor='center')
    nomor_karcis_label = tk.Label(root, text="Masukkan Nomor Karcis", font=("Cascadia Code", 16), bg="#FFACC5", fg="black")
    nomor_karcis_label.place(relx=0.5, rely=0.3, anchor='center')
    nomor_karcis_entry = tk.Entry(root, font=("Cascadia Code", 16))
    nomor_karcis_entry.place(relx=0.5, rely=0.4, anchor='center')

    def cari_data_karcis():
        nomor_karcis = nomor_karcis_entry.get().strip()

        # Validasi input nomor karcis
        if not nomor_karcis:
            messagebox.showerror("Error", "Nomor karcis harus diisi.")
            return
        
        # Cari data berdasarkan nomor karcis
        data = data_parkir_tercatat.get(nomor_karcis)
        if not data:
            messagebox.showerror("Error", "Nomor karcis tidak ditemukan.")
            return

        # Tampilkan informasi kendaraan
        jenis_kendaraan = data.get("jenis_kendaraan", "Tidak diketahui")
        nomor_plat = data.get("nomor_plat", "Tidak diketahui")
        tanggal_masuk = data.get("tanggal_masuk", "Tidak diketahui")
        waktu_masuk = data.get("waktu_masuk", "Tidak diketahui")

        messagebox.showinfo("Data Karcis",
            f"Nomor Karcis: {nomor_karcis}\n"
            f"Jenis Kendaraan: {jenis_kendaraan}\n"
            f"Nomor Plat: {nomor_plat}\n"
            f"Tanggal Masuk: {tanggal_masuk}\n"
            f"Waktu Masuk: {waktu_masuk}")
        
        # Lanjut ke proses waktu keluar
        waktu_keluar()

    cari_data_karcis_button = tk.Button(root, text="Cari Data Karcis", font=("Cascadia Code", 16), command=cari_data_karcis)
    cari_data_karcis_button.place(relx=0.5, rely=0.5, anchor='center')
    kembali_button = tk.Button(root, text="Kembali",font=("Cascadia Code", 16), command=kembali_ke_menu)
    kembali_button.place(relx=0.5, rely=0.6, anchor='center')
    
def waktu_keluar():
    for widget in root.winfo_children():
            widget.destroy() 
            
    set_background(root)
    
    waktu_keluar_label = tk.Label(root, text="Waktu Keluar", font=("Cascadia Code", 18), fg= "black", bg= "pink")
    waktu_keluar_label.place(relx=0.5, rely=0.1, anchor='center')

    waktu_keluar_entry = tk.Entry(root, font= ("Cascadia Code", 16))
    tanggal_keluar_entry = tk.Entry(root, font= ("Cascadia Code", 16))
    hari_label = tk.Label(root, text="",font= ("Cascadia Code", 16))

    def capture_waktu_keluar():
        now = datetime.now()
        waktu_keluar_entry.delete(0, tk.END)
        tanggal_keluar_entry.delete(0, tk.END)
        waktu_keluar_entry.insert(0, now.strftime("%H.%M"))
        tanggal_keluar_entry.insert(0, now.strftime("%d-%m-%Y"))
        hari_label.config(text=f"Hari: {now.strftime('%A')}")

    capture_button = tk.Button(root, text="Serahkan Karcis", font= ("Cascadia Code", 16), command=capture_waktu_keluar)
    capture_button.place(relx=0.5, rely=0.2, anchor='center')

    waktu_keluar_label = tk.Label(root, text="Waktu Keluar (HH.MM)",font= ("Cascadia Code", 16),bg= "pink", fg= "black")
    waktu_keluar_label.place(relx=0.5, rely=0.3, anchor='center')
    waktu_keluar_entry= tk.Entry(root, font= ("Cascadia Code", 16), bg= "lightgrey", fg= "black")
    waktu_keluar_entry.place(relx=0.5, rely=0.4, anchor='center')

    tanggal_keluar_label = tk.Label(root, text="Tanggal Keluar (DD-MM-YYYY)", font= ("Cascadia Code", 16),bg= "pink", fg= "black")
    tanggal_keluar_label.place(relx=0.5, rely=0.5, anchor='center')
    tanggal_keluar_entry= tk.Entry(root, font= ("Cascadia Code", 16), bg= "lightgrey", fg= "black")
    tanggal_keluar_entry.place(relx=0.5, rely=0.6, anchor='center')

    hari_label.place(relx=0.5, rely=0.7, anchor='center')  
 
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

    biaya_parkir_label = tk.Button(root, text="Hitunglah Biaya Parkir",font= ("Cascadia Code", 16), command=simpan_waktu_keluar)
    biaya_parkir_label.place(relx=0.5, rely=0.8, anchor='center')
    
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
        simpan_ke_csv (data_parkir["nomor_karcis"],jenis_kendaraan, nomor_plat, data_parkir["tanggal_masuk"], data_parkir["waktu_masuk"], data_parkir["waktu_keluar"], lama_parkir, harga_parkir)
        
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

    pilihan_menu_label = tk.Label(root, text="PILIHAN MENU", font= ("Cascadia Code", 28, "bold"), bg= "#FFACC5", fg= "black")
    pilihan_menu_label.place(relx=0.5, rely=0.3, anchor='center')
    kendaraan_masuk_button = tk.Button(root, text="Kendaraan Masuk",font= ("Cascadia Code", 16), command=kendaraan_masuk, bg= "lightgrey", fg= "black")
    kendaraan_masuk_button.place(relx=0.5, rely=0.4, anchor='center')
    kendaraan_keluar_button = tk.Button(root, text="Kendaraan Keluar", font= ("Cascadia Code", 16),command=kendaraan_keluar, bg= "lightgrey", fg= "black")
    kendaraan_keluar_button.place(relx=0.5, rely=0.5, anchor='center')
                
def set_background(window):
    image_path = "pinkbg.png"  # Ganti dengan nama file gambar Anda
    img = Image.open(image_path)
    img = img.resize((1920, 1080))  # Sesuaikan ukuran dengan window
    bg_image = ImageTk.PhotoImage(img)
    bg_label = tk.Label(window, image=bg_image)
    bg_label.image = bg_image  # Simpan referensi agar gambar tidak hilang
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
# Main window
root = tk.Tk()
root.title("Sistem Parkir")
root.geometry("1920x1080")

width = root.winfo_width()
height = root.winfo_height()

set_background(root)

# Membuat form login
username_label = tk.Label(root, text="Username:",font=("Cascadia Code", 16), bg= "#FFACC5", fg= "black") 
username_label.place(relx=0.5, rely=0.2, anchor='center')
username_entry = tk.Entry(root, font=("Cascadia Code", 16))
username_entry.place(relx=0.5, rely=0.3, anchor='center')

password_label = tk.Label(root, text="Password:",font=("Cascadia Code", 16), bg= "#FFACC5", fg= "black")
password_label.place(relx=0.5, rely=0.4, anchor='center')
password_entry = tk.Entry(root, font=("Cascadia Code", 16), show="*")
password_entry.place(relx=0.5, rely=0.5, anchor='center')

login_button = tk.Button(root, text="Login",font=("Cascadia Code", 16), bg= "lightgrey", fg= "black", command=login)
login_button.place(relx=0.5, rely=0.6, anchor='center')

root.mainloop()   