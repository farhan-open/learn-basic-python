'''
Fungsi dengan default argumen adalah fungsi di Python yang memungkinkan Anda menentukan nilai default untuk beberapa atau semua parameter fungsi. Jika argumen tidak diberikan saat pemanggilan fungsi, nilai default akan digunakan sebagai argumen. Namun, jika kita mengatur argumen atau memberikan argumen ketika melakukan pemanggilan fungsi, maka argumen yang diatur tersebutlah yang akan digunakan dan argumen default akan diabaikan.

SINTAKS DASAR:
def nama_fungsi(parameter1 = default_value1, parameter2 = default_value2, ...):
    # Blok kode fungsi
    # Pernyataan 1
    # Pernyataan 2
    # ...
    return nilai_kembali

'''

# contoh
def sapa(name="Otong", greeting="Halo"):
    print(f"{greeting}, {name}!")

sapa()  # Output: "Halo, Otong!"
sapa("Abangda")  # Output: "Halo, Mahmud!"
sapa("Eros", "Oi")  # Output: "Oi, Eros!"

# kita juga bisa mengakses tiap parameter dalam fungsi berdasarkan namanya
sapa(greeting = 'Assalamu\'alaikum',  name = 'Ukhti')
sapa(greeting = 'Assalamu\'alaikum') # hanya mengatur parameter greeting, sehingga untuk parameter name, tetap nilai default yang akan digunakan
