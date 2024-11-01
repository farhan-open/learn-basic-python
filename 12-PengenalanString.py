# CARA MEMBUAT STRING

# 1. Menggunakan single quote ('')
data = 'Ini adalah string'
print('Isi dari data adalah:', data, 'dengan tipe:', type(data))

# 2. Menggunakan double quote ("")
data = "Ini string juga"
print('Isi dari data adalah:', data, 'dengan tipe:', type(data))

# 3. Kasus jika keduanya digabungkan
kalimat1 = '"Halo Dunia!"'
print(kalimat1)

kalimat2 = "'Halo beb!'"
print(kalimat2)

# PENGGUNAAN TANDA \
'''
Tanda \ dalam string di Python digunakan sebagai karakter escape (pemetaan khusus) untuk menyisipkan karakter khusus ke dalam string. Ketika \ diikuti oleh karakter khusus tertentu, itu memberikan makna khusus ke karakter tersebut
'''

print('Mari salat jum\'at') # membuat tanda ' menjadi string

print('C:\\user\\Farhan') # menyisipkan backslash pada string

print('Ucup\tOtong, saling berjauhan') # menyisipkan tab pada string

print('Ucup\bOtong, saling berdekatan') # menyisipkan backspace pada string

print('')
print('Ini adalah baris pertama.\nIni adalah baris kedua') # menyisipkan enter pada sebuah string

# MEMBUAT RAW STRING ATAU STRING LITERAL

'''
Untuk membuat raw string di Python, Anda dapat menggunakan prinsip "raw string literals" dengan menambahkan awalan r sebelum tanda kutip pembuka string. Dengan menggunakan raw string, karakter escape (pemetaan khusus) tidak akan diinterpretasikan, sehingga karakter seperti \n, \t, dan \ akan diperlakukan sebagai karakter biasa tanpa makna khusus.
'''
print(r'C:\new-folder')

# membuat multiline literal string
print('''
Nama: Farhan
NIM: 222112195
''')
# catatan: tampilan string pada output akan benar-benar persis disesuaikan dengan tampilan string pada sintaks program kita, termasuk tab, spasi, tanda baca, dan seterusnya.

# menggabungkan multiline literal string dan raw
print(r'''
Nama: Farhan
NIM: 222112195\SD
Website: www.farhan.com/index
''')