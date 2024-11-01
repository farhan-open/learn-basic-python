# Operator AND (selalu bernilai FALSE, kecuali jika kedua kondisi yang disyaratkan bernilai TRUE)

x = 5
y = 10

result = (x > 0) and (y < 20)
print(result)  # Output: True

# Operator OR (selalu bernilai TRUE, kecuali jika kedua kondisi yang disyaratkan bernilai FALSE)

x = 5
y = 10

result = (x > 0) or (y > 20)
print(result)  # Output: True

# Operator NOT (negasi)

x = 5

result = not (x > 0)
print(result)  # Output: False

# Operator XOR (pada python disimbolkan dengan '^')

'''
Operator ini hanya berlaku untuk operand dengan nilai kebenaran (boolean).
Jika salah satu operand bernilai True dan yang lainnya bernilai False, maka hasilnya adalah True.
Jika kedua operand memiliki nilai kebenaran yang sama (baik keduanya True atau False), maka hasilnya adalah False.
'''

x = True
y = False

result = x ^ y
print(result)  # Output: True

# PRIORITAS EKSEKUSI/EVALUASI
'''
Operator not dievaluasi terlebih dahulu, diikuti oleh operator and, dan operator or dievaluasi terakhir.
Namun, Anda dapat menggunakan tanda kurung untuk mengatur urutan evaluasi yang diinginkan.
'''

