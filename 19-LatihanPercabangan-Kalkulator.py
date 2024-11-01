# KALULATOR SEDERHANA

judul = 'KALKULATOR SEDERHANA'.center(30, '=')
print(judul)

angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, x, /): ")
angka2 = float(input("Masukkan angka kedua: "))

if (operator == "+"):
    hasil = angka1 + angka2
    print(f"Hasil dari {angka1} + {angka2} = {hasil}")
elif (operator == "-"):
    hasil = angka1 - angka2
    print(f"Hasil dari {angka1} - {angka2} = {hasil}")
elif (operator == "x"):
    hasil = angka1 * angka2
    print(f"Hasil dari {angka1} x {angka2} = {hasil}")
elif (operator == "/"):
    hasil = angka1 / angka2
    print(f"Hasil dari {angka1} / {angka2} = {hasil}")
else:
    print("Anda salah memasukkan operator")