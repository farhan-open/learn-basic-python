fruits = ["apple", "banana", "cherry"]
print(fruits)

numbers = [1, 2, 3, 4, 5]
print(numbers)

mixed = [True, "Hello", 3.14, [1, 2, 3]]
print(mixed)

# mengakses elemen di dalam list
'''
Kita dapat mengakses elemen-elemen dalam list menggunakan indeks, yang dimulai dari 0 untuk elemen pertama.
'''
print('')
print(f'Index ke-0 dari list fruits adalah {fruits[0]}')

print(f'\nIndex ke-4 dari list numbers adalah {numbers[4]}')

print(f'\nIndex ke-3 dari list mixed adalah {mixed[3]} dengan tipe {type(mixed[3])}')

# mengambil info jumlah item di dalam list
print(f'\nPanjang data dari list fruits adalah {len(fruits)}')

print(f'\nPanjang data dari list numbers adalah {len(numbers)}')

print(f'\nPanjang data dari list mixed adalah {len(mixed)}')

# MENAMBAHKAN ITEM PADA LIST SESUAI POSISI
print('')
print('Menambahkan Isi List'.center(50, ':'))
print(f'Isi list fruits sebelum ditambah = {fruits}')
fruits.insert(1, 'grape') # menambahkan item 'grape' pada list fruits di index ke-1
print(f'Isi list fruits setelah ditambah = {fruits}')

# MENAMBAHKAN ITEM DI AKHIR LIST
print('')
print('Menambahkan Isi List di Bagian Akhir'.center(65, ':'))
print(f'Isi list fruits sebelum ditambah di bagian akhir = {fruits}')
fruits.append('mango') # menambahkan item 'mango' pada bagian akhir list fruits
print(f'Isi list fruits setelah ditambah di bagian akhir = {fruits}')

# MENAMBAH LIST DENGAN LIST
print('')
print('Menambahkan Isi List dengan List'.center(65, ':'))
print(f'Isi list fruits sebelum ditambah dengan list = {fruits}')
fruits.extend(numbers) # menggabungkan list fruits dan list numbers
print(f'Isi list fruits setelah ditambah dengan list = {fruits}')

# MERUBAH ITEM PADA LIST
print('')
print('Mengubah Item pada List'.center(65, ':'))
print(f'Isi list numbers yang asli = {numbers}')
numbers[2] = 3.14 # mengubah item dengan index = 2 pada list numbers dengan 3.14
print(f'Isi list numbers setelah dilakukan perubahan = {numbers}')

# ME-REMOVE ITEM PADA LIST
print('')
print('Menghapus Item pada List'.center(65, ':'))
print(f'Isi list mixed yang asli = {mixed}')
mixed.remove([1,2,3]) # menghapus item [1, 2, 3] pada list mixed
print(f'Isi list numbers setelah dilakukan penghapusan = {mixed}')

# ME-REMOVE DATA PALING BELAKANG PADA LIST
print('')
print('Menghapus Item Terakhir pada List'.center(65, ':'))
print(f'Isi list fruits yang asli = {fruits}')
data_buang = fruits.pop() # item terakhir dari list fruits disimpan pada variabel data_buang
print(f'Isi list fruits setelah dilakukan penghapusan pada item terakhir = {fruits}')
print(f'Data yang dihapus dari list fruits adalah {data_buang}')