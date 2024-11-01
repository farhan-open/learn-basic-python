'''
Runtime error dalam Python, juga dikenal sebagai exception, adalah suatu kondisi yang terjadi saat program dijalankan dan mengalami masalah atau kesalahan saat mengeksekusi kode. Saat runtime error terjadi, program tidak dapat melanjutkan eksekusi seperti yang diharapkan karena ada sesuatu yang tidak berjalan dengan baik.
'''

'''
SyntaxError: Terjadi ketika ada kesalahan dalam sintaksis kode, seperti tanda kurung yang tidak seimbang atau kesalahan penulisan.
'''

# Exception akan terjadi saat terdapat runtime error

# Contoh menangkap exception
# input_user =int(input('Masukkan angka: '))
# hasil = 0
# try:
#     hasil = 10/input_user
# except:
#     print('Input tidak boleh 0')

# print(f'Hasil = {hasil}')

# contoh pada aplikasi
while(True):
    angka = int(input('Masukkan angka pembagi: '))
    try:
        hasil = 10/angka
        print(f'Hasil = {hasil}')
        is_done = input('Lanjutkan (Y/N): ')
        if (is_done == 'Y' or is_done == 'y'):
            pass
        elif (is_done == 'N' or is_done == 'n'):
            break
        else:
            print('Anda salah memasukkan input, program dihentikan..')
            break
    except:
        print('Pembagi tidak boleh bernilai 0, silakan masukkan angka lain..')

print('Akhir dari program 1')

# contoh lain pada aplikasi 
while(True):
    try:
        with open('data.txt', mode='r') as file:
            print(file.read())
        break
    except:
        print('File tidak ditemukan, membuat file baru..')
        with open('data.txt', mode='w', encoding='utf-8') as file:
            file.write('Ini adalah isi dari file yang baru dibuat..')
        break

print('Akhir dari program 2')
