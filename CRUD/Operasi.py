import os
import time
from . Util import random_string
from . import Database

def create_first_data():
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

    data = Database.TEMPLATE.copy()
    
    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%Sz', time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = tahun

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    try:
        with open(Database.DB_NAME, mode='w', encoding='utf-8') as file:
            print('Data buku berhasil ditambahkan')
            file.write(data_str)
    except:
        print('Data buku gagal dimasukkan..')

'''
Penjelasan baris 14-15
- data['penulis'] adalah kunci (penulis) di dalam dictionary data yang akan diisi dengan nilai baru.

- penulis adalah variabel yang berisi data penulis yang ingin ditambahkan ke data.

- Database.TEMPLATE['penulis'] adalah kunci (penulis) di dalam dictionary Database.TEMPLATE yang berisi template data untuk penulis.

- [len(penulis):] adalah potongan (slice) dari template data Database.TEMPLATE['penulis'] yang dimulai dari panjang data penulis penulis hingga akhir data. Ini dilakukan untuk mengisi sisa bagian data yang belum diisi dari template.
'''

def read(**kwargs):
    try:
        with open(Database.DB_NAME, mode='r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if ('index' in kwargs):
                index_buku = kwargs['index']-1

                if (index_buku < 0 or index_buku > jumlah_buku):
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print('Error dalam membaca database')
        return False
    
def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()
    
    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%Sz', time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    try:
        with open(Database.DB_NAME, mode='a', encoding='utf-8') as file:
            file.write(data_str)
            print('Data buku berhasil ditambahkan..')
    except:
        print('Data gagal ditambahkan..')

def update(no_buku, pk, data_add, tahun, judul, penulis):
    data = Database.TEMPLATE.copy()
    
    data['pk'] = pk
    data['date_add'] = data_add
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"

    panjang_data = len(data_str)
    
    # Menghapus karakter '\n' dari data_str
    data_str = data_str.strip()

    try:
        with open(Database.DB_NAME, mode='r+', encoding='utf-8') as file:
            file.seek((panjang_data + 1) * (no_buku-1))
            file.write(data_str)
    except:
        print('Error dalam melakukan update data..')

def delete(no_buku):
    try:
        with open(Database.DB_NAME, mode='r') as file:
            counter = 0
            while(True):
                content = file.readline()
                if (len(content) == 0):
                    break
                elif (counter == no_buku-1):
                    pass
                else:
                    with open('data_temp.txt', mode='a', encoding='utf-8') as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print('Database error')

    # hapus file project.txt
    try:
        os.remove(Database.DB_NAME)
    except:
        print('Terjadi error dalam menghapus file basis')

    # Ganti nama file data_temp.txt menjadi project.txt
    try:   
        os.rename('data_temp.txt', Database.DB_NAME)
    except:
        print('Terjadi error dalam proses pembuatan file turunan')
'''
Penjelasan baris 85-86:
- penulis: Ini adalah variabel yang berisi data penulis yang ingin ditambahkan ke data.

- Database.TEMPLATE['penulis']: Ini adalah nilai dari kunci 'penulis' dalam dictionary Database.TEMPLATE. Nilai ini adalah string kosong yang memiliki panjang 255 karakter (dapat dilihat di Database.py).

- [len(penulis):]: Ini adalah proses slice (potongan) dari string Database.TEMPLATE['penulis']. Potongan ini dimulai dari panjang data penulis hingga akhir data.

Jadi, perintah ini bertujuan untuk mengisi data penulis pada data dengan nilai penulis yang baru, dan jika panjang data penulis lebih pendek dari 255 karakter (panjang data dalam template), maka bagian sisanya akan diisi dengan string kosong dari template.
'''