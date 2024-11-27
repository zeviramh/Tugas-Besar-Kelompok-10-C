import tkinter as tk
from tkinter import messagebox
import math
from datetime import datetime

# Fungsi untuk menghitung biaya parkir
def hitung_biaya_parkir():
    jenis_kendaraan = kendaraan_var.get()
    waktu_masuk = waktu_masuk_entry.get()
    waktu_keluar = waktu_keluar_entry.get()
    tanggal_masuk = tanggal_masuk_entry.get()
    tanggal_keluar = tanggal_keluar_entry.get()
    
    try:
        # Validasi dan konversi tanggal dan waktu masuk
        datetime_masuk = datetime.strptime(f"{tanggal_masuk} {waktu_masuk}", "%d-%m-%Y %H.%M")
        
        # Validasi dan konversi tanggal dan waktu keluar
        datetime_keluar = datetime.strptime(f"{tanggal_keluar} {waktu_keluar}", "%d-%m-%Y %H.%M")
        
        # Hitung selisih waktu dalam jam
        selisih_waktu = datetime_keluar - datetime_masuk
        lama_parkir = math.ceil(selisih_waktu.total_seconds() / 3600)  # Total detik dikonversi ke jam, lalu dibulatkan ke atas
        
        if lama_parkir < 0:
            messagebox.showerror("Error", "Waktu keluar harus lebih besar dari waktu masuk.")
            return
        
        # Menghitung harga parkir berdasarkan jenis kendaraan
        if jenis_kendaraan == "motor":
            if lama_parkir <= 1:
                harga_parkir = 2000
            else:
                harga_parkir = (lama_parkir - 1) * 1000 + 2000
        elif jenis_kendaraan == "mobil":
            if lama_parkir <= 1:
                harga_parkir = 3000
            else:
                harga_parkir = (lama_parkir - 1) * 2000 + 3000
        else:
            messagebox.showerror("Error", "Jenis kendaraan tidak valid.")
            return
        
        # Menampilkan hasil
        messagebox.showinfo("Hasil", f"Waktu Masuk: {datetime_masuk.strftime('%H.%M')}, {datetime_masuk.strftime('%A')}\n"
                                      f"Waktu Keluar: {datetime_keluar.strftime('%H.%M')}, {datetime_keluar.strftime('%A')}\n"
                                      f"Biaya parkir untuk {jenis_kendaraan} selama {lama_parkir} jam adalah: Rp{harga_parkir}")
    except ValueError:
        messagebox.showerror("Error", "Format waktu atau tanggal tidak valid. Gunakan format HH.MM untuk waktu dan DD-MM-YYYY untuk tanggal.")

# Fungsi untuk menangkap waktu masuk
def capture_waktu_masuk():
    now = datetime.now()
    waktu_masuk_entry.config(state="normal")
    waktu_masuk_entry.delete(0, tk.END)
    waktu_masuk_entry.insert(0, now.strftime("%H.%M"))
    waktu_masuk_entry.config(state="readonly")
    
    tanggal_masuk_entry.config(state="normal")
    tanggal_masuk_entry.delete(0, tk.END)
    tanggal_masuk_entry.insert(0, now.strftime("%d-%m-%Y"))
    tanggal_masuk_entry.config(state="readonly")

# Fungsi untuk menangkap waktu keluar
def capture_waktu_keluar():
    now = datetime.now()
    waktu_keluar_entry.delete(0, tk.END)
    waktu_keluar_entry.insert(0, now.strftime("%H.%M"))
    tanggal_keluar_entry.delete(0, tk.END)
    tanggal_keluar_entry.insert(0, now.strftime("%d-%m-%Y"))

# Membuat GUI dengan Tkinter
root = tk.Tk()
root.title("Kalkulator Biaya Parkir")

# Label dan radio button untuk memilih jenis kendaraan
tk.Label(root, text="Jenis Kendaraan:").grid(row=0, column=0, padx=10, pady=10)
kendaraan_var = tk.StringVar(value="motor")  # Default value
tk.Radiobutton(root, text="Motor", variable=kendaraan_var, value="motor").grid(row=0, column=1, padx=10, pady=10, sticky="w")
tk.Radiobutton(root, text="Mobil", variable=kendaraan_var, value="mobil").grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Entry dan tombol untuk waktu masuk
tk.Label(root, text="Waktu Masuk (HH.MM):").grid(row=2, column=0, padx=10, pady=10)
waktu_masuk_entry = tk.Entry(root, state="readonly")
waktu_masuk_entry.grid(row=2, column=1, padx=10, pady=10)

capture_masuk_button = tk.Button(root, text="Tekan Tombol", command=capture_waktu_masuk)
capture_masuk_button.grid(row=2, column=2, padx=10, pady=10)

tk.Label(root, text="Tanggal Masuk (DD-MM-YYYY):").grid(row=3, column=0, padx=10, pady=10)
tanggal_masuk_entry = tk.Entry(root, state="readonly")
tanggal_masuk_entry.grid(row=3, column=1, padx=10, pady=10)

# Entry dan tombol untuk waktu keluar
tk.Label(root, text="Waktu Keluar (HH.MM):").grid(row=4, column=0, padx=10, pady=10)
waktu_keluar_entry = tk.Entry(root)
waktu_keluar_entry.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Tanggal Keluar (DD-MM-YYYY):").grid(row=5, column=0, padx=10, pady=10)
tanggal_keluar_entry = tk.Entry(root)
tanggal_keluar_entry.grid(row=5, column=1, padx=10, pady=10)

capture_keluar_button = tk.Button(root, text="Tekan Tombol", command=capture_waktu_keluar)
capture_keluar_button.grid(row=4, column=2, padx=10, pady=10)

# Tombol untuk menghitung biaya parkir
hitung_button = tk.Button(root, text="Hitung Biaya Parkir", command=hitung_biaya_parkir)
hitung_button.grid(row=6, columnspan=3, pady=20)

root.mainloop()
