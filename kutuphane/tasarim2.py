from tkinter import *  # Tkinter kütüphanesi grafik arayüzler oluşturmayı sağlayan unsurları içeriyor
import veri_islem

def secili_satiri_getir(event):
    global secili_tuple
    index=list1.curselection()[0] # Listbox ta Seçili olan satir indexini alır
    secili_tuple=list1.get(index) # Seçili satırın bilgisin geriye döndürür
    e1.delete(0,END) # Entry i temizler
    e1.insert(END,secili_tuple[1]) #insert metodu Entry e veri yazar
    e2.delete(0,END)
    e2.insert(END,secili_tuple[2])
    e3.delete(0,END)
    e3.insert(END,secili_tuple[3])
    e4.delete(0,END)
    e4.insert(END,secili_tuple[4])

def grn_komut():
    list1.delete(0,END)
    for satir in veri_islem.goster():
        list1.insert(END,satir)

def ara_komut():
    list1.delete(0,END)
    for row in veri_islem.ara(baslik_metni.get(),yazar_metni.get(),yil_metni.get(),isbn_metni.get()):
        list1.insert(END,row)

def ekle_komut():
    veri_islem.ekle(baslik_metni.get(),yazar_metni.get(),yil_metni.get(),isbn_metni.get())
    list1.delete(0,END)
    list1.insert(END,(baslik_metni.get(),yazar_metni.get(),yil_metni.get(),isbn_metni.get()))

def sil_komut():
    veri_islem.sil(secili_tuple[0])

def gncl_komut():
    veri_islem.guncelle(secili_tuple[0],baslik_metni.get(),yazar_metni.get(),yil_metni.get(),isbn_metni.get())

window=Tk()  # Bir pencere oluşturmayı başlatır

window.wm_title("Kütüphane")

l1=Label(window,text="Başlık")
l1.grid(row=0,column=0)

l2=Label(window,text="Yazar")
l2.grid(row=0,column=2)

l3=Label(window,text="Yıl")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

baslik_metni=StringVar()
e1=Entry(window,textvariable=baslik_metni)
e1.grid(row=0,column=1)

yazar_metni=StringVar()
e2=Entry(window,textvariable=yazar_metni)
e2.grid(row=0,column=3)

yil_metni=StringVar()
e3=Entry(window,textvariable=yil_metni)
e3.grid(row=1,column=1)

isbn_metni=StringVar()
e4=Entry(window,textvariable=isbn_metni)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',secili_satiri_getir) # bind metodu ile fonksiyon listbox seçimine bağlanır

b1=Button(window,text="Tüm Kayıtlar", width=12,command=grn_komut)
b1.grid(row=2,column=3)

b2=Button(window,text="Ara ", width=12,command=ara_komut)
b2.grid(row=3,column=3)

b3=Button(window,text="Ekle", width=12,command=ekle_komut)
b3.grid(row=4,column=3)

b4=Button(window,text="Güncelle", width=12,command=gncl_komut)
b4.grid(row=5,column=3)

b5=Button(window,text="Sil", width=12,command=sil_komut)
b5.grid(row=6,column=3)

b6=Button(window,text="Kapat", width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()  # pencere burada sonlanır
