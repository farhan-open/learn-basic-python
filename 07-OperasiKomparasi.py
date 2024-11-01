# operator yang digunakan pada operasi komparasi adalah (<, >, <=, >=, ==, !=, is, dan is not) -> dapat digunakan untuk perbandingan pada sintaks literal

x = 5
y = 10

# Operator Persamaan
print(x == y)  # Output: False
print(x != y)  # Output: True

# Operator Ketidaksamaan
print(x < y)   # Output: True
print(x > y)   # Output: False
print(x <= y)  # Output: True
print(x >= y)  # Output: False

# Operator Pembanding Rentang
list_angka = [1, 2, 3, 4, 5]
print(x in list_angka)    # Output: True
print(y not in list_angka)  # Output: True

# Operator is dan is not

'''
Operator is dan is not adalah operator khusus di Python yang digunakan untuk memeriksa identitas OBJEK (bukan untuk sintaks literal), bukan nilai objeknya. Perbedaan ini penting karena dua objek dapat memiliki nilai yang sama tetapi berbeda secara identitas.Identitas yang dimaksud dapat diakatakan merujuk ke alamat memori yang dijadikan refrensi penyimpanan objek.

Untuk mengetahui identitas atau alamat memori yang menjadi referensi penyimpanan objek, dapat digunakan perintah berikut: id(nama_objek) atau hex(id(nama_bojek))
'''
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("Isi objek x adalah", x, "dengan tipe", type(x), "dan disimpan di alamat memori berikut:", hex(id(x)))
print("Isi objek z adalah", z, "dengan tipe", type(z), "dan disimpan di alamat memori berikut:", hex(id(z)))
print("Isi objek y adalah", y, "dengan tipe", type(y), "dan disimpan di alamat memori berikut:", hex(id(y)))

print(x is y)      # Output: False (x dan y memiliki nilai yang sama tetapi identitas yang berbeda)
print(x is z)      # Output: True (x dan z memiliki nilai yang sama dan identitas yang sama)
print(x is not y)  # Output: True (x dan y memiliki nilai yang sama tetapi identitas yang berbeda)
print(x is not z)  # Output: False (x dan z memiliki nilai yang sama dan identitas yang sama)

