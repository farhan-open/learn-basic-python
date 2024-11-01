import datetime

mahasiswa1 = {
    "nama": "Farhan",
    "nim": "222112195",
    "sks_lulus": 144,
    "beasiswa": True,
    "lahir": datetime.datetime(2002, 8, 10)
}

print(mahasiswa1)

mahasiswa2 = {
    "nama": "Otong",
    "nim": "222112190",
    "sks_lulus": 130,
    "beasiswa": False,
    "lahir": datetime.datetime(2000, 1, 17)
}

mahasiswa3 = {
    "nama": "Surotong",
    "nim": "222112197",
    "sks_lulus": 140,
    "beasiswa": False,
    "lahir": datetime.datetime(2003, 2, 4)
}

# dictionary di dalam dictionary (nesting dictionary)
data_mahasiswa = {
    'mhs1': mahasiswa1,
    'mhs2': mahasiswa2,
    'mhs3': mahasiswa3,
}

print(f'\n{data_mahasiswa}')

# mencetak nesting dictionary dengan gaya
print('')
print('='*67)
print('Key'.center(7) + '|' + 'Nama'.center(20) + '|' + 'NIM'.center(11) + '|' + 'SKS'.center(3) + '|' +'Beasiswa'.center(9) + '|' + 'Lahir'.center(11) + '|')
print('='*67)
for data in data_mahasiswa:
    key = data
    nama = data_mahasiswa[key]['nama']
    nim = data_mahasiswa[key]['nim']
    sks = data_mahasiswa[key]['sks_lulus']
    beasiswa = data_mahasiswa[key]['beasiswa']
    lahir = data_mahasiswa[key]['lahir'].strftime("%x")
    print(key.center(7) + '|' + nama.center(20) + '|' + nim.center(11) + '|' + str(sks).center(3) + '|' + f'{beasiswa:^9}' + '|' + f'{lahir:^11}' + '|')
    print('-'*67)