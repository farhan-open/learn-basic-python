import os

# program menghitung luas dan keliling persegi panjang

def header():
    os.system('cls') # untuk clearscreen

    print('='*65)
    print('Program Menghitung Luas dan Keliling Persegi Panjang'.center(65))
    print('='*65)

def input_user():
    panjang = int(input('Masukkan nilai panjang persegi panjang: '))
    lebar = int(input('Masukkan nilai lebar persegi panjang: '))

    return panjang, lebar

def luas(panjang, lebar):
    hasil = panjang * lebar
    return hasil

def keliling(panjang, lebar):
    hasil = 2 * panjang + 2 * lebar
    return hasil

def display(pesan, nilai):
    print(f'{pesan} {nilai}')

# program utama
while True:
    header()
    p, l = input_user()
    print('')
    print('Silakan pilih kalkulasi yang diinginkan:')
    print('1. Luas persegi panjang')
    print('2. Keliling persegi panjang')
    print(':'*65)
    opsi = int(input('Masukkan pilihan Anda: '))

    if (opsi == 1):
        hasil = luas(p, l)
        display('Luas persegi panjang =', hasil)
    elif (opsi == 2):
        keliling(p, l)
        hasil = keliling(p,l)
        display('Keliling persegi panjang =', hasil)
    else:
        print('Anda salah memasukkan input, program dihentikan..')
        break

    print('')
    isLanjut = input('Apakah Anda ingin melakukan kalkulasi ulang? (Y/N): ')

    if (isLanjut == 'Y' or isLanjut == 'y'):
        pass
    elif (isLanjut == 'N' or isLanjut =='n'):
        break
    else:
        print('Anda salah memasukkan input, program dihentikan..')
        break

