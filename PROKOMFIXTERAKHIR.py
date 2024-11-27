import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import math

# Variabel global untuk menyimpan data
data_parkir = {"jenis_kendaraan": None, "nomor_plat": None, "waktu_masuk": None, "waktu_keluar": None}

# Fungsi untuk menghitung biaya parkir
def hitung_biaya_parkir():
    try:
        jenis_kendaraan = data_parkir["jenis_kendaraan"]
        nomor_plat = data_parkir["nomor_plat"]
        datetime_masuk = datetime.strptime(data_parkir["waktu_masuk"], "%d-%m-%Y %H.%M")
        datetime_keluar = datetime.strptime(data_parkir["waktu_keluar"], "%d-%m-%Y %H.%M")

        # Hitung durasi parkir dalam jam
        selisih_waktu = datetime_keluar - datetime_masuk
        lama_parkir = math.ceil(selisih_waktu.total_seconds() / 3600)

        if lama_parkir < 0:
            messagebox.showerror("Error", "Waktu keluar harus lebih besar dari waktu masuk.")
            return

        # Menghitung biaya parkir
        if jenis_kendaraan == "motor":
            if lama_parkir <= 1:
                harga_parkir = 2000
            else:
                harga_parkir = 2000 + (lama_parkir - 1) * 1000
        elif jenis_kendaraan == "mobil":
            if lama_parkir <= 1:
                harga_parkir = 3000
            else:
                harga_parkir = 3000 + (lama_parkir - 1) * 2000
        else:
            messagebox.showerror("Error", "Jenis kendaraan tidak valid.")
            return

        # Menampilkan hasil dengan waktu, hari, dan nomor plat
        messagebox.showinfo(
            "Hasil",
            f"Jenis Kendaraan: {jenis_kendaraan.capitalize()}\n"
            f"Nomor Plat: {nomor_plat}\n\n"
            f"Waktu Masuk: {datetime_masuk.strftime('%H.%M')} ({datetime_masuk.strftime('%A')})\n"
            f"Tanggal Masuk: {datetime_masuk.strftime('%d-%m-%Y')}\n\n"
            f"Waktu Keluar: {datetime_keluar.strftime('%H.%M')} ({datetime_keluar.strftime('%A')})\n"
            f"Tanggal Keluar: {datetime_keluar.strftime('%d-%m-%Y')}\n\n"
            f"Lama Parkir: {lama_parkir} jam\n"
            f"Biaya Parkir: Rp{harga_parkir}"
        )
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Fungsi untuk window waktu masuk
def waktu_masuk_window():
    # Menghapus semua widget window utama
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
        # Perbarui label dengan hasil capture
        waktu_label.config(text=f"Tanggal: {tanggal_masuk}\nWaktu: {waktu_masuk}\nHari: {hari_masuk}")
        capture_button.destroy()  # Hapus tombol setelah ditekan
        lanjutkan_button.config(state="normal")

    capture_button = tk.Button(root, text="Tekan Tombol Masuk", command=capture_waktu_masuk)
    capture_button.pack(pady=10)

    lanjutkan_button = tk.Button(root, text="Kendaraan Keluar", state="disabled", command=waktu_keluar_window)
    lanjutkan_button.pack(pady=10)

# Fungsi untuk window waktu keluar
def waktu_keluar_window():
    # Menghapus semua widget window waktu masuk
    for widget in root.winfo_children():
        widget.destroy()
        
    # Entry untuk hasil capture (dapat diubah)
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

    # Entry fields untuk input manual
    tk.Label(root, text="Waktu Keluar (HH.MM)").pack(pady=5)
    waktu_keluar_entry.pack()

    tk.Label(root, text="Tanggal Keluar (DD-MM-YYYY)").pack(pady=5)
    tanggal_keluar_entry.pack()

    hari_label.pack()

    def simpan_waktu_keluar():
        waktu = waktu_keluar_entry.get()
        tanggal = tanggal_keluar_entry.get()
        try:
            datetime.strptime(f"{tanggal} {waktu}", "%d-%m-%Y %H.%M")
            data_parkir["waktu_keluar"] = f"{tanggal} {waktu}"
            hitung_biaya_parkir()
        except ValueError:
            messagebox.showerror("Error", "Format waktu atau tanggal tidak valid.")

    tk.Button(root, text="Berapa Biaya Parkirnya?", command=simpan_waktu_keluar).pack(pady=10)

# Main window untuk memilih jenis kendaraan
root = tk.Tk()
root.title("Biaya Parkir di Pusat Perbelanjaan")

tk.Label(root, text="Pilih Jenis Kendaraan").pack(pady=10)
kendaraan_var = tk.StringVar(value="motor")

tk.Radiobutton(root, text="Motor", variable=kendaraan_var, value="motor").pack(anchor="w", padx=20)
tk.Radiobutton(root, text="Mobil", variable=kendaraan_var, value="mobil").pack(anchor="w", padx=20)

# Entry untuk nomor plat kendaraan
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

root.mainloop()
