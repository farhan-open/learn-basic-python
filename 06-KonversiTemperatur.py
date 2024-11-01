print("PROGRAM KONVERSI TEMPERATUR\n")
print("===========================")

# celcius
celcius = float(input("Masukkan suhu dalam celcius: "))
print("Suhu yang Anda masukkan adalah", celcius, "derajat celcius")

# reamur
reamur = (4/5)*celcius
print("Suhu yang Anda masukkan dalam reamur adalah", reamur, "derajat reamur")

# fahrenheit
fahrenheit = (9/5)*celcius+32
print("Suhu yang Anda masukkan dalam fahrenheit adalah", fahrenheit, "derajat fahrenheit")

# kelvin
kelvin = celcius+273
print("Suhu yang Anda masukkan dalam kelvin adalah", kelvin, "derajat kelvin")