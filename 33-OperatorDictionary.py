list_farhan = [True, "Python", 100]

my_dict = {
    "nama": "Farhan", # "nama" adalah key
    "usia": 20, # "usia" adalah key
    "kota": "Jakarta", # "kota " adalah key
    "list": list_farhan, # "list" adalah key
}

# mengambil panjang dictionary
lendict = len(my_dict)
print(f'Panjang dari my_dict adalah = {lendict}')

# mengecek key exist atau tidak
key1 = 'nama'
cekkey1 = key1 in my_dict

key2 = 'panjang'
cekkey2 = key2 in my_dict
print(f'Apakah {key1} ada di my_dict: {cekkey1}')
print(f'Apakah {key2} ada di my_dict: {cekkey2}')

# mengakses item dictionary dengan get
print(my_dict.get("nama"))
print(my_dict.get("panjang")) # output: none karena tidak ada key 'panjang' pada dictionary yang kita buat. Atau kita dapat kostumisasi pesan 'None' sebagai berikut
print(my_dict.get("panjang", "Key tidak ditemukan")) # mengganti pesan 'None' menjadi 'Key tidak ditemukan'

# mengubah atau mengupdate value dari dictionary
print(f'my_dict sebelum diubah: {my_dict}')
my_dict["kota"] = "Makassar"
print(f'my_dict setelah diubah: {my_dict}')

# menambahkan key dan value baru pada dictionary
my_dict["pekerjaan"] = "Data Scientist"
print(f'my_dict setelah dilakukan penambahan: {my_dict}')

# mengubah atau mengupdate sekaligus value dari dictionary menggunakan method update()
my_dict.update({"kota": "Jakarta dan Makassar"}) # akan dilakukan update value pada key "kota"
my_dict.update({"hobi": "Ngoding"}) # akan ditambahkan value "Ngoding" pada key "hobi". Karena key "hobi" belum ada sebelumnya di my_dict
print('')
print(f'my_dict setelah dilakukan modifikasi: {my_dict}')

# menghapus item pada dictionary
del my_dict["hobi"]
print('')
print(f'my_dict setelah dilakukan penghapusan: {my_dict}')