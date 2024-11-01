# Looping Dictionary
list_farhan = [True, "Python", 100]

my_dict = {
    "nama": "Farhan", # "nama" adalah key
    "usia": 20, # "usia" adalah key
    "kota": "Jakarta", # "kota " adalah key
    "list": list_farhan, # "list" adalah key
}

# menggunakan for loop biasa (yang keluar hanyalah key-nya)
for i in my_dict:
    print(i)

# for loop untuk mengambil valuenya
for j in my_dict:
    print(my_dict.get(j))

# for loop untuk mengambil key dan valuenya
keys = my_dict.keys() # mengambil key dari dictionary yang kita punya
for key in keys:
    value = my_dict[key]
    print(f'Key: {key} -> Value: {value}')

# for loop berdasarkan item pada dictionary
items = my_dict.items()
print(f'Items dari my_dict adalah: {items}') # items akan mengambil pasangan key dan valuenya sekaligus

print('')
for item in items:
    print(item)

# untuk memsahkan antara key dan value berdasarkan item pada dictionary, dapat dilakukan sebagai berikut:
print('')
for key, value in items:
    print(f'Key: {key} -> Value: {value}')
