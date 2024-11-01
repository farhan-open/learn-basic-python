import numpy as np

# membuat vektor

vektor_a = np.array([1, 2, 4, 7]) 

print(f'Vektor: {vektor_a}')
print(f'Vektorkuadrat: {vektor_a**2}')


# Membuat matriks 2x3 menggunakan NumPy
matriks = np.array([[1, 2, 3],
                    [4, 5, 6]])

print(f'Matriks:\n{matriks}')

matriks_kuadrat = matriks**2

print(f'Matriks:\n{matriks_kuadrat}')

# operasi penjumlahan matriks
jumlah_matriks = matriks + matriks_kuadrat

print(f'Hasil penjumlahan matriks:\n{jumlah_matriks}')