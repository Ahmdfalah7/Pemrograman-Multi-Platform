import tkinter as tk

# Fungsi untuk prediksi prodi
def hasil_prediksi():
    luaran_label.config(text="Hasil Prediksi: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Membuat label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("bold", 14))
judul_label.pack()

# Membuat 10 input nilai mata pelajaran
mata_pelajaran_label = tk.Label(root, text="Masukkan nilai mata pelajaran:")
mata_pelajaran_label.pack()

input_mata_pelajaran = []
for i in range(10):
    input_label = tk.Label(root, text=f"Mata Pelajaran")
    input_label.pack()
    input_entry = tk.Entry(root)
    input_entry.pack()
    input_mata_pelajaran.append(input_entry)

# Membuat button Hasil Prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.pack()

# Membuat label luaran hasil prediksi
luaran_label = tk.Label(root, text="")
luaran_label.pack()

# Menampilkan jendela
root.mainloop()