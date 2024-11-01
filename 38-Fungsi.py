'''
SINTAKS DASAR FUNGSI DI PYTHON

def nama_fungsi(parameter1, parameter2, ...):
    # Blok kode fungsi
    # Pernyataan 1
    # Pernyataan 2
    # ...
    return nilai_kembali

CATATAN: Karena python merupakan interpreted language, maka fungsi tidak dapat dipanggil pada sebuah program jika tidak didefinisikan/dibuat terlebih dahulu. Sehingga, sebelum memanggil fungsi, kita harus membuatnya terlebih dahulu
'''

# contoh:

# fungsi tanpa parameter
def salam():
    print('Halo Dunia!')

salam() # memanggil fungsi

# fungsi dengan parameter
def jumlah(angka1, angka2):
    return angka1 + angka2

# fungsi dengan lebih dari satu return value
def operasi_matematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah, kurang, kali, bagi

k, l, m, n = operasi_matematika(8, 3) # memanggil fungsi
print(f'Hasil tambah = {k}')
print(f'Hasil kurang = {l}')
print(f'Hasil kali = {m}')
print(f'Hasil bagi = {n:.2f}')

hasil = jumlah (2, 3) # memanggil fungsi
print(hasil)

# fungsi dengan parameter list
def hai(list_mahasiswa):
    data_mahasiswa = list_mahasiswa.copy()
    for mahasiwa in data_mahasiswa:
        print(f'Halo {mahasiwa}!')

daftar_mahaswiwa = ['Otong', 'Mahmud', 'Jajang', 'Eros']
hai(daftar_mahaswiwa)
