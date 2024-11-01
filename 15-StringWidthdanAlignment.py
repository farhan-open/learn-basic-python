data_nama = 'Farhan'
data_umur = 17
data_tinggi = 170.5
data_sepatu = 42

# Membuat format string multiline (dengan menggunakan enter (\n))
data_string = f"Nama = {data_nama} \nUmur = {data_umur} \nTinggi = {data_tinggi} \nSepatu = {data_sepatu}"
print(5*'=' + 'Data String' +5*'=')
print(data_string)

# Membuat format sttring multiline menggunakan kutip triplets
data_string = f"""Nama = {data_nama}
Umur = {data_umur}
Tinggi = {data_tinggi}
Sepatu = {data_sepatu}
"""
print('\n' + 5*'=' + 'Data String' +5*'=')
print(data_string)

# mengatur alignment string pada formatted string literal
text = "Hello"
print(f"{text:<10}")  # Output: "Hello     " dalam artian akan disediakan space sepanjang 10 karakter untuk string 'Hello' dengan penulisan rata kiri
print(f"{text:>10}")  # Output: "     Hello" dalam artian akan disediakan space sepanjang 10 karakter untuk string 'Hello' dengan penulisan rata kanan
print(f"{text:^10}")  # Output: "  Hello   " dalam artian akan disediakan space sepanjang 10 karakter untuk string 'Hello' dengan penulisan rata tengah

