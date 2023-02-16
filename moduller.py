#############################################
#                                           #
#       kütüphane otomasyon sistemi         #
#                                           #
#           yapımcı bilgileri               #
#           github - gladyotr               #
#           instagram - @gladbey            #
#           gmail - gladyotr123@gmail.com   #
#                                           #
#               berat karaca <3             #
#############################################



from tkinter import *
from data import *
import time

def eklebt():
    def kitapeklebt():
        ad = isim.get()
        book = kitap.get()
        tarih = time.asctime()
        ekle(ad,book,tarih)
        print(data)
        ekle1= Label(pencereekle)
        ekle1.config(text="{}, isimli kişi sisteme eklendi!".format(ad),fg="green",bg="black",font=("Arial",15))
        ekle1.place(x=100,y=50)
    
    print("eklendi")
    pencereekle=Tk()
    pencereekle.title("kayıt ekle!")
    pencereekle.configure(background="black")
    pencereekle.geometry("500x500+100+200")

    isim = Entry(pencereekle)
    isim.place(x=200,y=100)

    kitap = Entry(pencereekle)
    kitap.place(x=200,y=150)

    kitapekle = Button(pencereekle)
    kitapekle.config(text="sisteme ekle", bg="grey", fg="white", height= 3, width=15,command=kitapeklebt)
    kitapekle.place(x=200,y=250)
    
    

def silbt():
    def sistemsilbt():
        ad = isim.get()
        sil(ad)
        print(data)
        sil1= Label(penceresil)
        sil1.config(text="{}, isimli kişi sistemden silindi!".format(ad),fg="red",bg="black",font=("Arial",15))
        """"gladbey"""
        sil1.place(x=100,y=50)
    penceresil=Tk()
    penceresil.title("kayıt sil!")
    penceresil.configure(background="black")
    penceresil.geometry("500x500+100+200")

    isim = Entry(penceresil)
    isim.place(x=200,y=100)

    kitapekle = Button(penceresil)
    kitapekle.config(text="sistemden sil", bg="grey", fg="white", height= 3, width=15,command=sistemsilbt)
    kitapekle.place(x=200,y=200)

def arabt():
    def sistemarabt():
        ad = isim.get()
        bir = data[ad][0]
        iki = data[ad][1]
        kisiad= Label(pencereara)
        kisiad.config(text="kişinin adı: {}".format(ad),fg="white",bg="black",font=("Arial",15))
        kisiad.place(x=100,y=300)

        kisikitap= Label(pencereara)
        kisikitap.config(text="kitabın adı: {}".format(bir),fg="white",bg="black",font=("Arial",15))
        """"berat karaca <3"""
        kisikitap.place(x=100,y=350)

        kitaptarih= Label(pencereara)
        kitaptarih.config(text="aldığı tarih: {}".format(iki),fg="white",bg="black",font=("Arial",15))
        kitaptarih.place(x=100,y=400)
    print(data)
    pencereara=Tk()
    pencereara.title("kayıt ara!")
    pencereara.configure(background="black")
    pencereara.geometry("500x500+100+200")

    isim = Entry(pencereara)
    isim.place(x=200,y=100)

    kisiara = Button(pencereara)
    kisiara.config(text="ara", bg="grey", fg="white", height= 3, width=15,command=sistemarabt)
    kisiara.place(x=200,y=200)
