import json
from difflib import get_close_matches

dosya = json.load(open('sozluk.json', mode='r', encoding="utf-8"))

def bul(k):
    k = k.lower()
    if k in dosya:
        return dosya[k]
    elif len(get_close_matches(k, dosya.keys()))>0:
                eh = input("Aradığınız kelime : %s ise e ye değilse h ye basınız  : " % get_close_matches(k, dosya.keys())[0])
                if(eh == "e"):
                    return dosya[get_close_matches(k, dosya.keys())[0]]
                else:
                    return "Aradığınız Kelime Bulunamadı"
    else :
        if k != "q":
            return "Aradığınız Kelime Bulunamadı"
        else:
            return "Hoşçakalın"


print("Bir İngilizce Kelime Giriniz Çıkmak için q ya basınız: ")

kelime = ""
while kelime != "q":
    kelime = input("Kelime : ")
    sonuc = bul(kelime)
    if type(sonuc) == list:
        for s in sonuc:
            print (s)
    else:
        print(sonuc)
