'''
Di Python, sebuah file kode Python disebut "module". Modul adalah cara untuk mengorganisasi kode Python dengan membaginya ke dalam file-file yang terpisah. Setiap modul dapat berisi definisi fungsi, variabel, dan kelas yang dapat diimpor dan digunakan dalam kode lain. Dengan menggunakan modul, Anda dapat mengatur dan mengelompokkan kode secara logis, membuat kode lebih mudah dipelihara, dan memungkinkan untuk penggunaan kembali kode di berbagai proyek.
'''

import matematika # Dengan begini, semua fungsi pada file matematika.py telah termuat

hasil_tambah = matematika.tambah(1, 2, 3, 4, 5)
print(f'Hasil tambah = {hasil_tambah}')

hasil_kali = matematika.kali(1, 2, 3, 4, 5)
print(f'Hasil kali = {hasil_kali}')

pangkat_3 = matematika.pangkat(3)
print(f'Hasil pangkat 3 = {pangkat_3(2)}') # berarti 2 pangkat 3 (berdasarkan fungsi pangkat yang telah kita buat pada file matematika.py)