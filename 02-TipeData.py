# TIPE DATA DASAR

# 1. Integer (bilangan bulat)
data_interger = 11
print("Data: ", data_interger, "bertipe: ", type(data_interger))

# 2. Float (angka desimal atau angka dengan koma)
data_float = 2.5
print("Data: ", data_float, "bertipe: ", type(data_float))

# 3. String (kumpulan karakter)
data_string = "Aku ingin menjadi seorang data scientist"
print("Data: ", data_string, "bertipe: ", type(data_string))

# 4. Boolean (tipe data biner -> true/false)
data_bool = True
print("Data: ", data_bool, "bertipe: ", type(data_bool))

# TIPE DATA KHUSUS

# 1. Tipe data dari bahasa C (kita bisa mengimport tipe data dari bahasa C ke python karena pyhton ini dibangun dengan menggunakan bahasa C)
from ctypes import c_double # pada contoh ini kita meng-import tipe data double dari bahasa C

data_c_double = c_double(10.5)
print("Data: ", data_c_double, "bertipe: ", type(data_c_double))

# 2. Bilangan kompleks (Menyatakan pasangan angka real dan imajiner)
data_complex = complex(5, 6)
print("Data: ", data_complex, "bertipe: ", type(data_complex))

# TIPE DATA TAMBAHAN

"""
1. List
Tipe data list digunakan untuk menyimpan kumpulan nilai atau objek. List bersifat mutable, yang berarti elemennya dapat diubah setelah dibuat. Elemen-elemen dalam list dipisahkan oleh koma dan dikelilingi oleh tanda kurung siku ([])
"""
buah = ["apel", "jeruk", "pisang"]
print(buah[0])  # Output: apel
buah.append("mangga")
print(buah)  # Output: ['apel', 'jeruk', 'pisang', 'mangga']

"""
2. Tuple
Tipe data tuple mirip dengan list, tetapi bersifat immutable, artinya elemennya tidak dapat diubah setelah dibuat. Tuple dikelilingi oleh tanda kurung biasa ()
"""
bulan = ("Januari", "Februari", "Maret")
print(bulan[1])  # Output: Februari

"""
3. Set
Tipe data set digunakan untuk menyimpan kumpulan nilai unik tanpa urutan tertentu. Set tidak mengizinkan duplikasi elemen. Elemen-elemen dalam set dipisahkan oleh koma dan dikelilingi oleh tanda kurung kurawal ({}) atau dapat juga dibuat menggunakan fungsi set()
"""
huruf = {"a", "b", "c"}
huruf.add("d")
print(huruf)  # Conth Output: {'a', 'b', 'c', 'd'} atau dengan urutan lain yang bersifat random

"""
4. Dictionary
Tipe data dictionary digunakan untuk menyimpan pasangan kunci-nilai (key-value pair). Setiap kunci harus unik dalam dictionary. Dictionary dikelilingi oleh tanda kurung kurawal ({}) dan setiap pasangan kunci-nilai dipisahkan oleh koma
"""
data = {"nama": "John", "umur": 25, "kota": "Jakarta"}
print(data["nama"])  # Output: John
data["pekerjaan"] = "Pengembang"
print(data)  # Output: {'nama': 'John', 'umur': 25, 'kota': 'Jakarta', 'pekerjaan': 'Pengembang'}

