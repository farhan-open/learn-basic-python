# LAMBDA FUNCTION

'''
Lambda function, juga dikenal sebagai fungsi lambda atau fungsi anonim, adalah jenis fungsi khusus di Python yang digunakan untuk membuat fungsi sederhana dengan sintaks yang ringkas. Lambda function biasanya digunakan ketika Anda memerlukan fungsi kecil dan sederhana yang tidak memerlukan blok kode yang kompleks.

Ciri khas lambda function:

- Lambda function didefinisikan menggunakan kata kunci lambda.
- Lambda function biasanya hanya berisi satu ekspresi.
- Lambda function dapat memiliki beberapa parameter, tetapi hanya dapat mengembalikan satu nilai.
- Lambda function tidak diberi nama, karena mereka bersifat anonim. Namun, Anda dapat menyimpannya dalam variabel atau menggunakan sebagai argumen dalam fungsi lain.

SINTAKS DASAR LAMBDA FUNCTION:
lambda parameters: expression

'''

# Contoh 1: Membuat lambda function untuk penjumlahan dua angka
add = lambda a, b: a + b
result = add(3, 5)
print(result)  # Output: 8

# Contoh 2: Membuat lambda function untuk kuadrat suatu angka
square = lambda x: x**2
print(square(4))  # Output: 16

# Contoh 3: Menggunakan lambda function sebagai argumen dalam fungsi map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# contoh kegunaan: (melakukan sorting list dengan item string berdasarkan panjangnya)
data_list = ['Otong', 'Ucup', 'Mahmud', 'Eros', 'Icikiwir']
data_list.sort(key=lambda daftar: len(daftar)) # paramter key pada method sort list di samping memberikan kita kewenangan untuk melakukan sorting berdasarkan apa/berdasarkan key yang kita definisikan
print(f'List yang telah di-sort berdasarkan panjangnya: {data_list}')

# contoh kegunaan: (melakukan filter pada list dengan item berupa angka)
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_angka_baru = list(filter(lambda x: x < 5, data_angka))
print(data_angka_baru)

'''
Penjelasan:

1. lambda x: x < 5:
    Ini adalah lambda function yang mengambil satu parameter (x) dan mengembalikan hasil evaluasi dari ekspresi x < 5.
    Lambda function ini berarti "return True" jika nilai x kurang dari 5, dan "return False" jika tidak.

2. filter(lambda x: x < 5, data_angka):
    Fungsi filter() digunakan untuk menyaring elemen-elemen dalam data_angka berdasarkan kondisi yang diberikan oleh lambda function.
    filter() menerima dua argumen: fungsi (lambda function) yang digunakan untuk mengevaluasi setiap elemen, dan iterable (data_angka) yang akan disaring.

3. list(filter(lambda x: x < 5, data_angka)):
    Setelah proses penyaringan menggunakan filter(), hasilnya berupa objek filter (filter object).
    Dalam perintah ini, hasil filter object diubah menjadi list menggunakan fungsi list() sehingga elemen-elemen yang memenuhi kondisi pada lambda function menjadi elemen-elemen dari data_angka_baru.
'''

# CURRYING
'''
Currying adalah teknik dalam pemrograman fungsional di mana sebuah fungsi dengan banyak parameter diubah menjadi serangkaian fungsi dengan satu parameter. Setiap fungsi baru ini mewakili bagian dari evaluasi fungsi asli dan mengembalikan fungsi lain yang menangani bagian berikutnya dari evaluasi. Currying memungkinkan kita untuk memanggil fungsi dengan beberapa argumen secara bertahap, yang dapat meningkatkan fleksibilitas dan ekspresivitas kode.

Dalam Python, currying dapat diimplementasikan dengan menggunakan fungsi lambda dan closure (fungsi yang mengandung referensi ke lingkungan di luar lingkupnya). Fungsi lambda digunakan untuk menciptakan fungsi kecil yang menerima satu parameter, sedangkan closure digunakan untuk menyimpan referensi ke argumen sebelumnya.
'''

# contoh:
# Fungsi asli dengan banyak parameter
def add(a, b, c):
    return a + b + c

# Currying menggunakan lambda
def curry_add(a):
    return lambda b: lambda c: a + b + c

# Menggunakan fungsi asli
result1 = add(1, 2, 3)
print(result1)  # Output: 6

# Menggunakan currying dengan lambda
# CATATAN: curried_add di bawah ini akan dibaca sebagai sebuah fungsi, meskipun nampaknya seperti variabel biasa. curried_add merupakan fungsi yang berbasisi dari fungsi curry_add
curried_add = curry_add(1) # angka 1 di sini akan masuk mengisi parameter a pada fungsi curry_add
print(curried_add)
result2 = curried_add(2)(3) # angka 2 di sini akan masuk mengisi parameter b pada lambda pertama di dalam fungsi curry_add, sedangkan angka 3 akan masuk mengisi parameter c pada lambda kedua di dalam fungsi curry_add
print(result2)  # Output: 6

# bisa juga dipanggil sebagai berikut:
print(curry_add(1)(2)(3)) #Output: 6

'''
Penjelasan:

- Fungsi add() adalah fungsi asli dengan tiga parameter. Ia mengembalikan hasil penjumlahan ketiga parameter tersebut.
- Fungsi curry_add() adalah contoh implementasi currying dengan menggunakan lambda function. Ia menerima satu parameter a, dan mengembalikan fungsi lambda yang menerima satu parameter b, dan kemudian mengembalikan lagi fungsi lambda yang menerima satu parameter c. Hasil dari fungsi ini adalah penjumlahan ketiga parameter.
'''
