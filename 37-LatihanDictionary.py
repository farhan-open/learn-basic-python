import datetime
import os
import string
import random

mahasiswa_template = {
    "nama": "Farhan",
    "nim": "222112195",
    "sks_lulus": 144,
    "beasiswa": True,
    "lahir": datetime.datetime(2002, 8, 10)
}

data_mahasiswa = {} #dictionary kosong

while True:
    os.system('cls')
    mahasiswa = dict.fromkeys(mahasiswa_template.keys()) # membuat dictionary dengan nama 'mahasiswa' yang key-nya diambil dari 'mahasiswa_template'
    mahasiswa['nama'] = input('Nama mahasiswa: ')
    mahasiswa['nim'] = input('NIM: ')
    mahasiswa['sks_lulus'] = int(input('SKS: '))
    tahun_lahir = int(input('Tahun lahir: '))
    bulan_lahir = int(input('Bulan lahir: '))
    tanggal_lahir = int(input('Tanggal lahir: '))
    mahasiswa['lahir'] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)

    random_key = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_mahasiswa.update({random_key: mahasiswa})

    print('='*67)
    print('Key'.center(7) + '|' + 'Nama'.center(20) + '|' + 'NIM'.center(11) + '|' + 'SKS'.center(3) + '|' + 'Lahir'.center(11) + '|')
    print('='*67)

    for data in data_mahasiswa:
        key = data
        nama = data_mahasiswa[key]['nama']
        nim = data_mahasiswa[key]['nim']
        sks = data_mahasiswa[key]['sks_lulus']
        # beasiswa = data_mahasiswa[key]['beasiswa']
        lahir = data_mahasiswa[key]['lahir'].strftime("%x")
        print(key.center(7) + '|' + nama.center(20) + '|' + nim.center(11) + '|' + str(sks).center(3) + '|' + f'{lahir:^11}' + '|')
        print('-'*67)

    print('')
    is_done = input('Apakah Anda ingin mengisi data mahasiswa lagi? (Y/N): ')

    if (is_done == 'Y' or is_done == 'y'):
        pass
    elif (is_done == 'N' or is_done == 'n'):
        break
    else:
        print('Anda salah memasukkan input, program dihentikan..')
        break