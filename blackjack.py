import random

##Gerekli değişkenler
kartlar = ["Maça As", "Maça İkili", "Maça Üçlü", "Maça Dörtlü", "Maça Beşli", "Maça Altılı", "Maça Yedili", "Maça Sekizli", "Maça Dokuzlu","Maça Onlu", "Maça Papaz", "Maça Vale", "Maça Kız","Karo As", "Karo İkili", "Karo Üçlü", "Karo Dörtlü", "Karo Beşli", "Karo Altılı", "Karo Yedili", "Karo Sekizli", "Karo Dokuzlu","Karo Onlu", "Karo Papaz", "Karo Vale", "Karo Kız", "Sinek As", "Sinek İkili", "Sinek Üçlü", "Sinek Dörtlü", "Sinek Beşli", "Sinek Altılı", "Sinek Yedili", "Sinek Sekizli", "Sinek Dokuzlu","Sinek Onlu", "Sinek Papaz", "Sinek Vale", "Sinek Kız", "Kupa As", "Kupa İkili", "Kupa Üçlü", "Kupa Dörtlü", "Kupa Beşli", "Kupa Altılı", "Kupa Yedili", "Kupa Sekizli", "Kupa Dokuzlu","Kupa Onlu", "Kupa Papaz", "Kupa Vale", "Kupa Kız"];

kasa = []
kullanici = []

##Fonksiyonlar
def kullaniciyaKartVer():       #kullanici listesine kartlar listesinden rastgele eleman seçilip, eklenmesi ve aynı elemanın kartlar listesinden silinmesi, kullanıcıya kart bilgisinin yazdırılması
    rastgeleKart = random.choice(kartlar)

    kullanici.append(rastgeleKart)
    kartlar.remove(rastgeleKart)

    print("\nKullanıcıya kart verildi.")
    print("Kullanıcıya verilen kart:\t{}".format(rastgeleKart))

def kasayaKartVer():            #kasa listesine kartlar listesinden rastgele eleman seçilip, eklenmesi ve aynı elemanın kartlar listesinden silinmesi
    rastgeleKart = random.choice(kartlar)

    kasa.append(rastgeleKart)
    kartlar.remove(rastgeleKart)

    print("\nKasaya kart verildi.\n")

def kasayaKartVerYazdir():      #kasa listesine kartlar listesinden rastgele eleman seçilip, eklenmesi ve aynı elemanın kartlar listesinden silinmesi, kasa kart bilgisinin yazdırılması
    rastgeleKart = random.choice(kartlar)

    kasa.append(rastgeleKart)     #Kasa listesinin içerisine kartlar listesinden rastgele bir değer atar
    kartlar.remove(rastgeleKart)     #Kasa listesine eklenen elemanı kartlar listesinden kaldırma

    print("\nKasaya kart verildi.")
    print("Kasaya verilen kart:\t{}".format(rastgeleKart))


##Uygulama
kullaniciyaKartVer()

#Tek seferlik kasaya verilen gösterilen kart
temp = random.choice(kartlar)
kasa.append(temp)
kartlar.remove(temp)
#end

print("\nKasaya kart verildi.\nKasaya verilen ilk kart:\t{}".format(temp))

kullaniciyaKartVer()
kasayaKartVer()


print("Kullanıcının kartları: ",kullanici, "\n")
print("Kasanın görünen kartı: ",kasa[0], "\n")

while(True):

    kullaniciSoru = int(input("1) Kart Çek\n2) Stand ve Kasaya Kart Çek\n0) Çıkış Yap\nSeçiminiz:\t"))

    if (kullaniciSoru == 1):
        kullaniciyaKartVer()
        print("\n",kullanici, "\n")

    elif (kullaniciSoru == 2 ):
        kasayaKartVerYazdir()

        print("\nKartlarınız: ", kullanici)
        print("\nKasanın kartları: ",kasa, "\n")

    elif (kullaniciSoru == 0):
        print("\nÇıkış yapılıyor")
        break

    else:
        print("\nYanlış seçim yaptınız. Tekrar deneyiniz...")


##