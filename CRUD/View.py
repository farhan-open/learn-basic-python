from . import Operasi

def read_console():
    data_file = Operasi.read()
    index = 'No'
    judul = 'Judul'
    penulis = 'Penulis'
    tahun = 'Tahun'

    # header
    print('')
    print('='*100)
    print(f'{index:4} | {judul:40} | {penulis:40} | {tahun:5}')
    print('='*100)

    # data
    for index, data in enumerate(data_file):
        data_break = data.split(',')
        pk = data_break[0]
        date_add = data_break[1] 
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f'{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}', end='')
    
    # footer
    print('='*100)

def create_console():
    print('')
    print('='*100)
    print('Silakan Tambah Data Buku'.center(100))
    print('='*100)

    penulis = input('Penulis: ')
    judul = input('Judul: ')
    while (True):
        try:
            tahun = int(input('Tahun: '))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus berupa angka, silakan masukkan ulang..")
        except:
            print("Tahun harus berupa angka, silakan masukkan ulang..")
    
    Operasi.create(tahun, judul, penulis)
    print('\nBerikut adalah data buku terbaru')
    read_console()

def update_console():
    print('Berikut ini adalah data buku pada database')
    read_console()
    while (True):
        no_buku = int(input('Nomor buku yang akan di-update: '))
        data_buku = Operasi.read(index=no_buku)

        if(data_buku):
            break
        else:
            print('Nomor buku tidak valid, silakan masukkan lagi..')

    data_break = data_buku.split(',') # dengan melakukan split di samping, setiap komponen string yang dipisahkan oleh tanda ',' akan dijadikan sebagai sebuah list
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while(True):
        # data yang ingin di-update
        print('='*100)
        print('Silakan pilih data yang ingin diubah'.center(100))
        print('='*100)
        print(f'1. Judul: {judul:.40}')
        print(f'2. Penulis: {penulis:.40}')
        print(f'3. Tahun: {tahun:4}')

        # memilih item yang ingin di-update
        user_option = input('Masukkan pilihan Anda: ')
        print('='*100)

        match user_option:
            case '1': judul = input('Masukkan judul yang baru: ')
            case '2': penulis = input('Masukkan nama penulis yang baru: ')
            case '3':
                while (True):
                    try:
                        tahun = int(input('Masukkan tahun yang baru: '))
                        if (len(str(tahun)) == 4):
                            break
                        else:
                            print("Tahun harus berupa angka dengan 4 digit, silakan masukkan ulang..")
                    except:
                        print("Tahun harus berupa angka dengan 4 digit, silakan masukkan ulang..")
            case _: print('Index yang Anda masukkan tidak cocok..') # default case, akan dijalankan jika tidak ada kondisi pada case sebelumnya yang cocok dengan nilai yang diberikan

        print('Data baru Anda adalah sebagai berikut:')
        print(f'1. Judul: {judul:.40}')
        print(f'2. Penulis: {penulis:.40}')
        print(f'3. Tahun: {tahun}')

        is_done = input('Apakah Anda ingin mengakhiri proses update? (Y/N): ')

        if (is_done == 'Y' or is_done == 'y'):
            print('Data berhasil di-update, silakan pilih menu "Read Data" untuk melihat data terbaru..')
            break
        elif (is_done == 'N' or is_done == 'n'):
            pass
        else:
            print('Anda salah memasukkan input, proses update dihentikan..')
            break
    
    Operasi.update(no_buku, pk, data_add, tahun, judul, penulis)

def delete_console():
    read_console()
    while (True):
        print('')
        no_buku = int(input('Silakan pilih nomor buku yang akan dihapus: '))
        data_buku = Operasi.read(index=no_buku)

        if(data_buku):
            data_break = data_buku.split(',') # dengan melakukan split di samping, setiap komponen string yang dipisahkan oleh tanda ',' akan dijadikan sebagai sebuah list
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            # data yang ingin di-update
            print('='*100)
            print('Data yang akan dihapus adalah sebagai berikut'.center(100))
            print('='*100)
            print(f'1. Judul: {judul:.40}')
            print(f'2. Penulis: {penulis:.40}')
            print(f'3. Tahun: {tahun:4}')

            is_done = input('Apakah Anda yakin ingin menghapus? (Y/N): ')

            if (is_done == 'Y' or is_done == 'y'):
                Operasi.delete(no_buku)
                print('Data berhasil dihapus, silakan pilih menu "Read Data" untuk melihat data terbaru..')
                break
            elif (is_done == 'N' or is_done == 'n'):
                pass
            else:
                print('Anda salah memasukkan input, proses update dihentikan..')
                break
        else:
            print('Nomor buku tidak valid, silakan masukkan lagi..')
        
'''
Penjelasan baris 68:
- data_break: Ini adalah list yang berisi data buku yang telah dipecah dari sebuah baris teks yang dibaca dari file. Setiap komponen data buku dipisahkan oleh tanda koma (,), sehingga masing-masing komponen tersebut menjadi elemen dalam list.

- data_break[4]: Ini adalah elemen keempat dalam list data_break, yang merepresentasikan nilai tahun dari data buku.

- [:-1]: Ini adalah proses slicing (potongan) dari string yang diambil dari data_break[4]. Potongan ini mengambil semua karakter dari awal string hingga karakter sebelum karakter terakhir. Tujuannya adalah untuk menghapus karakter newline (\n) yang mungkin ada di akhir string tersebut.
'''
    
    