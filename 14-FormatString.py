'''
Format string pada Python adalah teknik yang digunakan untuk memasukkan nilai ke dalam string dengan cara yang lebih fleksibel. Dengan format string, Anda dapat memasukkan variabel, ekspresi, atau nilai lain ke dalam string dengan menggabungkan mereka menggunakan tanda kurung kurawal {} sebagai segmen tempat penempatan nilai. 
'''
# contoh:
name = "John"
age = 30
height = 175.5

result = f"My name is {name}, I am {age} years old, and my height is {height} cm."
print(result)

# untuk tipe data boolean
bool = True
formatStr= f"Boolean = {bool}"
print(formatStr)

# kasus khusus: membuat format string hanya menerima masukan bilangan integer
angka = 15
formatStr = f"Bilangan bulat yang dimasukkan adalah: {angka:d}" #kode ':d' membuat format string di samping hanya menerima masukan angka yang bertipe integer
print(formatStr)

# kasus khusus: membuat format string menampilkan bilangan dengan ordo ribuan
angka = 2000
formatStr = f"Bilangan bulat yang dimasukkan adalah: {angka:,}" #kode ':,' membuat format string menambahkan tanda ',' pada tiap ordo ribuan
print(formatStr)

angka = 2000000000000
formatStr = f"Bilangan bulat yang dimasukkan adalah: {angka:,}" #kode ':,' membuat format string menambahkan tanda ',' pada tiap ordo ribuan
print(formatStr)

# mengatur jumlah angka di belakang koma khusus untuk bilangan dengan tipe float
number = 123.45678

result = f"The number is: {number:.2f}" #mengatur agar yang ditampilkan hanya dua angka di belakang koma
print(result)  # Output: The number is: 123.46

result = f"The number is: {number:10.2f}"
print(result)  # Output: The number is:     123.46 [10.2f digunakan untuk memformat bilangan dengan dua digit desimal dalam lebar tampilan sepuluh karakter dengan penyesuaian ke kanan.]

# menampilkan leading zero
result = f"The number is: {number:010.2f}" # [010.2f digunakan untuk memformat bilangan dengan dua digit desimal dalam lebar tampilan sepuluh karakter dengan penyesuaian ke kanan dan karakter-karakter awal diisi dengan 0.]
print(result)

# memformat persentase
persentase = 0.045
format_persen = f"Persen = {persentase:.2%}" # menampilkan persentase dengan dua angka di belakang koma
print(format_persen)

# melakukan operasi aritmatika di dalam tanda kurung kurawal
harga = 10000
jumlah = 5

format_string = f"Harga total = Rp. {harga*jumlah:,}"
print(format_string)

# formar angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"Format binary dari {angka} = {bin(angka)}"
format_oktal = f"Format oktal dari {angka} = {oct(angka)}"
format_hex = f"Format hex dari {angka} = {hex(angka)}"

print(format_binary)
print(format_oktal)
print(format_hex)