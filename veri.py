import sqlite3

def create_table():
    bag = sqlite3.connect("deneme.db")
    cur = bag.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS urunler(uad TEXT, miktar INT, fiyat REAL)")
    bag.commit()
    bag.close()

def insert(ad,mk,fyt):
    bag = sqlite3.connect("deneme.db")
    cur = bag.cursor()
    cur.execute("INSERT INTO urunler VALUES(?,?,?)",(ad,mk,fyt))
    bag.commit()
    bag.close()

def goruntule():
    bag = sqlite3.connect("deneme.db")
    cur = bag.cursor()
    cur.execute("SELECT * FROM urunler")
    tablo = cur.fetchall()
    bag.close()
    return tablo


def sil(ad):
    bag = sqlite3.connect("deneme.db")
    cur = bag.cursor()
    cur.execute("DELETE FROM urunler WHERE uad = ?",(ad,))
    bag.commit()
    bag.close()

def guncelle(ad,mk,fyt):
    bag = sqlite3.connect("deneme.db")
    cur = bag.cursor()
    cur.execute("UPDATE urunler SET miktar = ? , fiyat = ? WHERE uad = ? ",(mk,fyt,ad))
    bag.commit()
    bag.close()

#insert('iphoneX',10, 4999.0)
#insert('S9',50, 3999.0)
#insert('Sony Xperia', 100, 3200.0)
#insert('LG',30, 2547.0)

#print(goruntule())
#guncelle('LG',25,2600.0)
#print(goruntule())

sil('Kalemlik')
print(goruntule())
