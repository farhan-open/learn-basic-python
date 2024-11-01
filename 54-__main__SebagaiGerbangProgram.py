# __main__ adalah top level code environment

# __name__ == '__main__' akan terjadi jika ada di program utama

# __name__ pada file program utama
print(f'Nilai __name__ pada file ini = "{__name__}"')

# __name__ pada file program eksternal
import Gerbang

# CONTOH PENGGUNAAN
def fungsi_tambah(a: int, b: int) -> int:
    return a + b

# fungsi utama
if __name__ == '__main__':
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1, angka2)
    print(f'Hasil tambah = {hasil}')

import package