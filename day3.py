from human import Human


print("3.Gün")

# classlar => sınıflar
# modules
# paket yönetme 
# argument=parametre
# self = this 


# instance => Örnek

human1 = Human("Ahmet")
# human1.name = "Berk"
human1.talk("Merhaba")
human1.walk()
print(human1)


human2 = Human("Berk")
# human2.name = "Ahmet"
human2.talk("Selam")
human2.walk()
print(human2)

print("*****")
Human("Berk").walk() # bu şekildede değişkene atamdan kullanılabilir.
print("*****")



