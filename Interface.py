from tkinter import * 
from BD import *
from Clients import Client
from Emplacement import Emplacement
import datetime
import time
homePage = Toplevel()
homePage['bg']='gray'

voitureRUP=PhotoImage(file = r".\images\RCarUp.png")
voitureRDOWN=PhotoImage(file = r".\images\RCarDown.png")
voitureBUP=PhotoImage(file = r".\images\BCarUp.png")
voitureBDOWN=PhotoImage(file = r".\images\BCarDown.png")
voitureGUP=PhotoImage(file=r".\images\GCarUp.png")
voitureGDOWN=PhotoImage(file=r".\images\GCarDown.png")
voitureWUP=PhotoImage(file=r".\images\WCarUP.png")
voitureWDOWN=PhotoImage(file=r".\images\WCarDown.png")


#liste client tkoon global
#liste emplacemnt , w methode te3ha
#methode add client
bd=BD("parking.sql")
list_client=bd.listClients()
list_emplacement=bd.listEmplacement()



Methode= True    # True direct , Fasle réservartion

#Vérification du client
def Recherche_Client(num):
   i=0
   test= False
   for c in list_client:
      if (c.get_cin()==num):
         test= True
         break
      else:
         i+=1
   if (test):
      return i
   else:
      return -1


#Menu principal
def Home():
    label = Label(homePage, text="Bienvenue", bg="gray", fg="SlateBlue4" )
    label.config(font=("Roman bold", 30))
    label.pack()
    reservation=Button(homePage,text ="Gestion de réservartion", bg='red' )
    reservation.pack()
    reservation.config(command = gest_reservation)
    surplace=Button(homePage,text ="Parking direct", bg='red' )
    surplace.pack()
    surplace.config(command = parking_direct)
    homePage.mainloop()

#Parking sur place
def parking_direct():
    Methode=True
    homePage.destroy()
    global direct 
    direct = Toplevel()
    direct['bg']='gray'
    Label(direct, text="Bienvenue, merci d'indiquer la durée de votre visite et puis choisir votre emplacement").pack()
    global duree
    duree= Entry(direct, width= 60)
    duree.insert(0,"Durée de visite en minutes")
    duree.pack()
    confirmd= Button(direct,text="Choisir", bg='red')
    confirmd.pack()
    confirmd.config(command = Affichage)

def Affichage():
    d=getint(duree.get())
    global fin
    fin = datetime.timedelta(minutes=d)+datetime.datetime.now()
    direct.destroy()
    aff= Toplevel()
    aff['bg']='gray'
    #updateliste_emplacmenet(heure,dure)
    n=len(list_emplacement[0])
    if ((n%2)==0):
        #l foo9
        i=0
        j=0
        while (i<n-1):
            if (list_emplacement[0][i].estOccupe(fin)==0):
                if (plusproche(list_emplacement)==i):
                    ProcheBut1(aff,i,j)
                else:
                    DispoBut1(aff,i,j)
            elif (list_emplacement[0][i].estOccupe(fin)==2):
                ResBut1(aff,i,j)
            else:
                OccupBut1(aff,i,j)
            i+=2
            j+=1
        #loota   
        i=1
        j=1
        while(i<n):
            if (list_emplacement[0][i].estOccupe(fin)==0):
                if (plusproche(list_emplacement)==i):
                    ProcheBut2(aff,i,j)
                else:
                    DispoBut2(aff,i,j)
            elif (list_emplacement[0][i].estOccupe(fin)==2):
                ResBut2(aff,i,j)
            else:
                OccupBut2(aff,i,j)
            i+=2
            j+=1
    else:
        #foo9
        i=0
        j=0
        while(i<=n-1):
            if (list_emplacement[0][i].estOccupe(fin)==0):
                if (plusproche(list_emplacement)==i):
                    ProcheBut1(aff,i,j)
                else:
                    DispoBut1(aff,i,j)
            elif (list_emplacement[0][i].estOccupe(fin)==2):
                ResBut1(aff,i,j)
            else:
                OccupBut1(aff,i,j)
            i+=2
            j+=1

        #loota
        i=1
        j=1
        while (i<n):
            if (list_emplacement[0][i].estOccupe(fin)==0):
                if(plusproche(list_emplacement)==i):
                    ProcheBut2(aff,i,j)
                else:
                    DispoBut2(aff,i,j)
            elif (list_emplacement[0][i].estOccupe(fin)==2):
                ResBut2(aff,i,j)
            else:
                OccupBut2(aff,i,j)
            
                #l foo9 ekher kaaba
            i+=2
            j+=1
    
        if (list_emplacement[0][n].estOccupe(fin)==0):
            if (plusproche(list_emplacement)==n):
                ProcheBut1(aff,n,0)
            else:
                DispoBut1(aff,n,0)
        if (list_emplacement[0][n].estOccupe(fin)==2):
            ResBut1(aff,n,0)
        if (list_emplacement[0][n].estOccupe(fin)==1):
                OccupBut1(aff,n,0)
    aff.mainloop()

#Gestion de reservartion
def gest_reservation():
    homePage.destroy()
    global gres
    gres= Toplevel()
    gres['bg']='gray'
    labelr = Label(gres, text="Gestion de réservartion", bg="gray", fg="SlateBlue4" )
    labelr.config(font=("Roman bold", 30))
    labelr.pack()
    print("test")
    er=Entry(gres,width=60, textvariable=DoubleVar())
    er.insert(0,"Merci de nous fournir votre numéro de CIN")
    er.pack()
    global n
    n=er.get()
    reserver = Button(gres,text="Reserver", bg="red")
    reserver.pack()
    reserver.config(command=reservartion)
    

def reservartion():
    print('testeee')
    gres.destroy()
    global res
    res=Toplevel()
    res['bg']='gray'
    Methode=False
    if ((Recherche_Client(n)!=-1)):
        if (not(list_client[Recherche_Client(n)].reservation_exist())):
            label= Label(res,text="On est heureux de vous revoir chez nous, merci d'indiquer l'heure et la durée de votre visite et puis choisir votre emplacement,merci ", bg="gray",fg="SlateBlue4")
            label.config(font=("Roman bold", 30))
            label.pack()
            global heure1
            heure1= Entry(res, width=60,textvariable=DoubleVar())
            heure1.insert(0,"L'heure de votre arrivé")
            global dure1
            dure1= Entry(res, width=60,textvariable=DoubleVar())
            dure1.insert(0,"Durée") # bch taamel mise à jour 
            choisir=Button(res,text="Chosir votre emplacement")
            choisir.config(command=Affichage(heure1,dure1)) #fct taamel l affichage
        else:
            #aando réser bch yconformi li hoa je 
            confirm=Button(res,text="Confirmer")
            confirm.config(command= valider)     
    else:
            #création d'un client
            label= Label(res,text="Merci pour avoir nous visiter, Merci d'indiquer votre nom")
            label.config(font=("Roman bold", 30))
            label.pack()
            nom= Entry(res,width=60)
            nom.insert(0,"Votre nom")
            nom.pack()
            #bd.addClient(Client(n,nom.get()))
            global heure2
            heure2= Entry(res, width=60,textvariable=DoubleVar())
            heure2.pack()
            heure2.insert(0,"L'heure de votre arrivé")
            global dure2
            dure2= Entry(res, width=60,textvariable=DoubleVar())
            dure2.pack()
            dure2.insert(0,"Durée") # bch taamel mise à jour             
            choisir=Button(res,text="Chosir votre emplacement")
            choisir.pack()
            choisir.config(command=Affichage) #fct taamel l affichag
            
        


#Affichage Parking
#ROW1
def DispoBut1(arg,ii,jj):
    disponible= Button(arg,text="Emplacement Disponible",image=voitureGDOWN, bg="green")
    disponible.grid(row=1,column=ii-jj)
def ResBut1(arg,ii,jj):
    reservé=Button(arg,text="Emplacement Reservé",image=voitureBDOWN,bg='blue')
    reservé.grid(row=1,column=ii-jj)
def OccupBut1(arg,ii,jj):
    occupé=Button(arg,text="Emplacement Occupé",image=voitureRDOWN,bg='red')
    occupé.grid(row=1,column=ii-jj)
def ProcheBut1(arg,ii,jj):
    proche=Button(arg,text="Emplacement le plus proche",image=voitureWDOWN, bg="yellow")
    proche.grid(row=1,column=ii-jj)
#ROW2
def DispoBut2(arg,ii,jj):
    disponible= Button(arg,text="Emplacement Disponible",image=voitureGUP,bg="green")
    disponible.grid(row=2,column=ii-jj)
def ResBut2(arg,ii,jj):
    reservé=Button(arg,text="Emplacement Reservé",image=voitureBUP,bg='blue')
    reservé.grid(row=2,column=ii-jj)
def OccupBut2(arg,ii,jj):
    occupé=Button(arg,text="Emplacement Occupé",image=voitureRUP,bg='red')
    occupé.grid(row=2,column=ii-jj)
def ProcheBut2(arg,ii,jj):
    proche=Button(arg,text="Emplacement le plus proche",image=voitureWUP,bg="yellow")
    proche.grid(row=2,column=ii-jj)
#plus proche


#def valider()
 #tekhoo l res heki w trodha occupé , tu confirmes eli hoa je

def choix():
    if (Methode):
        #tzid juste occupé
        print("testee")
    else:
        #tekhoo l res heki w trodha occupé
        print("testeezef")

def plusproche(liste):
    l=0
    while (l<len(liste[0])):
       if (liste[0][l].estOccupe(fin)==0):
          return l
       else:
          l+=1
    return -1

#main
Home()


        



