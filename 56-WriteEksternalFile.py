# 1. Mode Write (bisa dianalogikan seperti membuat file jika nama filenya tidak ada. Namun jika nama filenya sudah ada, maka perintah yang dijalankan dengan write, akan MENIMPA isi asli dari file yang sudah ada sebelumnya tersebut.)
with open('file_text.txt', mode='w', encoding='utf-8') as file:
    file.write('Ucup Surucup')

# 2. Mode Append (akan menambahkan konten pada file target)
with open('file_text_1.txt', mode='w', encoding='utf-8') as file:
    file.write('Ucup Surucup\n')

with open('file_text_1.txt', mode='a', encoding='utf-8') as file: # mode 'a' untuk append
    file.write('Otong Surotong')

# 3. Mode r+
with open('file_text_2.txt', mode='w', encoding='utf-8') as file: # membuat file_text_2.txt
    file.write('Ini adalah file_text ke-2\n')

with open('file_text_2.txt', mode='r+', encoding='utf-8') as file: # mode ini memungkinkan operasi read dan write. 
    # perintah di bawah ini akan menimpa isi file_text_2.txt yang sudah ada sebelumnya
    file.write('Baris-1\n')
    file.write('Baris-2\n')
    file.write('Baris-3\n')

with open('file_text_2.txt', mode='r+', encoding='utf-8') as file: 
    # membaca isi file_text_2.txt
    data = file.read()
    print(data)

with open('file_text_2.txt', mode='r+', encoding='utf-8') as file: 
    file.write('Otong') # akan menimpa isi text pada baris pertama sesuai dengan panjang data, karena proses write seperti ini akan dijalankan secara berurutan baris per baris dimulai dari baris pertama