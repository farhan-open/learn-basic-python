# Import berfungsi untuk mengambil program dari file eksternal .py

# 1. Menyambung program dari file .py eksternal
import Cetak # perintah-perintah yang ada pada file Cetak.py akan dimasukkan ke dalam program ini dan dapat dijalankan

# 2. Meng-import variabel atau data dari file .py eksternal
import Variabel # Dengan begini, semua variabel yang ada pada file Variabel.py telah termuat

# untuk mengakses variabel tersebut, dapat dilakukan sebagai berikut:
print(Variabel.kalimat)

# 3. Meng-import fungsi dari file .py eksternal
import Fungsi # Dengan begini, semua fungsi yang ada pada Fungsi.py telah termuat

# untuk mengakses fungsi tersebut, dapat dilakukan sebagai berikut:
hasil = Fungsi.tambah(4, 5)
print(hasil)