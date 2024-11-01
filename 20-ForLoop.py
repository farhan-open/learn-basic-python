'''
Sintaks Dasar:
for elemen in urutan:
    # Blok kode yang akan diulang

Elemen:
    Variabel elemen merupakan variabel yang digunakan untuk menyimpan nilai elemen saat ini pada setiap iterasi.
    Pada setiap iterasi, variabel elemen akan diberi nilai dari urutan yang diiterasi.

Urutan:
    Urutan dapat berupa objek iterabel seperti list, tuple, set, string, atau objek lain yang dapat diiterasi.
    For loop akan mengambil elemen-elemen dari urutan satu per satu dalam urutan yang telah ditentukan.

Blok kode yang diulang:
    Blok kode yang diulang adalah blok kode yang terkait dengan for loop, dan akan dijalankan untuk setiap elemen dalam urutan.
    Blok kode tersebut biasanya diberi indentasi dengan empat spasi atau satu tab.
'''

# contoh:
fruits = ["apple", "banana", "cherry"]

for f in fruits:
    print(f)

# contoh lain:
print('')
angka = [0, 1, 2, 3, 4]

for i in angka:
    print(f'Nilai i sekarang adalah {i}')

# contoh dengan range
print('')
angka_range = range(5) # range(5) akan berisi (0, 1, 2, 3, 4)

for j in angka_range:
    print(f'Nilai j sekarang adalah {j}')

print('')
angka_range2 = range(1, 10) # range(1, 10) berarti kita punya range 0-9 tapi penghitungannya dimulai dari 1 sehingga, isinya adalah (1, 2, 3, 4, 5, 6, 7, 8, 9)

for k in angka_range2:
    print(f'Farhan belajar python')

# contoh dengan string
data_str = 'Belajar Python'

for huruf in data_str:
    print(huruf)
