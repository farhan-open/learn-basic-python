list_farhan = [True, "Python", 100]

my_dict = {
    "nama": "Farhan", # "nama" adalah key
    "usia": 20, # "usia" adalah key
    "kota": "Jakarta", # "kota " adalah key
    "list": list_farhan, # "list" adalah key
}

#  proses copy pada  dictionary kurang lebih sama dengan proses copy di list
my_dict_2 = my_dict # my_dict dan my_dict_2 akan merujuk ke alamat memori yang sama. Sehingga, apapun yang dilakukan pada my_dict akan berpengaruh pada my_dict_2 (begitupun sebaliknya)
print(f'Isi dari my_dict adalah:\n{my_dict}')
print(f'Isi dari my_dict_2 adalah:\n{my_dict_2}')
print(f'\nAlamat memori dari my_dict adalah = {hex(id(my_dict))}')
print(f'Alamat memori dari my_dict_2 adalah = {hex(id(my_dict_2))}')

my_dict_copy = my_dict.copy() # my_dict dan my_dict_copy akan merujuk ke alamat memori yang berbeda. Sehingga, apapun yang dilakukan pada my_dict tidak akan berpengaruh pada my_dict_2 (begitupun sebaliknya) -- saling bebas
print('')
print(f'Isi dari my_dict adalah:\n{my_dict}')   
print(f'Isi dari my_dict_copy adalah:\n{my_dict_copy}')
print(f'\nAlamat memori dari my_dict adalah = {hex(id(my_dict))}')
print(f'Alamat memori dari my_dict_copy adalah = {hex(id(my_dict_copy))}')

# Pop dictionary berdasarkan key
data_list = my_dict.pop("list") # akan mengeluarkan item dengan key 'list' pada dictionary dan menyimpannya pada variabel data_list
print(f'\nData list = {data_list}')
print(f'Isi dari my_dict setelah dilakukan pop berdasarkan key:\n{my_dict}')

# Pop dictionary berdasarkan item
my_dict = {
    "nama": "Farhan", # "nama" adalah key
    "usia": 20, # "usia" adalah key
    "kota": "Jakarta", # "kota " adalah key
    "list": list_farhan # "list" adalah key
}

item_terakhir = my_dict.popitem() # akan mengeluarkan item terakhir pada list my_dict dan menyimpannya pada variabel item_terakhir
print(f'\nItem terakhir dari my_dict = {item_terakhir}')
print(f'Isi dari my_dict setelah dilakukan pop berdasarkan item:\n{my_dict}')