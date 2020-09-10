from tkinter import * 
from Emplacement import *
homePage = Tk()
homePage['bg']='gray'

#liste client tkoon global
#variable global  temchi fl fct li feha l choix taa l blasa wl variable heki hia li bch tfara9 bin l réservartion wala surplace
#aleh naamlooch dictionnaire yetsnaa waktha  wala hata lista tabda l index hia l num taa l emplacemnet w valeur hia 0 1 2 , w  yetaamel waktha selon l wakt li ta3taa 
empla= True    # True direct , Fasle réservartion

#Vérification du client
def Recherche_Client(num):
   i=0
   test= False
   while (i in list_client):
       if (list_client[i]==num.get()):
           test= True
           break
        else:
            i++
    return test


#Menu principal
def Home():
    label = Label(homePage, text="Bienvenue", bg="gray", fg="SlateBlue4" )
    label.config(font=("Roman bold", 30))
    label.pack()
    reservation=Button(homePage,text ="Gestion de réservartion", bg='red' )
    reservation.pack()
    reservation.config(command = gest_reservation )
    surplace=Button(homePage,text ="Parking direct", bg='red', )
    surplace.pack()
    surplace.config(command = parking_direct)
    homePage.mainloop()

#Parking sur place
def parking_direct():
    #na7i cin
    homePage.destroy()
    direct = Tk()
    direct['bg']='gray'
    ed = Entry(direct, width= 60)
    ed.insert(0, "Donner votre num de CIN")
    ed.pack()
    confirmd= Button(direct,text="Confirmer", bg='red')
    confirmd.pack()
    confirmd.config(command = confirmation_direct(direct,ed.get()))

def confirmation_direct(arg,num):
   arg.destroy()
   arg=Tk()
   arg['bg']='gray'
   print('test')
    if (Recherche_Client(num)):
        #Client existe
        label= Label(arg,text="On est heureux de vous revoir chez nous, merci d'indiquer la durée de votre visite et puis choisir votre emplacement,merci ", bg="gray",fg="SlateBlue4")
        label.config(font=("Roman bold", 30))
        label.pack()
        dure= Entry(arg, width=60)*
        dure.insert(0,"Durée") # bch taamel mise à jour 


        choisir=Button(arg,text='Choisir',bg="red")
        choisir.config(command= )# ydeclanchi l fct li a9reb wahda lih 
        
    else:
        #Création
    

#Gestion de reservartion
#L page de menu de réservartion
def gest_reservation():
    homePage.destroy()
    gres= Tk()
    gres['bg']='gray'
    labelr = Label(gres, text="Gestion de réservartion", bg="gray", fg="SlateBlue4" )
    labelr.config(font=("Roman bold", 30))
    labelr.pack()
    print("test")
    reserverB = Button(gres,text="Reserver", bg="red")
    reserverB.pack()
    reserverB.config(command = reserver(gres) )
    valider = Button(gres,text="Valider", bg='red')
    valider.pack()
    
def reserver(arg):
    arg.destroy()
    arg= Tk()
    arg['bg']='gray'
    er = Entry(arg, width= 60)
    er.insert(0, "Donner votre num de CIN")
    er.pack() 
    confirmr= Button(arg,text="Confirmer", bg='red')
    confirm.config(command = reservartion(arg,er.get()) )

def reservartion(arg,num):
    if (Recherche_Client(num)):
        label= Label(arg,text="On est heureux de vous revoir chez nous, merci d'indiquer l'heure et la durée de votre visite et puis choisir votre emplacement,merci ", bg="gray",fg="SlateBlue4")
        label.config(font=("Roman bold", 30))
        label.pack()
        heure= Entry(arg, width=60)
        heure.insert(0,"L'heure de votre arrivé")
        dure= Entry(arg, width=60)
        dure.insert(0,"Durée") # bch taamel mise à jour 
        chosisir=Button(arg,text="Chosir votre emplacement")
        choisir.config(command=) #fct taamel l affichage

    else:
        #création d'un client

#Affichage Parking
def Affichage(arg):
    arg.destroy()
    arg= Tk()
    arg['bg']='gray'
    if (empla):#   Direct

    else: # rersevation



#main
Home()


        



