'''
Dictionary (mirip dengan associative array) adalah tipe data dalam Python yang digunakan untuk menyimpan kumpulan pasangan kunci-nilai (key-value pairs). Dalam dictionary, setiap kunci (key) harus unik dan digunakan untuk mengidentifikasi nilai-nilai (values) yang terkait. Dictionary menggunakan tanda kurung kurawal {} dan memiliki pasangan kunci dan nilai yang dipisahkan oleh titik dua :
'''
list_farhan = [True, "Python", 100]

my_dict = {
    "nama": "Farhan", # "nama" adalah key
    "usia": 20, # "usia" adalah key
    "kota": "Jakarta", # "kota " adalah key
    "list": list_farhan, # "list" adalah key
}

print(my_dict)

# mengakses item pada dictionary
print(my_dict["nama"]) # harus menggunakan key
print(my_dict["usia"]) # harus menggunakan key
print(my_dict["list"])