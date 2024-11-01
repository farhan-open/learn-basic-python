# GUI (Graphical User Interface)

import tkinter as tk
'''
Tkinter adalah modul dalam library standar Python yang digunakan untuk membuat antarmuka grafis (GUI - Graphical User Interface) untuk aplikasi desktop. Dengan menggunakan Tkinter, Anda dapat membuat jendela, tombol, label, kotak teks, menu, dan berbagai elemen GUI lainnya untuk berinteraksi dengan pengguna. Tkinter memberikan antarmuka yang sederhana dan mudah digunakan, membuatnya menjadi pilihan yang populer untuk pengembangan aplikasi desktop Python yang sederhana dan ringan.
'''

from tkinter import ttk
'''
Pada Tkinter, ttk merupakan singkatan dari "Themed Tkinter". ttk adalah modul yang terdapat di dalam library standar Python dan merupakan bagian dari Tkinter. Modul ttk menyediakan widget Tkinter dengan tampilan yang lebih modern dan lebih baik secara estetika daripada widget Tkinter standar.

Widget adalah elemen-elemen GUI seperti tombol, kotak teks, label, kotak centang, dan lain-lain. Dalam Tkinter, Anda dapat membuat widget menggunakan kelas-kelas seperti Button, Label, Entry, dan lain-lain. Namun, modul ttk memperkenalkan widget dengan tampilan yang lebih baik dan mengikuti tema tampilan sistem operasi yang sedang digunakan oleh pengguna.

Dengan ttk, Anda dapat membuat aplikasi yang lebih modern dan lebih konsisten dengan tampilan sistem operasi yang sedang digunakan oleh pengguna. Sebagai contoh, widget tombol dengan ttk akan memiliki tampilan yang lebih ramping dan lebih halus daripada widget tombol standar Tkinter.
'''

from tkinter.messagebox import showinfo

# Init
window = tk.Tk() # Baris ini menciptakan instance dari kelas Tk yang merupakan kelas utama dalam Tkinter. Setiap aplikasi Tkinter memerlukan jendela utama (main window) yang dibuat dengan instance kelas Tk.

window.configure(bg = 'lightblue') # merubah warna background dari window menjadi lightblue
window.geometry('800x500') # mengatur ukuran default dari window
window.resizable(width=False, height=False) # membuat lebar dan tinggi dari window tidak dapat diubah
window.title("Haloo") # menambahkan judul pada window

# Variabel dan fungsi 
nama_depan = tk.StringVar()
nama_belakang = tk.StringVar()

def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f'Halo {nama_depan.get()} {nama_belakang.get()}'
    showinfo(title='Hai', message=pesan)

#frame
input_frame = ttk.Frame(window)
# penempatan (grid, pack, place)
input_frame.pack(padx=10, pady=10, fill='x', expand=True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text='Nama Depan')
nama_depan_label.pack(padx=10, fill='x', expand=True)

# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=nama_depan)
nama_depan_entry.pack(padx=10, fill='x', expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text='Nama Belakang')
nama_belakang_label.pack(padx=10, fill='x', expand=True)

# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=nama_belakang)
nama_belakang_entry.pack(padx=10, fill='x', expand=True)

# 5. Tombol
tombol_sapa = ttk.Button(input_frame, text='Sapa!', command=tombol_click)
tombol_sapa.pack(padx=10, pady=10, fill='x', expand=True)

# Main loop window
window.mainloop()
'''
Metode mainloop() adalah metode utama dalam Tkinter yang digunakan untuk memulai loop peristiwa utama (event loop) untuk aplikasi GUI. Ketika metode ini dipanggil, Tkinter akan memantau dan menangani berbagai peristiwa, seperti klik tombol, input keyboard, perubahan ukuran jendela, dan peristiwa GUI lainnya.

Jika Anda tidak memanggil mainloop(), jendela aplikasi akan ditampilkan sebentar dan segera ditutup karena program akan berakhir secara otomatis. Namun, dengan memanggil mainloop(), aplikasi akan tetap berjalan dan berinteraksi dengan pengguna hingga jendela ditutup.

Penting untuk menyebutkan bahwa setelah mainloop() dijalankan, baris kode selanjutnya setelah perintah tersebut tidak akan dieksekusi hingga jendela ditutup. Hal ini karena program akan terus berada dalam loop peristiwa utama, dan kode di bawah mainloop() hanya akan dieksekusi setelah aplikasi ditutup.
'''