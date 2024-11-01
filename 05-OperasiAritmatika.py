a = 10
b = 3

# operasi penjumlahan +
hasil = a + b
print(a, "+", b, "=", hasil)

# operasi pengurangan -
hasil = a - b
print(a, "-", b, "=", hasil)

# operasi perkalian *
hasil = a * b
print(a, "x", b, "=", hasil)

# operasi pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)

# operasi eksponen/pangkat **
hasil = a ** b
print(a, "pangkat", b, "=", hasil)

# operasi modulus %
hasil = a % b
print(a, "%", b, "=", hasil)

# operasi floor division (pembulatan hasil pembagian) //
hasil = a // b
print(a, "//", b, "=", hasil)

# prioritas operasi
'''
Urutan prioritas operasi pada python adalah sebagai berikut:
1. ()
2. eksponen **
3. perkalian *, pembagian /, modulus %, floor division //
4. penjumlahan + dan pengurangan -
'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,"**",y,"*","(",z,"+",x,")","/",y,"-",y,"%",z,"//",x, "=", hasil)