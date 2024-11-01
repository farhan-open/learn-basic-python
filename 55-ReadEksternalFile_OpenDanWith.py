'''
Mekanisme read eksternal file menggunakan open() dan with pada Python memungkinkan Anda membaca isi dari sebuah file eksternal dan melakukan operasi dengan aman, termasuk menutup file secara otomatis setelah operasi selesai. Ini adalah cara yang direkomendasikan untuk membaca file di Python karena memastikan file ditutup dengan benar setelah digunakan, sehingga menghindari masalah dengan resource handling.
'''

# 1. open() Function:
'''
- open() adalah fungsi bawaan Python yang digunakan untuk membuka file eksternal.
- Fungsi ini membutuhkan dua argumen utama: nama file (string) dan mode file (string) yang mengindikasikan tujuan operasi pada file tersebut (misalnya, membaca, menulis, menambahkan, dll.).
- Mode file dapat berupa 'r' (read), 'w' (write), 'a' (append), 'x' (create), dan kombinasi lainnya seperti 'rb', 'wb', dan sebagainya.
'''
print('Membaca File TXT'.center(35, '='))
file = open('file_text.txt', mode='r')
print(file.read()) # menampilkan/membaca semua isi file eksternal secara keseluruhan

# mendapatkan informasi spesifik file eksternal
print(f'Status read: {file.readable()}') # apakah bisa dibaca
print(f'Status write: {file.writable()}') # apakah bisa di-write

# metode lain dalam membaca/menampilkan isi file eksternal
# print(file.readline()) # menampilkan/membaca semua isi file eksternal pada baris pertama 
# print(file.readline()) # menampilkan/membaca semua isi file eksternal pada baris kedua 

# membaca semua baris pada file eksternal SEBAGAI LIST
# print(file.readlines())

# MENUTUP FILE EKSTERNAL SETELAH DIGUNAKAN
print(f'Apakah file sudah di-close: {file.closed}')
file.close()
print(f'Apakah file sudah di-close: {file.closed}')

# 2. with Statement:
'''
- with adalah statement dalam Python yang digunakan untuk mengelola konteks eksekusi. Ini bekerja dengan objek yang memiliki metode __enter__() dan __exit__().
- Ketika digunakan dengan open(), with digunakan untuk membuka file dalam konteks yang aman dan memastikan bahwa file ditutup secara otomatis setelah keluar dari blok with.
- Keuntungan menggunakan with statement:
    1. Memastikan bahwa file ditutup dengan benar setelah operasi selesai, bahkan jika terjadi kesalahan dalam eksekusi.
    2. Menghindari potensi memory leaks dan resource leaks karena file akan ditutup otomatis bahkan jika ada kesalahan.
'''

with open('file_text.txt', mode='r') as file:
    content = file.readline()
    print(content)

# CATATAN: File akan ditutup secara otomatis ketika program telah keluar dari blok 'with'
print(f'Apakah file sudah di-close: {file.closed}')