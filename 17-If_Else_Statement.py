# Sintaks dasar if-else statement
'''
if kondisi:
    # Blok kode yang akan dieksekusi jika kondisi benar
else:
    # Blok kode yang akan dieksekusi jika kondisi salah
'''

# contoh:
x = int(input("Silakan masukkan angka: "))

if (x > 5):
    print("Angka yang Anda masukkan lebih besar dari 5")
    print(f"Angka yang Anda masukkan adalah {x}")
else:
    print("Angka yang Anda masukkan tidak lebih besar dari 5")
    print(f"Angka yang Anda masukkan adalah {x}")
    
print("Akhir dari program")

# Catatan : python sangat sensitif dengan indentasi. Pada if-else statement, indentasi akan membentuk sebuah blok tertentu dalam program layaknya {} dalam bahasa pemrograman yang lain.
