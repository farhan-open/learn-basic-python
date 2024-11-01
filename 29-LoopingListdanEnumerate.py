# Looping dari list

# for loop
kumpulan_angka = [4, 3, 2, 5, 6, 7]

for angka in kumpulan_angka:
    print(f'Angka = {angka}')

fruits = ['fig', 'apple', 'elderberry', 'grapefruit', 'durian', 'cherry', 'banana']
panjang = len(fruits)
print(f'Panjang dari lis fruits adalah {panjang}')

# mengakses index dan item list menggunakan for loop dan range
print('')
print('Mengakses Indeks Item pada List Menggunakan For Loop dan Range'.center(70, '='))
for i in range(panjang):
    print(f'Item pada index ke-{i} adalah {fruits[i]}')

# mengakses index dan item list menggunakan while loop
print('')
print('Mengakses Indeks Item pada List Menggunakan While Loop'.center(70, '='))
i = 0
while (i < panjang):
    print(f'Item pada index ke-{i} adalah {fruits[i]}')
    i += 1

# mengakses item list menggunakan list comprehension
print('')
print('Mengakses Indeks Item pada List Menggunakan List Comprehension'.center(70, '='))
[print(f'Item-item pada list fruits adalah:\n{i}') for i in fruits]

# contoh lain
angka_kuadrat = [i**2 for i in kumpulan_angka] # meng-kuadratkan tiap item pada list kumpulan angka
print(f'\n{angka_kuadrat}')

# mengakses index dan item list menggunakan enumerate
'''
Fungsi enumerate() mengembalikan objek enumerate yang berisi pasangan tuple (indeks, nilai) untuk setiap elemen dalam iterable (seperti list, tuple, string, atau objek lain yang dapat diiterasi)
'''
print('')
print('Mengakses Indeks Item pada List Menggunakan Enumerate'.center(70, '='))
for i, d in enumerate(fruits):
    print(f'Item pada index ke-{i} adalah {d}')