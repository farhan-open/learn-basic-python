'''
Di Python, setiap variabel memiliki cakupan (scope) yang menentukan bagian kode mana di mana variabel tersebut dapat diakses atau dikenali. Dalam Python, terdapat dua jenis cakupan utama yang perlu dipahami yaitu local scope dan global scope
'''

'''
1. Local Scope (Cakupan Lokal):
    - Local scope berarti cakupan variabel hanya berlaku di dalam blok kode atau fungsi di mana variabel tersebut dideklarasikan.
    - Variabel yang dideklarasikan dalam fungsi memiliki local scope dan hanya dapat diakses di dalam fungsi itu sendiri.
    - Ketika fungsi selesai dieksekusi, variabel lokal tidak lagi ada dalam memori.
'''

# contoh:
def my_function():
    x = 10  # Variabel lokal, hanya berlaku di dalam fungsi ini
    print(x)

my_function()  # Output: 10

# Akses variabel lokal di luar fungsi menyebabkan NameError
# print(x)  # Error: NameError: name 'x' is not defined

'''
2. Global Scope (Cakupan Global):
    - Global scope berarti cakupan variabel berlaku di seluruh kode program, yaitu di luar blok kode fungsi atau kelas.
    - Variabel yang dideklarasikan di luar fungsi atau kelas memiliki global scope dan dapat diakses dari semua bagian kode program.
    - Variabel global harus dideklarasikan di luar semua fungsi atau kelas sebelum dapat digunakan di dalamnya.
'''

# contoh:
x = 10  # Variabel global (variabel lokal dan variabel global dapat memiliki nama yang sama dan tidak akan menyebabkan konflik, karena cakupannya yang berbeda)

def my_function():
    print(x)  # Mengakses variabel global di dalam fungsi

my_function()  # Output: 10

def another_function():
    print(x)  # Mengakses variabel global di dalam fungsi lain

another_function()  # Output: 10

# MERUBAH VARIABEL GLOBAL DARI DALAM SEBUAH FUNGSI
angka = 0

def ubah_angka(nilai_baru):
    global angka # membuat fungsi ubah_angka memiliki akses ke variabel global 'angka'
    angka = nilai_baru # melakukan perubahan pada variabel global yang telah diakses sebelumnya

print(f'Nilai angka sebelum diubah: {angka}')
ubah_angka(3)
print(f'Nilai angka setelah diubah: {angka}')

# CATATAN: VARIABEL YANG DIBUAT/DIDEFINISIKAN DI DALAM PERULANGAN DAN PERCABANGAN (IF) TETAP DIANGGAP SEBAGAI VARIABEL GLOBAL. BUKTINYA ADALAH SEBAGAI BERIKUT:
nilai = 0

for i in range(5):
    nilai += i
    nilai_dummy = 0

if (nilai_dummy == 0):
    boolean = True
else:
    boolean = False

def akses_variabel():
    print(nilai_dummy)

def akses_boolean():
    print(boolean)

print(nilai)
akses_variabel()
akses_boolean()