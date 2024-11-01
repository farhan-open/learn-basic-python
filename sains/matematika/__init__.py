from . import basic
from . import scientific

# kira juga bisa melakukan import langsung yang mengarah pada fungsi di suatu file eksternal sebagai berikut:
from . basic import tambah, kali # Dengan begini, fungsi tambah dan kali langsung menempel ke folder matematika, sehingga untuk menggunakan fungsinya, tidak perlu menuliskan nama filenya lagi
from . scientific import pangkat # Dengan begini, fungsi pangkat dan kali langsung menempel ke folder matematika sehingga untuk menggunakan fungsinya, tidak perlu menuliskan nama filenya lagi