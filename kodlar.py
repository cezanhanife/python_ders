def fakt(n):
    f = 1
    for s in range(1,n+1):  # range(1,10) - 1 , 2, 3 , 4... 9
        f *= s
    return f

#print(fakt(5))

def fakt2(n):
    if(n == 1):
        return 1
    return n * fakt2(n-1)

print(fakt2(10))

class Arac:
    renk = ""
    vites = 6
    tur = "binek"
    marka = ""

    def bilgiYaz(self):
        print("Aracın rengi : %s vites sayısı : %d türü :%s"
             + "markası :%s " %(
        self.renk,self.vites,self.tur,self.marka))


a1 = Arac()
a1.renk = "Siyah"
a1.marka = "bmw"
a2 = Arac()
a2.marka = "honda"

a1.bilgiYaz()
a2.bilgiYaz()

rehber = {
    "Ahmet Tekin" : "054587866",  # anahtar , deger
    "Hakan can" : "055578663",
    "Ayşe Melek" : "0532111166",
    "Zeynep Güngör" : "054454566",
    "Hasan Baleş" : "054582323",
}   #json

print(rehber)
print(rehber['Hakan can'])

for ad,tel in rehber.items():
    print("Ad Soyad : %s , Tel : %s" % (ad,tel))

del rehber['Zeynep Güngör']

print('********************')

for ad,tel in rehber.items():
    print("Ad Soyad : %s , Tel : %s" % (ad,tel))


ogrenciler = {
    '121551551' : [{"bölüm":"bilgisayar"}, {"kredi": 85}],
    '343551551' : [{"bölüm":"orman"}, {"kredi": 100}],
    '134451551' : [{"bölüm":"mobilya"}, {"kredi": 110}]
}

print(ogrenciler)
print(ogrenciler['343551551'])
print(ogrenciler['134451551'][0])
print(ogrenciler['134451551'][0]['bölüm'])
ogrenciler.pop('343551551')
print(ogrenciler)

print(ogrenciler['134451551'][1])

import urllib
dir(urllib)
help(urllib)



import numpy as np

boy = [1.85, 1.77, 1.72, 1.90, 1.50]
kilo = [80, 82, 76, 85, 55]

boy_dizi = np.array(boy)
kilo_dizi = np.array(kilo)

bmi = kilo_dizi/ boy_dizi ** 2

print(boy_dizi)
print(kilo_dizi)
print(bmi)

print(bmi[bmi < 24])

import urllib.request
response = urllib.request.urlopen('http://omu.edu.tr/tr')
html = response.read()
print(html)
