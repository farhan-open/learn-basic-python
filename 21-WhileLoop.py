'''
Sintaks Dasar:

while kondisi:
    # Blok kode yang akan diulang

Kondisi:
    Kondisi adalah ekspresi boolean yang dievaluasi sebelum setiap iterasi. Jika kondisi bernilai True, blok kode dalam while loop akan dieksekusi. Jika kondisi bernilai False, while loop akan berhenti dan eksekusi dilanjutkan ke baris berikutnya setelah while loop.

Blok kode yang diulang:
    Blok kode yang diulang adalah blok kode yang terkait dengan while loop, dan akan dijalankan selama kondisi yang diberikan bernilai True.
    Blok kode tersebut biasanya diberi indentasi dengan empat spasi atau satu tab.

Penghentian while loop:
    Untuk menghindari terjadinya perulangan tak terbatas, pastikan bahwa ada perubahan dalam kondisi yang mengarah pada kondisi menjadi False.
    Anda dapat menggunakan pernyataan break untuk menghentikan while loop secara paksa berdasarkan kondisi tertentu.
'''

# Contoh:
count = 0

while (count < 5):
    print(f"Nilai count sekarang adalah {count}")
    count += 1

# Penggunaan continue, pass, dan break

'''
1. PASS
- Pernyataan pass adalah pernyataan yang tidak melakukan apa pun. Ia digunakan sebagai placeholder atau tanda bahwa suatu blok kode diperlukan secara sintaksis, tetapi tidak ada tindakan yang harus dilakukan saat ini.

- Saat pernyataan pass dieksekusi, tidak ada tindakan yang diambil, dan eksekusi melanjutkan ke pernyataan berikutnya.

- Pernyataan pass berguna saat Anda ingin menulis struktur pengendalian atau fungsi yang masih kosong, tetapi ingin menghindari kesalahan sintaksis.
'''
print('')
print('PASS'.center(35, '='))
angka = 0
while (angka < 5):
    angka += 1

    if angka == 3:
        pass # ini tidak akan dieksekusi

    print(f"Nilai angka sekarang adalah {angka}")

'''
2. CONTINUE
- Pernyataan continue digunakan dalam loop (baik for loop maupun while loop) untuk melanjutkan ke iterasi berikutnya secara paksa, tanpa menjalankan sisa blok kode dalam iterasi saat ini.

- Saat pernyataan continue dieksekusi, semua kode di bawahnya dalam iterasi saat ini akan diabaikan, dan iterasi berikutnya akan dimulai.

- Pernyataan continue berguna ketika Anda ingin mengabaikan sisa blok kode dalam iterasi saat ini berdasarkan kondisi tertentu, dan melanjutkan ke iterasi berikutnya.
'''
print('')
print('CONTINUE DENGAN WHILE LOOP'.center(35, '='))
angka = 0
while (angka < 5):
    angka += 1
    print(f"Nilai angka sekarang adalah {angka}")
    print('CEKPOINT A')

    if (angka == 3):
        continue

    print('CEKPOINT B')

print('')
print('CONTINUE DENGAN FOR LOOP'.center(35, '='))
for i in range(5):
    if i == 2:
        continue
    print(i)

'''
3. BREAK
- Pernyataan break digunakan dalam loop (baik for loop maupun while loop) untuk menghentikan eksekusi loop secara paksa berdasarkan kondisi tertentu.

- Saat pernyataan break dieksekusi, eksekusi loop akan langsung keluar dari loop, dan program melanjutkan eksekusi dari baris berikutnya setelah loop.

- Pernyataan break berguna ketika Anda ingin menghentikan loop secara paksa berdasarkan kondisi tertentu, dan keluar dari loop sebelum mencapai akhir iterasi yang normal.
'''
print('')
print('BREAK DENGAN FOR LOOP'.center(35, '='))
for j in range(5):
    if j == 2:
        break
    print(j)

print('')
print('BREAK DENGAN WHILE LOOP'.center(35, '='))
angka = 0
while (angka < 5):
    angka += 1
    print(f"Nilai angka sekarang adalah {angka}")

    if (angka == 3):
        print('Stop!')
        break

    print('CEKPOINT')

print('Akhir dari program')

