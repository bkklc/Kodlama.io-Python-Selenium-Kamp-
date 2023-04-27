
class Human:
    # built-in
    # constructor
    # initialize
    # yapıcı blok
    def __init__(self,name) -> None: 
        self.name = name # init fonsiyonuna name parametresi eklendiğinde çalışır
        # self.name = input("Lütfen bir isim giriniz: ") # name parametresi kullanıcıdan girdi ile de istenebilir
        print("Bir human instance 'i üretildi.")
    def __str__(self) :
        return f"STR fonksiyonundan dönen değer: {self.name}"
    
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")        
    def walk(self):
        print(f"{self.name} is walking..")
    