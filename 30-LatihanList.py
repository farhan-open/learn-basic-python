# Program List Buku
list_buku = []

while True:
    judul = input('Masukkan judul buku: ')
    penulis = input('Masukkan nama penulis: ')

    buku = [judul, penulis]
    list_buku.append(buku)

    print('')
    print('Data Buku'.center(59, ':'))
    print('='*63)
    print('|' + 'No'.center(4) + '|' + 'Judul'.center(40) + '|' + 'Penulis'.center(15) + '|')
    print('='*63)
    for i, b in enumerate(list_buku):
        print('|' + str(i+1).center(4) + '|' + b[0].center(40) + '|' + b[1].center(15) + '|')
        print('-'*63)
    
    print('')
    isLanjut = input('Apakah Anda ingin melakukan input ulang? (Y/N): ')
    if (isLanjut == 'Y' or isLanjut == 'y'):
        print('')
    elif (isLanjut == 'N' or isLanjut == 'n'):
        break
    else:
        print('Anda salah memasukkan input, program dihentikan..')
        break

print('Program Selesai..')