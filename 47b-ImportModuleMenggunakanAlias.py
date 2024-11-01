import matematika as math # Dengan begini, semua fungsi pada file matematika.py telah termuat dan untuk mengaksesnya, alih-aling menggunakan 'matematika', kita bisa menggunakan alias yang dalam hal ini adalah 'math'

from matematika import kali as k # Dengan begini, kita bisa menggunakan fungsi kali dari file matematika.py dengan menggunakan nama yang lebiematika singkat, dalam hal ini adalah k
from matematika import pangkat as p # Dengan begini, kita bisa menggunakan fungsi pangkat dari file matematika.py dengan menggunakan nama yang lebih singkat, dalam hal ini adalah p

hasil_tambah = math.tambah(1, 2, 3, 4, 5)
print(f'Hasil tambah = {hasil_tambah}')

hasil_kali = k(1, 2, 3, 4, 5)
print(f'Hasil kali = {hasil_kali}')

pangkat_3 = p(3)
print(f'Hasil pangkat 3 = {pangkat_3(2)}') # berarti 2 pangkat 3 (berdasarkan fungsi pangkat yang telah kita buat pada file matematika.py)