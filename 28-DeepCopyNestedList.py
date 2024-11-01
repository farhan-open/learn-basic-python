data_0 = [1, 2]
data_1 = [3, 4, 5]
list_2D = [data_0, data_1, 'Banana']

print(f'List 2D = {list_2D}')

# meng-copy nested list
list_2D_copy = list_2D.copy()
print(f'\nList 2D hasil copy = {list_2D_copy}')

# mengambil informasi address list
print(f'\nAlamat memori list_2D adalah {hex(id(list_2D))}')
print(f'Alamat memori list_2D_copy adalah {hex(id(list_2D_copy))}')

# mengambil informasi address dari tiap member pada list
print(f'\nAlamat memori member pertama')
print(f'Alamat memori list_2D adalah {hex(id(list_2D[0]))}')
print(f'Alamat memori list_2D_copy adalah {hex(id(list_2D_copy[0]))}')
# TERNYATA SAMA, SEHINGGA JIKA KITA LAKUKAN PERUBAHAN PADA MEMBERNYA (data_0 dan data_1) MAKA KEDUA LIST 2D YANG KITA PUNYA AKAN TERPENGARUH MESKIPUN KEDUANYA SUDAH MEMILIKI ALAMAT MEMORI YANG BERBEDA

# contoh
list_2D[1][0] = 5
print(f'\nList 2D = {list_2D}')
print(f'List 2D hasil copy = {list_2D_copy}')

# NAMUN JIKA KITA MELAKUKAN PERUBAHAN PADA ITEM YANG TIDAK TERMASUK NESTED LIST, MAKA PERUBAHAN HANYA TERJADI PADA LIST YANG KITA MODIFIKASI SECARA LANGSUNG
# contoh
list_2D[2] = 'Python'
print(f'\nList 2D = {list_2D}')
print(f'List 2D hasil copy = {list_2D_copy}')

# untuk mengantisipasi kondisi ini, pada nested list kita perlu melakukan deepcopy sebagai berikut
from copy import deepcopy
list_2D = [data_0, data_1, 'Banana']
list_2D_deepcopy = deepcopy(list_2D)
print('')
print('Hasil Deepcopy pada Nested List'.center(50, '='))
print(f'List 2D = {list_2D}')
print(f'List 2D hasil deepcopy = {list_2D_deepcopy}')
print(f'Alamat memori list_2D adalah {hex(id(list_2D))}')
print(f'Alamat memori list_2D_deepcopy adalah {hex(id(list_2D_deepcopy))}')
print(f'\nAlamat memori member pertama')
print(f'Alamat memori list_2D adalah {hex(id(list_2D[0]))}')
print(f'Alamat memori list_2D_deepcopy adalah {hex(id(list_2D_deepcopy[0]))}')
# sudah beda, sehingga kedua nested list sekarang akan bersifat saling bebas
# contoh
list_2D[1][0] = 500
print(f'\nList 2D = {list_2D}')
print(f'List 2D hasil deepcopy = {list_2D_deepcopy}')