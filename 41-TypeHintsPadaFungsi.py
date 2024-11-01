'''
Type hints adalah fitur pada Python yang memungkinkan Anda menambahkan anotasi tipe data pada deklarasi parameter fungsi, nilai kembali fungsi, dan variabel. Dengan menggunakan type hints, Anda dapat menyatakan tipe data yang diharapkan untuk setiap variabel atau parameter, sehingga memudahkan pembacaan kode dan memberikan informasi lebih jelas tentang tipe data yang diharapkan pada saat penggunaan.
'''

# contoh penggunaan type hints
def sepuluh_pangkat(argument: int) -> int : # menandai bahwa argumen tipe pada fungsi sepuluh_pangkat adalah integer kemudian tanda '->' menandakan tipe dari nilai return dari fungsi sepuluh_pangkat yang dalam hal ini adalah int
    '''Fungsi dengan Hints'''
    hasil = 10 ** argument
    return hasil

print(sepuluh_pangkat(5))