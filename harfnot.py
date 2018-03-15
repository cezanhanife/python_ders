def harfNot():
        sn = int(e1_d.get())
        hn = ""
        if sn >= 85 :
            hn = "A"
        elif sn >=70 :
            hn = "B"
        elif sn >= 60:
            hn = "C"
        elif sn >= 50:
            hn = "D"
        elif sn >= 40:
            hn = "DC"
        else :
            hn = "F"
        t1.delete('1.0', END)
        t1.insert(END, hn )


window = Tk()

e1_d = StringVar()
e1 = Entry(window, textvariable = e1_d)
e1.grid(row = 0 , column = 0)

t1 = Text(window, width = 10 , height = 2)
t1.grid(row=0 , column = 1)

b1 = Button(window, text = "Harf Notunu Görüntüle" , command = harfNot)
b1.grid(row=0, column = 2)


window.mainloop()
