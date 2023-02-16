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
from moduller import *
from data import *

pencere=Tk()

pencere.title("Kütüphane sistemi!")
pencere.configure(background="black")
"""berat karaca"""
pencere.geometry("500x500+100+200")

label1= Label()
label1.config(text="kütüphane sistemi",bg="black",fg="white",font=("Arial",20))
label1.place(x=150,y=50)

buton1 = Button(pencere)
buton1.config(text="ekle", bg="grey", fg="white", height= 3, width=15,command=eklebt)
buton1.place(x=200,y=150)

buton2 = Button(pencere)
buton2.config(text="kaldır", bg="grey", fg="white", height= 3, width=15,command=silbt)
buton2.place(x=200,y=250)

buton3 = Button(pencere)
buton3.config(text="liste", bg="grey", fg="white", height= 3, width=15,command=arabt)
buton3.place(x=200,y=350)
mainloop()