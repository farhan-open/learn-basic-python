# Teknik Menduplikat List

a = ['fig', 'apple', 'elderberry', 'grapefruit', 'durian', 'cherry', 'banana']
print(f'a = {a}')

b = a # dengan begini, berarti kita memiliki variabel b yang merujuk ke list yang sama dengan yang dirujuk oleh variabel a
print(f'b = {b}')

print('')
print(f'alamat list a = {hex(id(a))}')
print(f'alamat list b = {hex(id(b))}')

# dengan begitu, apapun yang dilakukan pada list a akan berpengaruh terhadap list b.. begitupun sebaliknya
a[1] = 'watermelon'
print('')
print('Setelah perubahan item di index ke-1'.center(50, '='))
print(f'a = {a}')
print(f'b = {b}')

'''
agar kasus di atas tidak terjadi, kita pperlu melakukan duplikasi list.. karena pada beberapa kondisi mungkin kita akan butuh dua buah variabel list yang isinya sama, namun operasi list yang diberlakukan pada kedua variabel list tersebut harus bersifat saling bebas
'''
c = a.copy() # melakukan duplikasi list
print('')
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}') # variabel list c merujuk ke alamat yang berbeda meskipun isi listnya sama

print('')
print(f'alamat list a = {hex(id(a))}')
print(f'alamat list b = {hex(id(b))}')
print(f'alamat list c = {hex(id(c))}')

c.sort() # sorting pada variabel list c tidak akan berpengaruh terhadap list pada variabel a dan b
print('')
print('Setlah Dilakukan Sorting'.center(50, '='))
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')