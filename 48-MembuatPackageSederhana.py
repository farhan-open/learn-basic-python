# Secara sederhana, package dapat dianalogikan sebagai folder

import sains.math # meng-import file math.py dari folder sains (ssemua fungsi yang dibuat pada file math.py telah termuat)
# proses import juga dapat dilakukan sebagai berikut:
from sains import fisika as f

# cara mengakses fungsi yang telah di-import adalah sebagai berikut:
hasil_tambah = sains.math.tambah(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'Hasil penjumlahan dari improt package = {hasil_tambah}')

gaya = f.gaya(90, 10)
print(f'Besar gaya adalah {gaya}')