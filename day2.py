print("2.Gün")

faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"

print(type(vade))
print(type(krediAdi))
print(type(faiz))

print("----------------------------------------------------------------------------")
# tip dönüşümü
faiz = str(faiz)
print(type(faiz))

# inputta veri tipi default olarak string
vade = 24  # int(input("Faiz Miktarı Giriniz: "))
print(type(vade))
vade = vade + 12

# print(int(vade + 12))
print("----------------------------------------------------------------------------")

# string interpolation (farklı türden veya aynı türde olan verileri birleştirirken kullanırız )
# Seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade : " + str(vade))
print("!!! Seçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi}" .format(
    vadeSayisi=vade))

# isim = input("Lütfen İsminizi Giriniz: ")
isim = "Berk"
metin = "Merhaba {name}" .format(name=isim)
print(metin)

# f-string
metin = f"Hoşgeldiniz {isim}"
print(metin)

print("----------------------------------------------------------------------------")
# listeler
# döngüler

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))
print(krediler)
print(len(krediler))  # lenght

dizi = ["İhtiyaç Kredisi", 15, 65, 45.2, True] # farklı türde verileride dizide bulunabilir
# print(dizi)
# print(dizi[0])

krediler.append("Özel Krediler")
print(krediler)

krediler.append("X kredisi")
print(krediler)

krediler.pop(0) # default olarak -1. indeksi alıyor oda son indeksteki değeri siler
print(krediler)

krediler.append("Taşıt Kredisi") 
print(krediler)
krediler.remove("Taşıt Kredisi") # bu değerde bulduğu ilk elemanı siler
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"]) # diziye birden fazla değer eklemek için kullanılır.
print(krediler)

print("----------------------------------------------------------------------------")
# Döngüler
# for 
# i=0 i<10 condition (şart) olacak 
# for i in range(10):
#     print(i)

for i in range(10):
    print(i)
print("**************")
for i in range(5,11):
    print(i)
print("**************")
for i in range(0,51,10): # 3.eleman kaça kaçar artacağını belirttiğimiz kısım
    print(i)
print("**************")
#for i in range(0.1,0.5): int olacak hata verir
    #print(i)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]

for kredi in krediler:
    print(kredi)
print("**************")
# yukarıdaki ile aynı şey
for i in range(len(krediler)): 
    print(krediler[i])

# while (sonsuz döngü)
# while True:
#     print("x")

i=0
while i < 10:
    print("x")
    #i = i + 1
    i +=1
print("y")    
print("**************")

while True:
    print("x")
    break
print("***********")
print("son döngü")
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
i = 0
while i < len(krediler):
    i +=1
    print(i)
    print(krediler[i])
    if krediler[i] ==  "Konut Kredisi":
        break

print("***********")  
# fonksiyonlar
# definition define

def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(100,80)
calculateWithParams(150,70)
sayHello("Mehmet")
sayHello("Berk")

def calculateAndReturn(price, discount):
    return price-discount

yeniFiyat = calculateAndReturn(200,50)
print("Yeni Fiyat =" , yeniFiyat)

#void
def calculatePrice(price, discount):
    print(price-discount)

def calculatePriceAndReturn(price, discount):
    return price-discount

print("*********")    
fonk1 = calculatePrice(100,50)    
fonk2 = calculatePriceAndReturn(300,100)
print(f"157.Satır =  {fonk1}")
print(f"157.Satır =  {fonk2}")
print("*********")