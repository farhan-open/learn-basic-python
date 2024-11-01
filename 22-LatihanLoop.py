# Membuat Segitiga
sisi = 4
count = 0

# 1. Menggunakan For
print('SEGITIGA DENGAN FOR'.center(30, ':'))
for i in range(sisi):
    count += 1
    print('*'*count)

print('Akhir dari For')

# 2. Menggunakan While
print('')
print('SEGITIGA DENGAN WHILE'.center(30, ':'))
sisi = int(input("Masukkan panjang sisi segitiga: "))
count = 0
while True:
    count += 1
    print("*"*count)

    if (count > sisi):
        break

print('Akhir dari While')   

# 3. Mencetak segitiga dengan jumlah bintang pada tiap barisnya adalah ganjil
print('')
print('SEGITIGA GANJIL'.center(30, ':'))
sisi = int(input("Masukkan panjang sisi segitiga: "))
count = 0
while True:
    count += 1

    if (count > sisi):
        break

    if (count % 2): # akan true jika 1, dan akan false jika 0
        print("*"*count)
    else: # jika count-nya genap, kita continue
        continue

print("Segitiga ganjil selesai")

# 4. Membuat segitiga sama kaki
print('')
print('SEGITIGA SAMA KAKI'.center(30, ':'))
sisi = int(input("Masukkan panjang sisi segitiga: "))
spasi = sisi // 2
count = 0
while True:
    count += 1

    if (count > sisi):
        break

    if (count % 2): # akan true jika 1, dan akan false jika 0
        print(" "*spasi + "+"*count)
        spasi -= 1
    else: # jika count-nya genap, kita continue
        continue

print("Segitiga sama kaki selesai")

# 4. Membuat belah ketupat
print('')
print('BELAH KETUPAT'.center(30, ':'))
sisi = int(input("Masukkan panjang sisi belah ketupat: "))
spasi = sisi // 2
count = 0
while True:
    count += 1

    if (count > sisi):
        count -= 2
        spasi = 1
        while True:
            count -= 1
            if (count % 2):
                print(" "*spasi + "+"*count)
                spasi += 1

            if (count == 0):
                break
        
        break

    if (count % 2): # akan true jika 1, dan akan false jika 0
        print(" "*spasi + "+"*count)
        spasi -= 1
    else: # jika count-nya genap, kita continue
        continue

print("Belah ketupat selesai")