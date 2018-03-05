from difflib import get_close_matches


liste = ["elma","elmalık","elmacı","armut","armutcu","kalem"]
sozluk = {"kalem":["yazı yazar","çizer","rengi var"], "kalemlik": "kalem konur",
          "kalemci":"kalem satar","kagit":"yazılır"}

k = "armu"
s = get_close_matches(k,liste)

k2 = "kalek"
s2 = get_close_matches(k2,sozluk.keys())

if len(s2):
    for i in range(len(s2)):
        print (s2[i] + " : " + str(sozluk[s2[i]]))

print(s)
