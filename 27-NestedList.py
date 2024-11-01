data_0 = [1, 2]
data_1 = [3, 4, 5]
list_biasa = [1, 2, 3, 5]
list_2D = [data_0, data_1, 'Banana']

print(f'List biasa = {list_biasa}')
print(f'List 2D = {list_2D}')

# contoh penggunaan
peserta_0 = ['Ucup', 25, 'Laki-laki']
peserta_1 = ['Otong', 10, 'Laki-laki']
peserta_2 = ['Dedeh', 63, 'Perempuan']

list_peserta = [peserta_0, peserta_1, peserta_2]

print(f'List peserta = {list_peserta}')

# mengakses elemen di dalam nested list
print('')
print('Mengakses Elemen pada Nested List'.center(50, '='))
print(f'Item pertama pada nested list adalah {list_peserta[0]}')
print(f'Item kedua pada nested list adalah {list_peserta[1]}')
print(f'Item ketiga pada nested list adalah {list_peserta[2]}')
print('')
print(f'Data nama 1: {list_peserta[0][0]}')
print(f'Data nama 2: {list_peserta[1][0]}')
print(f'Data nama 3: {list_peserta[2][0]}')
print('')
print(f'Data umur 1: {list_peserta[0][1]}')
print(f'Data umur 2: {list_peserta[1][1]}')
print(f'Data umur 3: {list_peserta[2][1]}')
print('')
print(f'Data jenis kelamin 1: {list_peserta[0][2]}')
print(f'Data jenis kelamin 2: {list_peserta[1][2]}')
print(f'Data jenis kelamin 3: {list_peserta[2][2]}')

# akses menggunakan for loop
print('')
print('Akses menggunakan for loop'.center(50, '='))
for peserta in list_peserta:
    print(f'Nama = {peserta[0]}')
    print(f'Umur = {peserta[1]}')
    print(f'Jenis kelamin = {peserta[2]}\n')

# modifikasi elemen nested list
list_peserta[2][0] = 'Putri' # mengubah nama pada list peserta_2
print(f'List peserta setelah dilakukan modfikasi = {list_peserta}')