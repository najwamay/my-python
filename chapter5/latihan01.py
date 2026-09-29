"""
Write a python code, to determine whether a number of year is a leap year or not

Example:
(input) Enter a year: 2000
(output) Year 2000 is a leap year 
(input) Enter a year: 2001
(output) Year 2001 is not a leap year
"""

# Menginput Tahun
tahun = int(input("Tulis Sebuah Tahun: "))
 
#Perulangan Pertama
if (tahun % 4) == 0:
 
   #Perulangan Kedua
   if (tahun % 100) == 0:
 
       #Perulangan Ketiga
       if (tahun % 400) == 0:
 
           #Tergolong Tahun Kabisat
           print("{0} adalah Tahun Kabisat".format(tahun))
 
       #Bukan Tergolong Tahun Kabisat
       else:
           print("{0} bukan Tahun Kabisat".format(tahun))
 
   #Tergolong Tahun Kabisat
   else:
       print("{0} adalah Tahun Kabisat".format(tahun))
 
#Bukan Tergolong Tahun Kabisat
else:
   print("{0} bukan Tahun Kabisat".format(tahun))