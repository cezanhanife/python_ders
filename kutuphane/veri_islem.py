import sqlite3

def baglan():
    conn=sqlite3.connect("kitap.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS kitaplar (id INTEGER PRIMARY KEY, baslik text, yazar text, yil integer, isbn text)")
    conn.commit()
    conn.close()

def ekle(baslik,yazar,yil,isbn):
    conn=sqlite3.connect("kitap.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO kitaplar VALUES (NULL,?,?,?,?)",(baslik,yazar,yil,isbn))
    conn.commit()
    conn.close()
    #goster()

def goster():
    conn=sqlite3.connect("kitap.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM kitaplar")
    tablo=cur.fetchall()  # bütün kayıtları yakalar
    conn.close()
    return tablo

def ara(baslik="",yazar="",yil="",isbn=""):
    conn=sqlite3.connect("kitap.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM kitaplar WHERE baslik = ? OR yazar LIKE ? OR yil=? OR isbn=?",
     (baslik,'%'+yazar+'%',yil,isbn))
    arananlar=cur.fetchall() # aranan bütün kayıtları yakalar
    conn.close()
    return arananlar

def sil(id):
    conn=sqlite3.connect("kitap.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM kitaplar WHERE id=?",(id,))
    conn.commit()
    conn.close()

def guncelle(id,baslik,yazar,yil,isbn):
    conn=sqlite3.connect("kitap.db")
    cur=conn.cursor()
    cur.execute("UPDATE kitaplar SET baslik=?, yazar=?, yil=?, isbn=? WHERE id=?",
    (baslik,yazar,yil,isbn,id))
    conn.commit()
    conn.close()

baglan()
#ekle("Sabah Uykum","Ahmet Batman",1918,91312)
#ekle("Osho","Özgürlük",2000,121212)
#ekle("Da Vinci Şifresi","Dan Brown",2001,225312)
#ekle("Bir Dinazorun Anıları","Mina Urgan",2003,94412)
#ekle("Babı Esrar","Ahmet Ümit",2005,855512)
#ekle("Tekin Seyri","Ahmet Hulusi",2006,11112)

#print(goster())
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))
