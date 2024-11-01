# TUPLE

'''
Tuples (tuple) adalah tipe data dalam Python yang digunakan untuk menyimpan kumpulan elemen, mirip dengan list. Perbedaannya adalah tuples bersifat tidak dapat diubah (immutable), artinya setelah dibuat, elemen-elemen dalam tuple tidak dapat ditambah, diubah, atau dihapus. Tuples menggunakan tanda kurung biasa () untuk menyatakan elemen-elemennya
'''

# membuat tuple
my_tuple = (1, 2, 3, "Hello", True)
print(my_tuple)

# mengakses elemen tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: "Hello"

# SET
'''
Set (himpunan) adalah tipe data dalam Python yang digunakan untuk menyimpan kumpulan elemen unik, artinya tidak ada elemen duplikat dalam set. Set menggunakan kurung kurawal {} untuk menyatakan elemen-elemennya
'''

# membuat set
print('')
my_set = {1, 2, 3, 4, 5}
empty_set = {}

print(my_set)
print(empty_set)

'''
- Set tidak menyimpan elemen dalam urutan tertentu. Ini berarti set tidak dapat diakses menggunakan indeks seperti list atau tuple.
- Karena elemen-elemen tidak berurutan, tidak ada cara untuk merujuk elemen dalam set berdasarkan indeks.
- Jika Anda perlu mengakses elemen tertentu, Anda harus melakukannya dengan pencarian menggunakan pernyataan in.
'''
print(3 in my_set)  # Output: True

'''
METHOD PADA SET
- Set memiliki berbagai metode yang berguna, seperti add(), remove(), discard(), pop(), union(), intersection(), dan lainnya.
- Metode-metode ini memungkinkan Anda untuk melakukan operasi pada set, seperti menambahkan elemen baru, menghapus elemen tertentu, dan melakukan operasi himpunan seperti gabungan atau irisan dengan set lain.
'''

# contoh
my_set = {1, 2, 3}
print(f'Set asli = {my_set}')
my_set.add(4)
print(f'Set setelah dilakukan penambahan = {my_set}')  # Output: {1, 2, 3, 4}

my_set.remove(2)
print(f'Set setelah dilakukan penghapusan = {my_set}')  # Output: {1, 3, 4}
