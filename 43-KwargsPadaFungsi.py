'''
Dalam Python, **kwargs adalah mekanisme yang memungkinkan Anda untuk mengirimkan sejumlah argumen nama-kunci (keyword arguments) tanpa batas ke dalam sebuah fungsi. Istilah kwargs adalah singkatan dari "keyword arguments" (argumen nama-kunci) dan tanda asterisk ganda ** di depannya menunjukkan bahwa itu adalah parameter yang berisi kumpulan argumen nama-kunci yang tidak terbatas.

Penggunaan **kwargs memungkinkan Anda untuk membuat fungsi yang menerima argumen nama-kunci yang tidak pasti atau bervariasi. Dalam tubuh fungsi, **kwargs akan menjadi sebuah dictionary yang berisi pasangan kunci-nilai dari semua argumen nama-kunci yang dilewatkan ke fungsi tersebut.
''' 

# contoh
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(nama="Otong", umur=30, kota="Jakarta") # dengan memanggil fungsi seperti ini, maka terdapat 3 key untuk parameter fungsi, yaitu 'nama', 'umur', dan 'kota'

# studi kasus
def math(*angka, **kunci):
    hasil = 0
    if (kunci['operasi'] == 'tambah'):
        for i in angka:
            hasil += i
    elif (kunci['operasi'] == 'kurang'):
        hasil = angka[0]
        for i in angka:
            hasil -= i

        hasil += angka[0]
    elif (kunci['operasi'] == 'kali'):
        hasil = 1
        for i in angka:
            hasil *= i
    elif (kunci['operasi'] == 'bagi'):
        hasil = angka[0]
        for i in angka:
            hasil /= i

        hasil *= angka[0]
    else:
        print('Tidak ada operasi yang cocok')
    
    return hasil

output_tambah = math(4, 3, 7, 8, operasi = 'tambah') # dengan memanggil fungsi seperti ini, maka hanya terdapat 1 key untuk parameter fungsi, yaitu 'operasi'
output_kurang = math(4, 3, 7, 8, operasi = 'kurang') # dengan memanggil fungsi seperti ini, maka hanya terdapat 1 key untuk parameter fungsi, yaitu 'operasi'
output_kali = math(4, 3, 7, 8, operasi = 'kali') # dengan memanggil fungsi seperti ini, maka hanya terdapat 1 key untuk parameter fungsi, yaitu 'operasi'
output_bagi = math(4, 3, 7, 8, operasi = 'bagi') # dengan memanggil fungsi seperti ini, maka hanya terdapat 1 key untuk parameter fungsi, yaitu 'operasi'

print(f'Hasil penjumlahan = {output_tambah}')
print(f'Hasil pengurangan = {output_kurang}')
print(f'Hasil perkalian = {output_kali}')
print(f'Hasil pembagian = {output_bagi}')
