# 1. Menyambung string (concatenate)
nama_pertama = 'ucup'
nama_tengah = 'D'
nama_akhir = 'Fame'

nama_lengkap = nama_pertama + ' ' + nama_tengah + nama_akhir
print(nama_lengkap)

# contoh lain
print('Saya' + ' ' + 'belajar' + ' ' + 'Python')

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print('Panjang dari dari', nama_lengkap, '=', panjang) # pada kasus ini, string kosong yang merupakan string juga dihitung sebagai satu string

# 3. Operator untuk string

# mengecek apakah ada komponen char atau string di sebuah string
d1 = 'd'
status1 = d1 in nama_lengkap
print('Apakah', d1, 'ada di', nama_lengkap, '?', status1)

d2 = 'D'
status2 = d2 in nama_lengkap
print('Apakah', d2, 'ada di', nama_lengkap, '?', status2)

ucup = 'ucup'
status3 = ucup in nama_lengkap
print('Apakah', ucup, 'ada di', nama_lengkap, '?', status3)

print('')
# mengecek apakah komponen char atau string tertentu tidak ada di sebuah string
d1 = 'd'
status1 = d1 not in nama_lengkap
print('Apakah', d1, 'tidak ada di', nama_lengkap, '?', status1)

d2 = 'D'
status2 = d2 not in nama_lengkap
print('Apakah', d2, 'tidak ada di', nama_lengkap, '?', status2)

ucup = 'ucup'
status3 = ucup not in nama_lengkap
print('Apakah', ucup, 'tidak ada di', nama_lengkap, '?', status3)

# mengulang string
print('wk'*10) # string 'wk' akan dicetak sebanyak 10 kali secara inline
print('')
print(8*'ha') # string 'ha' akan dicetak sebanyak 8 kali secara inline

# indexing dari kiri ke kanan (dimulai dari index ke-0)
print('Index ke-0 dari ' + nama_lengkap + ' adalah ', nama_lengkap[0])
print('Index ke-6 dari ' + nama_lengkap + ' adalah ', nama_lengkap[6])
print('Index ke-4 dari ' + nama_lengkap + ' adalah ', nama_lengkap[4])

# indexing dari kanan ke kiri (dimulai dari index ke-(-1))
print('Index ke-(-1) dari ' + nama_lengkap + ' adalah ', nama_lengkap[-1])
print('Index ke-(-2) dari ' + nama_lengkap + ' adalah ', nama_lengkap[-2])
print('Index ke-(-3) dari ' + nama_lengkap + ' adalah ', nama_lengkap[-3])

# mengambil index berdasarkan range
print('index ke-0 sampai 3 dari ' + nama_lengkap + ' adalah ', nama_lengkap[0:4]) # jika ingin mengambil string berdasarkan range tertentu, penulisan sintaksnya adalah sebagai berikut: variabel_string[indeksAwal:indeksAkhir+1]

print('index ke-3 sampai 7 dari ' + nama_lengkap + ' adalah ', nama_lengkap[3:8])

# mengambil index string berdasarkan pola tertentu
print('index ke-[0, 2, 4, 6, 8, 10] dari ' + nama_lengkap + ' adalah ', nama_lengkap[0:11:2]) # jika ingin mengambil string berdasarkan pola tertentu, penulisan sintaksnya adalah sebagai berikut: variabel_string[indeksAwal:indeksAkhir+1:pola_increment]

# mengindentifikasi item paling kecil pada sebuah string (berdasarkan urutan abjad/kode ASCII)
print('')
print('Item yang nilainya paling kecil dari ' + nama_lengkap + ' adalah ' + min(nama_lengkap))
ascii_code_spasi = ord(' ')
print('Kode ASCII untuk spasi ( ) adalah ' + str(ascii_code_spasi))

# mengindentifikasi item paling besar pada sebuah string (berdasarkan urutan abjad/kode ASCII)
print('')
print('Item yang nilainya paling besar dari ' + nama_lengkap + ' adalah ' + max(nama_lengkap))
ascii_code_u = ord('u')
print('Kode ASCII untuk huruf u adalah ' + str(ascii_code_u))

# 4. Operator dalam bentuk method
'''
Karena tipe string pada python diidentifikasi sebagai sebuah class, maka terdapat method khusus untuk class string tersebut yang dapat digunakan
'''
# Beberapa operator dalam bentuk method yang bisa digunakan pada string adalah sebagai berikut:

# a. Operator 'count'
nama = 'Otong Surotong Pararotong'
jumlah = nama.count('o') # menghitung jumlah o yang disimpan oleh variabel nama (case sensitive)
print("Jumlah 'o' pada " + nama + " = " + str(jumlah))

# b. Merubah semua karakter dalam string menjadi upper case
salam = 'halo dunia!'
print('Salam dalam bentuk normal = ' + salam + '. Tapi, dalam bentuk upper case = ' + salam.upper())

# c. Merubah semua karakter dalam string menjadi lower case
alay = 'aKu KeCe AbieEEsZz'
print('Alay dalam bentuk normal = ' + alay + '. Tapi, dalam bentuk lower case = ' + alay.lower())

# d. Pengecekan dengan is method

# contoh 1: pengecekan lower case
text = "hello"
print(text.islower())  # Output: True

text = "Hello"
print(text.islower())  # Output: False

text = "Hello, World!"
print(text.islower())  # Output: False

text = "123"
print(text.islower())  # Output: False

# contoh 2: pengecekan upper case
text = "HELLO"
print(text.isupper())  # Output: True

text = "Hello"
print(text.isupper())  # Output: False

text = "Hello, World!"
print(text.isupper())  # Output: False

text = "123"
print(text.isupper())  # Output: False

# contoh 3: isalpha() -> untuk mengecek apakah semua karakter dari sebuah string merupakan huruf atau bukan
# contoh 4: isalnum() -> untuk mengecek apakah semua karakter dari sebuah string merupakan kombinasi huruf dan angka atau bukan
# contoh 5: isdecimal() -> untuk mengecek apakah semua karakter dari sebuah string merupakan angka atau bukan
# contoh 6: isspace() -> untuk mengecek apakah semua karakter dari sebuah string merupakan spasi, tab, newline, \n, atau bukan

# contoh 7: istitle() -> untuk memeriksa apakah sebuah string memiliki format judul (title case)
text = "Hello World"
print(text.istitle())  # Output: True

text = "Hello world"
print(text.istitle())  # Output: False

text = "Hello, World"
print(text.istitle())  # Output: True

text = "123 Hello World"
print(text.istitle())  # Output: True

# e. Pengecekan komponen (startswith() dan endswith())
# startswith()
text = "Hello, World"
print(text.startswith("Hello"))  # Output: True

text = "Hello, World"
print(text.startswith("World"))  # Output: False

text = "Hello, World"
print(text.startswith("Hello, "))  # Output: True

# endswith()
text = "Hello, World"
print(text.endswith("World"))  # Output: True

text = "Hello, World"
print(text.endswith("Hello"))  # Output: False

text = "Hello, World"
print(text.endswith(", World"))  # Output: True

# f. Penggabungan komponen join()
my_list = ["Hello", "World", "Python"]
result = " ".join(my_list)
print(result)  # Output: Hello World Python

my_tuple = ("Apple", "Banana", "Orange")
result = "-".join(my_tuple)
print(result)  # Output: Apple-Banana-Orange

my_set = {"cat", "dog", "rabbit"}
result = ", ".join(my_set)
print(result)  # Output: rabbit, cat, dog

# g. Pemisahan komponen split()
'''
Metode .split() adalah metode string dalam Python yang digunakan untuk membagi (split) string menjadi potongan-potongan lebih kecil berdasarkan pemisah (separator) yang ditentukan dengan tipe return berupa list.
'''

text = "Hello World Python"
result = text.split()
print(result)  # Output: ['Hello', 'World', 'Python']

text = "Apple-Banana-Orange"
result = text.split("-")
print(result)  # Output: ['Apple', 'Banana', 'Orange']

text = "cat, dog, rabbit"
result = text.split(", ")
print(result)  # Output: ['cat', 'dog', 'rabbit']

# h. Alokasi karakter [.rjust(), .ljust(), dan .center()]

# Metode .rjust(width, fillchar): --> fillchar defaultnya adalah spasi
'''
Metode .rjust() digunakan untuk melakukan perataan teks ke kanan (right-aligned) di dalam suatu lebar yang ditentukan.
'''
text = "Hello"
result = text.rjust(10)
print(result)  # Output: "     Hello"

result = text.rjust(10, "-")
print(result)  # Output: "-----Hello"

# Metode .ljust(width, fillchar): --> fillchar defaultnya adalah spasi
'''
Metode .ljust() digunakan untuk melakukan perataan teks ke kiri (left-aligned) di dalam suatu lebar yang ditentukan.
'''
text = "Hello"
result = text.ljust(10)
print(result)  # Output: "Hello     "

result = text.ljust(10, "*")
print(result)  # Output: "Hello*****"

# Metode .center(width, fillchar): --> fillchar defaultnya adalah spasi
'''
Metode .center() digunakan untuk melakukan perataan teks di tengah (center-aligned) di dalam suatu lebar yang ditentukan.
'''
text = "Hello"
result = text.center(10)
print(result)  # Output: "  Hello   "

result = text.center(10, "=")
print(result)  # Output: "==Hello==="

# i. Menghapus karakter spasi (whitespace) atau karakter khusus di awal dan akhir sebuah string
text = "  Hello World  "
result = text.strip() # jika argumennya tidak diatur, maka secara default akan menghapus karakter spasi
print(result)  # Output: "Hello World"

text = "---Hello---"
result = text.strip("-")
print(result)  # Output: "Hello"

text = "\t\tPython\n"
result = text.strip()
print(result)  # Output: "Python"