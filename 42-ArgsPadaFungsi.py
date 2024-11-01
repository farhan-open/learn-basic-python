''''
Dalam Python, *args adalah sebuah mekanisme yang memungkinkan Anda untuk mengirimkan sejumlah argumen tanpa batas ke dalam sebuah fungsi. Istilah args adalah singkatan dari "arguments" (argumen) dan tanda asterisk * di depannya menunjukkan bahwa itu adalah parameter yang berisi kumpulan argumen yang tidak terbatas.

Penggunaan *args memungkinkan Anda untuk membuat fungsi yang menerima jumlah argumen yang tidak pasti atau bervariasi. Dalam tubuh fungsi, *args akan menjadi tuple yang berisi semua argumen yang dilewatkan ke fungsi tersebut.
'''

# contoh

def cetak(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'Nama: {nama}\nTinggi: {tinggi}\nBerat: {berat}')

cetak('Otong', 170, 65)

# studi kasus lain
def tambah(*data): # INGAT BAHWA PARAMETER ARGS (YANG DIBERI DENGAN TANDA *) AKAN MENJADI TUPLE
    output = 0
    for angka in data:
        output = output + angka
    
    return output

hasil = tambah(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(hasil)

hasil2 = tambah( 3, 6, 7)
print(hasil2)