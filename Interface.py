from tkinter import * 
from Emplacement import *
homePage = Tk()
homePage['bg']='gray'
    

#Menu principal
def Home():
    label = Label(homePage, text="Bienvenue", bg="gray", fg="SlateBlue4" )
    label.config(font=("Roman bold", 30))
    label.place(x=150, y=0)
    reservation=Button(homePage,text ="Gestion de réservartion", bg='red' )
    reservation.place(x=10, y=100)
    reservation.config(command = gest_reservation )
    surplace=Button(homePage,text ="Parking direct", bg='red', )
    surplace.place(x=350, y=100)
    homePage.mainloop()

#Gestion de reservartion
def gest_reservation():
    res= Tk()
    res['bg']='gray'
    labelr = Label(res, text="Gestion de réservartion", bg="gray", fg="SlateBlue4" )
    labelr.config(font=("Roman bold", 30))
    labelr.place(x=150, y=0)
    print("test")
    reserverB = Button(res,text="Reserver", bg="red")
    reserverB.place(x=10, y=100)
    reserverB.config(command = reserver() )
    valider = Button(res,text="Valider", bg='red')
    valider.place(x=350,y=100)
    
def reserver():
    print('testee')


Home()


        



