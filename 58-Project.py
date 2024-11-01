import os
import CRUD as CRUD

if __name__ == '__main__':
    sistem_operasi = os.name

    match sistem_operasi:
        case 'posix': os.system('clear') # untuk mac dan linux
        case 'nt': os.system('cls') # untuk windows

    print('Selamat Datang di Program Perpustakaan Sederhana'.center(60, ':'))
    
    # mengecek database ada atau tidak
    CRUD.init_console()

    while(True):
        match sistem_operasi:
            case 'posix': os.system('clear') # untuk mac dan linux
            case 'nt': os.system('cls') # untuk windows

        print('Selamat Datang di Program Perpustakaan Sederhana'.center(60, ':'))
        print('1. Read Data Buku')
        print('2. Create Data Buku')
        print('3. Update Data Buku')
        print('4. Delete Data Buku')
        print('='*60 + '\n')
        user_option = input('Masukkan pilihan Anda: ')

        match user_option: # match-case ini seperti case pada Pascal
            case '1': CRUD.read_console()
            case '2': CRUD.create_console()
            case '3': CRUD.update_console()
            case '4': CRUD.delete_console()

        is_done = input('Apakah Anda ingin mengakhiri program? (Y/N): ')

        if (is_done == 'Y' or is_done == 'y'):
            print('Terima Kasih karena telah berkunjung..')
            break
        elif (is_done == 'N' or is_done == 'n'):
            pass
        else:
            print('Anda salah memasukkan input, program dihentikan..')
            break
