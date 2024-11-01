# IMPLISIT CASTING
x = 5
y = 20.3
hasil_jumlah = x + y # x secara implisit dikonversi menjadi float
print("Hasil jumlah = ", hasil_jumlah, "dengan tipe: ", type(hasil_jumlah))

#EKSPLISIT CASTING
print("======TIPE DATA AWAL INTEGER======")
data_int1 = 9
print("Data = ", data_int1, "dengan tipe: ", type(data_int1))

data_float1 = float(data_int1)
data_str1 = str(data_int1)
data_bool1 = bool(data_int1) # selalu bernilai 'True' kecuali jika data int bernilai 0

print("Data = ", data_float1, "dengan tipe: ", type(data_float1))
print("Data = ", data_str1, "dengan tipe: ", type(data_str1))
print("Data = ", data_bool1, "dengan tipe: ", type(data_bool1))

print("======TIPE DATA AWAL FLOAT======")
data_float2 = 9.7
print("Data = ", data_float2, "dengan tipe: ", type(data_float2))

data_int2 = int(data_float2) # akan dilakukan pembulatan ke bawah
data_str2 = str(data_float2)
data_bool2 = bool(data_float2) # selalu bernilai 'True' kecuali jika data float bernilai 0

print("Data = ", data_int2, "dengan tipe: ", type(data_int2))
print("Data = ", data_str2, "dengan tipe: ", type(data_str2))
print("Data = ", data_bool2, "dengan tipe: ", type(data_bool2))

print("======TIPE DATA AWAL BOOLEAN======")
data_bool3 = True
print("Data = ", data_bool3, "dengan tipe: ", type(data_bool3))

data_int3 = int(data_bool3) 
data_str3 = str(data_bool3)
data_float3 = float(data_bool3) 

print("Data = ", data_int3, "dengan tipe: ", type(data_int3))
print("Data = ", data_str3, "dengan tipe: ", type(data_str3))
print("Data = ", data_float3, "dengan tipe: ", type(data_float3))

print("======TIPE DATA AWAL STRING======")
data_str4 = "10"
print("Data = ", data_str4, "dengan tipe: ", type(data_str4))

data_int4 = int(data_str4) # dapat berjalan jika isi data string berupa angka
data_bool4 = bool(data_str4) # false jika string kosong
data_float4 = float(data_str4) # dapat berjalan jika isi data string berupa angka

print("Data = ", data_int4, "dengan tipe: ", type(data_int4))
print("Data = ", data_bool4, "dengan tipe: ", type(data_bool4))
print("Data = ", data_float4, "dengan tipe: ", type(data_float4))