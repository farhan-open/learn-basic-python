'''
List (daftar) adalah tipe data yang digunakan untuk menyimpan koleksi elemen yang berbeda dalam urutan tertentu. List adalah salah satu tipe data bawaan dalam Python dan sangat serbaguna.
'''

fruits = ["apple", "banana", "cherry"]
print(fruits)

numbers = [1, 2, 3, 4, 5]
print(numbers)

mixed = [True, "Hello", 3.14, [1, 2, 3]]
print(mixed)

# cara alternatif membuat list melalui range
data_range = range(0, 10) # mengandung range dari 0 sampai 9
print(f"Isi asli dari data_range = {data_range}")

data_list = list(data_range)
print(f"Isi dari data list = {data_list}")

# membuat list dengan for loop (list comprehension)
list_for = [i for i in range(0, 10)]
print(f"Isi dari list_for adalah {list_for}")

# membuat setiap item list pada list_for dikuadratkan
list_for = [i**2 for i in range(0, 10)]
print(f"Isi dari list_for setelah dikuadratkan adalah {list_for}")

# membuat list menggunakan for dan if
list_for_if = [i for i in range(0, 10) if i % 2 == 0] # membuat list yang isinya adalah range 0-9 namun khusus untuk bilangan genap
print(f"Isi dari list_for_if adalah {list_for_if}")

