data_angka = [1, 4, 3, 1, 2, 5, 6, 6, 7, 3 , 2, 9, 7, 5, 3, 0, 8, 1, 2, 5, 4, 8, 9, 0]

fruits = ['fig', 'apple', 'elderberry', 'grapefruit', 'durian', 'cherry', 'banana']
print(fruits)

numbers = [1, 2, 3, 4, 5]
print(numbers)

mixed = [True, "Hello", 3.14, [1, 2, 3]]
print(mixed)

# count data -> menghitung berapa kali sebuah data/item muncul dalam sebuah list
jumlah_data_4 = data_angka.count(4)
jumlah_data_2 = data_angka.count(2)

print(f'Nilai 4 dalam list muncul sebanyak {jumlah_data_4} kali')
print(f'Nilai 2 dalam list muncul sebanyak {jumlah_data_2} kali')

# mengambil posisi atau nilai index sebuah item pada list
index_banana = fruits.index("banana")

print(f"Index item 'banana' pada list fruits adalah: {index_banana}")

# mengurutkan item pada list
# 1. Metode sort()
'''
- Metode sort() digunakan untuk mengurutkan item-item dalam list secara langsung, yaitu dengan mengubah list asli.
- Metode ini mengurutkan list secara ascending (menaik), yaitu dari nilai terkecil ke terbesar.
'''
print('')
print('MENGGUNAKAN METHOD SORT'.center(35,'='))
print('LIST ANGKA'.center(25,':'))
print(f'List angka sebelum di-sort adalah:\n{data_angka}')
data_angka.sort()
print(f'\nList angka setelah diurutkan secara ascending adalah:\n{data_angka}')
data_angka.reverse()
print(f'\nList angka setelah diurutkan secara descending adalah:\n{data_angka}')

print('')
print('LIST STRING'.center(25,':'))
print(f'List fruits sebelum di-sort adalah:\n{fruits}')
fruits.sort() # mengurutkan secara ascending
print(f'\nList fruits setelah diurutkan secara ascending adalah:\n{fruits}')
fruits.reverse() #mengurutkan secara descending
print(f'\nList fruits setelah diurutkan secara descending adalah:\n{fruits}')

# 2. Fungsi sorted()
'''
- Fungsi sorted() digunakan untuk mengurutkan item-item dalam list dan mengembalikan list yang baru yang telah diurutkan.
- Fungsi ini tidak mengubah list asli, melainkan mengembalikan list baru yang diurutkan.
'''
data_angka = [1, 4, 3, 1, 2, 5, 6, 6, 7, 3 , 2, 9, 7, 5, 3, 0, 8, 1, 2, 5, 4, 8, 9, 0]
fruits = ['fig', 'apple', 'elderberry', 'grapefruit', 'durian', 'cherry', 'banana']

print('')
print('MENGGUNAKAN FUNGSI SORTED'.center(35,'='))
print('LIST ANGKA'.center(25,':'))
print(f'List angka sebelum di-sort adalah:\n{data_angka}')
print(f'\nList angka setelah diurutkan secara ascending adalah:\n{sorted(data_angka)}')
print(f'\nList angka setelah diurutkan secara descending adalah:\n{sorted(data_angka, reverse = True)}')

print('')
print('LIST STRING'.center(25,':'))
print(f'List fruits sebelum di-sort adalah:\n{fruits}')
print(f'\nList fruits setelah diurutkan secara ascending adalah:\n{sorted(fruits)}')
print(f'\nList fruits setelah diurutkan secara descending adalah:\n{sorted(fruits, reverse = True)}')