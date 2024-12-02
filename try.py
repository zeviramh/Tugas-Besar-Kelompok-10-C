import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import math

# Variabel global untuk menyimpan data
data_parkir = {"jenis_kendaraan": None, "nomor_plat": None, "waktu_masuk": None, "waktu_keluar": None}

# Fungsi untuk menghitung biaya parkir
def hitung_biaya_parkir():
    try:
        # Ambil data dari variabel global
        jenis_kendaraan = data_parkir["jenis_kendaraan"]
        nomor_plat = data_parkir["nomor_plat"]
        datetime_masuk = datetime.strptime(data_parkir["waktu_masuk"], "%d-%m-%Y %H.%M")
        datetime_keluar = datetime.strptime(data_parkir["waktu_keluar"], "%d-%m-%Y %H.%M")

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

        # Tampilkan hasil
        messagebox.showinfo(
            "Hasil",
            f"Jenis Kendaraan: {jenis_kendaraan.capitalize()}\n"
            f"Nomor Plat: {nomor_plat}\n"
            f"Waktu Masuk: {datetime_masuk.strftime('%H.%M')} ({datetime_masuk.strftime('%A')})\n"
            f"Tanggal Masuk: {datetime_masuk.strftime('%d-%m-%Y')}\n\n"
            f"Waktu Keluar: {datetime_keluar.strftime('%H.%M')} ({datetime_keluar.strftime('%A')})\n"
            f"Tanggal Keluar: {datetime_keluar.strftime('%d-%m-%Y')}\n\n"
            f"Lama Parkir: {lama_parkir} jam\n"
            f"Biaya Parkir: Rp{harga_parkir}"
        )
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Fungsi untuk menangani waktu masuk
def waktu_masuk_window():
    # Bersihkan jendela utama
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Waktu Masuk").pack(pady=10)
    waktu_label = tk.Label(root, text="")
    waktu_label.pack()

    def capture_waktu_masuk():
        now = datetime.now()
        waktu_masuk = now.strftime("%H.%M")
        tanggal_masuk = now.strftime("%d-%m-%Y")
        hari_masuk = now.strftime("%A")
        data_parkir["waktu_masuk"] = f"{tanggal_masuk} {waktu_masuk}"
        waktu_label.config(text=f"Tanggal: {tanggal_masuk}\nWaktu: {waktu_masuk}\nHari: {hari_masuk}")
        capture_button.destroy()
        lanjutkan_button.config(state="normal")

    capture_button = tk.Button(root, text="Capture Waktu Masuk", command=capture_waktu_masuk)
    capture_button.pack(pady=10)

    lanjutkan_button = tk.Button(root, text="Lanjut ke Waktu Keluar", state="disabled", command=waktu_keluar_window)
    lanjutkan_button.pack(pady=10)

# Fungsi untuk menangani waktu keluar
def waktu_keluar_window():
    # Bersihkan jendela utama
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Waktu Keluar").pack(pady=10)

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

    capture_button = tk.Button(root, text="Capture Waktu Keluar", command=capture_waktu_keluar)
    capture_button.pack(pady=10)

    tk.Label(root, text="Waktu Keluar (HH.MM)").pack()
    waktu_keluar_entry.pack()

    tk.Label(root, text="Tanggal Keluar (DD-MM-YYYY)").pack()
    tanggal_keluar_entry.pack()

    hari_label.pack()

    def simpan_waktu_keluar():
        waktu = waktu_keluar_entry.get()
        tanggal = tanggal_keluar_entry.get()
        try:
            datetime_keluar = datetime.strptime(f"{tanggal} {waktu}", "%d-%m-%Y %H.%M")
            datetime_masuk = datetime.strptime(data_parkir["waktu_masuk"], "%d-%m-%Y %H.%M")

            if datetime_keluar <= datetime_masuk:
                messagebox.showerror("Error", "Waktu keluar harus lebih besar dari waktu masuk.")
                return

            data_parkir["waktu_keluar"] = f"{tanggal} {waktu}"
            hitung_biaya_parkir()
        except ValueError:
            messagebox.showerror("Error", "Format waktu atau tanggal tidak valid.")

    tk.Button(root, text="Hitung Biaya Parkir", command=simpan_waktu_keluar).pack(pady=10)

# Fungsi utama untuk memilih jenis kendaraan
def pilih_kendaraan():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Pilih Jenis Kendaraan").pack(pady=10)
    kendaraan_var = tk.StringVar(value="motor")

    tk.Radiobutton(root, text="Motor", variable=kendaraan_var, value="motor").pack(anchor="w", padx=20)
    tk.Radiobutton(root, text="Mobil", variable=kendaraan_var, value="mobil").pack(anchor="w", padx=20)

    tk.Label(root, text="Nomor Plat Kendaraan").pack(pady=10)
    nomor_plat_entry = tk.Entry(root)
    nomor_plat_entry.pack()

    def simpan_jenis_kendaraan():
        data_parkir["jenis_kendaraan"] = kendaraan_var.get()
        data_parkir["nomor_plat"] = nomor_plat_entry.get().strip()
        if not data_parkir["nomor_plat"]:
            messagebox.showerror("Error", "Nomor plat kendaraan harus diisi.")
            return
        waktu_masuk_window()

    tk.Button(root, text="Lanjutkan", command=simpan_jenis_kendaraan).pack(pady=10)

# Main window
root = tk.Tk()
root.title("Sistem Parkir")
pilih_kendaraan()
root.mainloop()

