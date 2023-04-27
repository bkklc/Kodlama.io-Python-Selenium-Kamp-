
print("Kodlama io")

baslik = "Taşıt Kredisi - Araç Kredisi"
print(baslik)

# string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)

# int, inteeger => sayısal ifade
vade = 36
ekvade = 6

# float, decimal, double
aylikOdeme = 200.50

# bool, boolean => true, false
yukselisteMi = False

# matematiksel(aritmetik) operatörler
# +
print(5+5)
print(vade + 12)
print(vade + ekvade)

# -
print(5 - 5)
print(vade - 25)

# *
print(vade * 5)

# /
print(vade / 4)

yeniVade = vade/2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operator (mod alma)
print(10 % 2)
print(vade % 5)

# mantıksal opeatörler
print(1 == 1)
print(1 == 2)

print(1 < 2)
print(3 > 1)
print(1 >= 1)
print(1 <= 1)

print(1 != 2)
print(2 != 2)

# or (veya) and (ve)
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)
print(1 > 2 and 5 > 2 and 3 > 2)

# karar yapıları (condition)
# if elif else (if else if else)


sayi1 = 10
sayi2 = 20

# sayi 1 sayi2 den büyükse ekrana sayi 1 daha büyüktür yaz

if sayi1 > sayi2:

    print("Sayi1 Sayi2 den büyüktür")


elif sayi1 == sayi2:
    print("Sayi1 Sayi2 ye eşittir")


else:
    print("Sayi1 Sayi2 den küçüktür")

print("İf bloğunun dışı")
