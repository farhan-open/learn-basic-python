from . import Operasi

DB_NAME = 'project.txt'
TEMPLATE = {
    'pk': 'XXXXXX',
    'date_add': 'yyyy-mm-dd',
    'judul': ' '*255,
    'penulis': ' '*255,
    'tahun': 'yyyy'
}

def init_console(): 
    try:
        with open(DB_NAME, mode='r') as file:
            print('Database tersedia')
    except:
        print('Database tidak ditemukan, membuat database baru..')
        Operasi.create_first_data()
            