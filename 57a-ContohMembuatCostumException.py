from numbers import Number


def tambah (angka1, angka2):
    if not isinstance(angka1, Number) or not isinstance(angka2, Number):
        raise 'Input harus berupa angka'
    return angka1 + angka2

'''
Penjelasan:
- def tambah(angka1, angka2):: Ini adalah definisi fungsi dengan nama tambah. Dua parameter angka1 dan angka2 diberikan sebagai input untuk fungsi ini.

- if not isinstance(angka1, Number) or not isinstance(angka2, Number):: Ini adalah pernyataan if yang digunakan untuk memeriksa apakah kedua parameter angka1 dan angka2 merupakan angka. Fungsi isinstance() digunakan untuk memeriksa tipe data dari objek, dalam hal ini digunakan untuk memeriksa apakah parameter adalah bilangan bulat atau bilangan desimal.

- raise 'Input harus berupa angka': Jika salah satu atau kedua parameter bukan angka (tidak integer atau float), maka fungsi akan menyebabkan error dengan melemparkan sebuah exception dengan pesan "Input harus berupa angka". Perintah raise digunakan untuk menghasilkan error (exception) yang dapat ditangkap dan ditangani di tempat lain dalam program.

- return angka1 + angka2: Jika kedua parameter adalah angka, maka fungsi akan mengembalikan hasil penambahan angka1 dan angka2.


'''

print(tambah(5, 6))
# print(tambah(5, 'K'))

# menangkap berdasarkan tipe exception
angka = 0
try:
    hasil = 10/angka
except Exception as pesan_error:
    print(pesan_error)

'''
Penjelasan:
- try:: Ini adalah blok yang digunakan untuk mencoba mengeksekusi kode yang mungkin menyebabkan runtime error. Kode di dalam blok try akan dievaluasi, dan jika terjadi runtime error, program akan beralih ke blok except.

- hasil = 10/angka: Kode ini mencoba untuk melakukan pembagian 10 dengan angka. Jika angka adalah 0 atau tidak dapat dikonversi menjadi bilangan (misalnya, input berupa string bukan angka), maka akan terjadi runtime error.

- except Exception as pesan_error:: Ini adalah blok yang akan dieksekusi jika terjadi runtime error dalam blok try. Exception adalah tipe dasar untuk menangani berbagai jenis exception atau runtime error. Jika terjadi error, pesan error akan ditangkap dan disimpan dalam variabel pesan_error.

- print(pesan_error): Kode ini akan mencetak pesan error yang ditangkap oleh blok except. Pesan error akan berisi informasi tentang jenis error dan detail lainnya yang membantu Anda dalam menemukan dan memperbaiki masalah dalam kode.
'''