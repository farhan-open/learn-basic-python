import datetime

data_waktu = datetime.datetime.now()
print(f'Datetime now: {data_waktu}')
print(f'Tahun: {data_waktu.year}')
print(f'Hari: {data_waktu.strftime("%A")}')

'''
Penjelasan dari perintah di atas adalah sebagai berikut:

- data_waktu = datetime.datetime.now(): Baris ini menciptakan objek data_waktu yang berisi waktu saat ini sesuai dengan saat eksekusi kode. Metode now() digunakan pada kelas datetime untuk mengambil waktu saat ini dari sistem.

- print(f'Datetime now: {data_waktu}'): Baris ini mencetak waktu saat ini yang disimpan dalam variabel data_waktu. Objek datetime memiliki metode __str__() yang menghasilkan representasi string yang dapat dibaca manusia dari objek tanggal dan waktu.

- print(f'Tahun: {data_waktu.year}'): Baris ini mencetak tahun dari waktu saat ini yang disimpan dalam variabel data_waktu. Properti year pada objek datetime digunakan untuk mendapatkan nilai tahun dari waktu tersebut.

- print(f'Hari: {data_waktu.strftime("%A")}'): Baris ini mencetak nama hari dari waktu saat ini yang disimpan dalam variabel data_waktu. Metode strftime() (string format time) digunakan untuk memformat objek datetime menjadi string dengan menggunakan format tertentu. %A adalah kode format untuk mendapatkan nama hari dalam bentuk teks.
'''

from collections import Counter
'''
Perintah di atas adalah pernyataan import untuk mengimpor spesifik kelas atau fungsi Counter dari modul collections ke dalam kode Python. Dengan melakukan import Counter, kita dapat menggunakan kelas Counter tanpa menyebutkan nama modul collections setiap kali kita menggunakannya.

Modul collections adalah bagian dari library standar Python yang menyediakan koleksi data tambahan dan struktur data yang berguna. Salah satu kelas yang disediakan oleh modul ini adalah Counter.

Kelas Counter adalah sebuah alat di Python yang digunakan untuk menghitung jumlah kemunculan setiap elemen dalam sebuah iterable (seperti list, tuple, string, atau dictionary). Dengan menggunakan Counter, Anda dapat dengan mudah menghitung frekuensi kemunculan dari setiap elemen dalam kumpulan data.
'''

data = ['a', 'b', 'c', 'd', 'a', 'f', 'c', 'a', 'f', 'b']
data_count = Counter(data)

print(f'Data count = {data_count}') # akan memberikan informasi jumlah tiap item pada list yang kita punya
print(f'Jumlah a = {data_count["a"]}') # mengakses informasi jumlah elemen a pada list
print(f'Jumlah d = {data_count["d"]}') # mengakses informasi jumlah elemen d pada list

import io

file = io.open('file_text.txt', 'r')
print(file.read())

'''
PENJELASAN DARI PERINTAH DI ATAS ADALAH SEAGAI BERIKUT:

1. import io: Ini adalah pernyataan import untuk mengimpor modul io. Modul io adalah bagian dari library standar Python yang menyediakan fungsi-fungsi untuk bekerja dengan input/output (I/O) yang berorientasi byte dan berorientasi karakter.

2. file = io.open('file_text.txt', 'r'): Baris ini membuka file teks 'file_text.txt' dalam mode baca ('r') menggunakan fungsi io.open(). Fungsi open() dari modul io mirip dengan fungsi open() dari modul built-in Python (open()). Perbedaannya adalah io.open() bekerja dengan objek berorientasi karakter (teks), sedangkan open() bekerja dengan objek berorientasi byte.

3. print(file.read()): Baris ini mencetak isi file yang telah dibuka ke konsol menggunakan metode read() dari objek file. Metode read() digunakan untuk membaca seluruh konten file (teks) dalam satu kali panggilan dan mengembalikan teks yang dibaca.
'''