# alias
from matematik import topla # bir modüldeki belirli bir nesneyi çağırmak için kullanılır
# from matematik import topla as toplamaIslemi # bir modüldeki belirli bir nesneyi çağırmak için kullanılır
# import matematik as mat # matematikde bütün nesneleri fonkları çağırır.
from human import Human
# built-in modules
import random 
#import selenium
from selenium import webdriver

print("Modules")

#print(mat.topla(80,5))
print(topla(80,5))

print(random.randint(0,100))

human1 = Human("Klc")
human1.talk("Merhaba")

# packages
chromedriver = webdriver.Chrome()


