'''
Pernyataan elif (else if) digunakan ketika ada beberapa kondisi yang perlu dievaluasi secara berurutan, dan blok kode yang sesuai akan dieksekusi pada kondisi yang pertama kali terpenuhi.

SINTAKS DASAR:
if kondisi1:
    # Blok kode yang akan dieksekusi jika kondisi1 benar
elif kondisi2:
    # Blok kode yang akan dieksekusi jika kondisi1 salah dan kondisi2 benar
elif kondisi3:
    # Blok kode yang akan dieksekusi jika kondisi1 dan kondisi2 salah, dan kondisi3 benar
else:
    # Blok kode yang akan dieksekusi jika semua kondisi di atas salah
'''

x = int(input("Silakan masukkan sebuah angka: "))

if (x > 15):
    print("Angka yang Anda masukkan lebih besar dari 15")
    print(f"Angka yang Anda masukkan adalah {x}")
elif (x > 10):
    print("Angka yang Anda masukkan berada di dalam range 11 - 15")
    print(f"Angka yang Anda masukkan adalah {x}")
elif (x > 5):
    print("Angka yang Anda masukkan berada di dalam range 6 - 10")
    print(f"Angka yang Anda masukkan adalah {x}")
else:
    print("Angka yang Anda masukkan tidak lebih besar dari 5")
    print(f"Angka yang Anda masukkan adalah {x}")
    
print("Akhir dari program")
