data = input("Silakan masukkan data: ") # return value-nya selalu bertipe string
print("Data yang Anda masukkan adalah: ", data, "dengan tipe: ", type(data))

# Jika kita ingin memanipulasi tipe dari return value fungsi string, maka perlu dilakukan type casting
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
tinggi = float(input("Masukkan tinggi badan Anda: "))

print("Nama Anda adalah:", nama, "dengan tipe: ", type(nama))
print("Umur Anda adalah:", umur, "dengan tipe: ", type(umur))
print("Tinggi badan Anda adalah:", tinggi, "cm, dengan tipe: ", type(tinggi))

# Khusus untuk boolean, proses type castingnya perlu dilakukan sebagai berikut:
biner = bool(int(input("Masukkan nilai boolean (1/0):")))
print("Nilai boolean dari data yang anda inputkan adalah", biner, "dengan tipe:", type(biner))
# Proses di atas bertujuan agar proses recognize tipe boolean oleh program bisa berjalan dengan lancar
