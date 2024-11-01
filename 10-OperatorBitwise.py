# Operator bitwise (operasi biner)

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n==========OR==========')
print('Nilai:', a, ' , binary:', format(a, '08b'))
print('Nilai:', b, ' , binary:', format(b, '08b'))
print('---------------------------------------- (|)')
print('Nilai:', c, ', binary:', format(c,'08b'))

# bitwise AND (&)
c = a & b
print('\n==========AND==========')
print('Nilai:', a, ', binary:', format(a, '08b'))
print('Nilai:', b, ', binary:', format(b, '08b'))
print('---------------------------------------- (&)')
print('Nilai:', c, ', binary:', format(c,'08b'))

# bitwise XOR (^)
c = a ^ b
print('\n==========XOR==========')
print('Nilai:', a, ' , binary:', format(a, '08b'))
print('Nilai:', b, ' , binary:', format(b, '08b'))
print('---------------------------------------- (^)')
print('Nilai:', c, ', binary:', format(c,'08b'))

# bitwise NOT (~)
c = ~b
print('\n==========OR==========')
print('Nilai:', a, '  , binary:', format(a, '08b'))
print('---------------------------------------- (~)')
print('Nilai:', c, ', binary:', format(c,'08b'))

# SHIFTING

# shifting kanan (>>)
c = a >> 2 # setiap bit akan digeser ke kanan sebanyak dua kali
print('\n==========SHIFTING KANAN==========')
print('Nilai:', a, '  , binary:', format(a, '08b'))
print('---------------------------------------- (>>)')
print('Nilai:', c, ', binary:', format(c,'08b')) 

# shifting kiri (<<)
c = b << 2 # setiap bit akan digeser ke kiri sebanyak dua kali
print('\n==========SHIFTING KIRI==========')
print('Nilai:', b, '  , binary:', format(b, '08b'))
print('---------------------------------------- (>>)')
print('Nilai:', c, ', binary:', format(c,'08b')) 