# Kondisi 1 -----0+++++5-----8+++++11-----

inputUser = int(input("Masukkan angka:"))

isLebihDari0 = inputUser > 0
isKurangDari5 = inputUser < 5
isLebihDari8 = inputUser > 8
isKurangDari11 = inputUser < 11

hasilAkhir = (isLebihDari0 and isKurangDari5) or (isLebihDari8 and isKurangDari11)
print("Angka yang Anda masukkan menghasilkan nilai kebenaran berikut:", hasilAkhir)

print("\n", 10*"=", "\n")

# Kondisi 2 +++++0-----5+++++8-----11+++++

inputUser = int(input("Masukkan angka:"))

isLebihDari0 = inputUser > 0
isKurangDari5 = inputUser < 5
isLebihDari8 = inputUser > 8
isKurangDari11 = inputUser < 11

hasilAkhir = not((isLebihDari0 and isKurangDari5) or (isLebihDari8 and isKurangDari11))
print("Angka yang Anda masukkan menghasilkan nilai kebenaran berikut:", hasilAkhir)