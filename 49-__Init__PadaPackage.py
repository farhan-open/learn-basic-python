#  Pada sebuah program yang menggunakan package dan di dalam package tersebut terdapat file __init__.py, maka file tersebutlah yang akan dijalankan pertama kali
import sains # contoh melakukan import pada package yang memiliki floder di dalamnya

hasil_tambah = sains.matematika.basic.tambah(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # implementasi pemanggilan fungsi dari baris ke-1 dan ke-2 pada file __init__.py pada folder matematika
print(f'Hasil penjumlahan dari import package = {hasil_tambah}') # implementasi pemanggilan fungsi dari baris ke-1 dan ke-2 pada file __init__.py pada folder matematika

gaya = sains.fisika.gaya(90, 10) # implementasi pemanggilan fungsi dari baris ke-2 pada file __init__.py pada folder sains
print(f'Besar gaya adalah {gaya}')

hasil_kali = sains.matematika.basic.kali(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'Hasil penjumlahan dari import package = {hasil_kali}') 

pangkat_3 = sains.matematika.pangkat(3) # implementasi pemanggilan fungsi dari baris ke-5 dan ke-6 pada file __init__.py pada folder matematika
print(f'Hasil pemangkatan dari import package = {pangkat_3(2)}') 