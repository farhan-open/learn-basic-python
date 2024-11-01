import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)

print('Silakan masukkan tanggal, bulan, dan tahun lahir Anda')
tanggal = int(input('Tanggal lahir: '))
bulan = int(input('Bulan lahir: '))
tahun = int(input('Tahun lahir: '))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f'Tanggal lahir Anda adalah {tanggal_lahir}')
print(f'Harinya adalah: {tanggal_lahir:%A}') # sintaks %A akan mengambil hari dari sebuah tanggal

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days//365 # umur_hari.days -> hanya mengambil jumlah hari saja
umur_bulan = (umur_hari.days % 365) // 30
print(f'Umur Anda adalah: {umur_tahun} tahun, {umur_bulan} bulan.')  
