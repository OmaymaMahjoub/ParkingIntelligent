from tkinter import * 
from BD import *
from Clients import *
import datetime
import time
homePage = Tk()
homePage['bg']='gray'

voitureRUP=PhotoImage(file = r".\images\RCarUp.png")
voitureRDOWN=PhotoImage(file = r".\images\RCarDown.png")
voitureBUP=PhotoImage(file = r".\images\BCarUp.png")
voitureBDOWN=PhotoImage(file = r".\images\BCarDown.png")

#liste client tkoon global
#liste emplacemnt , w methode te3ha
#methode add client
bd=BD("parking.sql")
list_client=bd.listClients()
#list_emplacement=bd.listEmplacement()
list_emplacement=[1,2,0,1,2,2,1,0]


Methode= True    # True direct , Fasle réservartion

#Vérification du client
def Recherche_Client(num):
   i=0
   test= False
   for c in list_client:
      if (c.get_cin()==num.get()):
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
    direct = Tk()
    direct['bg']='gray'
    Label(direct, text="Bienvenue, merci d'indiquer la durée de votre visite et puis choisir votre emplacement").pack()
    duree= Entry(direct, width= 60)
    duree.insert(0,"Durée de visite")
    duree.pack()
    confirmd= Button(direct,text="Choisir", bg='red')
    confirmd.pack()
    confirmd.config(command = Affichage(direct,datetime.datetime.now(),duree.get()))

#Gestion de reservartion
def gest_reservation():
    homePage.destroy()
    gres= Tk()
    gres['bg']='gray'
    labelr = Label(gres, text="Gestion de réservartion", bg="gray", fg="SlateBlue4" )
    labelr.config(font=("Roman bold", 30))
    labelr.pack()
    print("test")
    er=Entry(gres,width=60)
    er.insert(0,"Merci de nous fournir votre numéro de CIN")
    er.pack()
    reserver = Button(gres,text="Reserver", bg="red")
    reserver.pack()
    reserver.config(command=reservartion(gres,er.getint(er.get())))
    

#def test():
    #print('test')
def reservartion(arg,num):
    arg.destroy()
    res=Tk()
    res['bg']='gray'
    Methode=False
    if ((Recherche_Client(num)!=-1)):
        if (not(list_client[Recherche_Client(num)].reservation_exist())):
            label= Label(res,text="On est heureux de vous revoir chez nous, merci d'indiquer l'heure et la durée de votre visite et puis choisir votre emplacement,merci ", bg="gray",fg="SlateBlue4")
            label.config(font=("Roman bold", 30))
            label.pack()
            heure= Entry(res, width=60)
            heure.insert(0,"L'heure de votre arrivé")
            dure= Entry(res, width=60)
            dure.insert(0,"Durée") # bch taamel mise à jour 
            choisir=Button(res,text="Chosir votre emplacement")
            choisir.config(command=Affichage(res,heure,dure)) #fct taamel l affichage
        else:
            #aando réser bch yconformi li hoa je 
            confirm=Button(res,text="Confirmer")
            confirm.config(command= valider())        
    else:
            #création d'un client
            label= Label(arg,text="Merci pour avoir nous visiter, Merci d'indiquer votre nom")
            label.config(font=("Roman bold", 30))
            label.pack()
            nom= Entry(res,width=60)
            nom.insert(0,"Votre nom")
            bd.addClient(Client(num,nom.get()))
            heure= Entry(res, width=60)
            heure.insert(0,"L'heure de votre arrivé")
            dure= Entry(res, width=60)
            dure.insert(0,"Durée") # bch taamel mise à jour 
            choisir=Button(res,text="Chosir votre emplacement")
            choisir.config(command=Affichage(res,heure,dure)) #fct taamel l affichag
        


#Affichage Parking
#ROW1
def DispoBut1(arg,ii,jj):
    disponible= Button(arg,text="Emplacement Disponible",bg="green",command=choix(arg,ii))
    disponible.grid(row=1,column=ii-jj)
def ResBut1(arg,ii,jj):
    reservé=Button(arg,text="Emplacement Reservé",image=voitureBDOWN,bg='blue',command=choix(arg,ii))
    reservé.grid(row=1,column=ii-jj)
def OccupBut1(arg,ii,jj):
    occupé=Button(arg,text="Emplacement Occupé",image=voitureRDOWN,bg='red')
    occupé.grid(row=1,column=ii-jj)
def ProcheBut1(arg,ii,jj):
    proche=Button(arg,text="Emplacement le plus proche",bg="yellow")
    proche.grid(row=1,column=ii-jj)
#ROW2
def DispoBut2(arg,ii,jj):
    disponible= Button(arg,text="Emplacement Disponible",bg="green",command=choix(arg,ii))
    disponible.grid(row=2,column=ii-jj)
def ResBut2(arg,ii,jj):
    reservé=Button(arg,text="Emplacement Reservé",image=voitureBUP,bg='blue',command=choix(arg,ii))
    reservé.grid(row=2,column=ii-jj)
def OccupBut2(arg,ii,jj):
    occupé=Button(arg,text="Emplacement Occupé",image=voitureRUP,bg='red')
    occupé.grid(row=2,column=ii-jj)
def ProcheBut2(arg,ii,jj):
    proche=Button(arg,text="Emplacement le plus proche",bg="yellow")
    proche.grid(row=2,column=ii-jj)
#plus proche

def Affichage(arg,h,d): #paramtre l durée wl wakt 
    arg.destroy()
    aff= Tk()
    aff['bg']='gray'
    #updateliste_emplacmenet(h,d)
    n=len(list_emplacement)
    if ((n%2)==0):
        #l foo9
        i=0
        j=0
        while (i<n-1):
            if (list_emplacement[i]==0):
                if (plusproche(list_emplacement)==i):
                    ProcheBut1(aff,i,j)
                else:
                    DispoBut1(aff,i,j)
            elif (list_emplacement[i]==1):
                ResBut1(aff,i,j)
            else:
                OccupBut1(aff,i,j)
            i+=2
            j+=1
        #loota   
        i=1
        j=1
        while(i<n):
            if (plusproche(list_emplacement)==i):
                ProcheBut2(aff,i,j)
            elif (list_emplacement[i]==0):
                DispoBut2(aff,i,j)
            elif (list_emplacement[i]==1):
                ResBut2(aff,i,j)
            else:
                OccupBut2(aff,i,j)
            i+=2
            j+=1
    else:
        #foo9
        i=0
        j=0
        while(i<n-1):
            if (list_emplacement[i]==0):
                if (plusproche(list_emplacement)==i):
                    ProcheBut1(aff,i,j)
                else:
                    DispoBut1(aff,i,j)
            elif (list_emplacement[i]==1):
                ResBut1(aff,i,j)
            else:
                OccupBut1(aff,i,j)
            i+=2
            j+=1
        
        #l foo9 ekher kaaba
        if (list_emplacement[n]==0):
            if (plusproche(list_emplacement)==n):
                ProcheBut1(aff,n,0)
            else:
                DispoBut1(aff,n,0)
        elif (list_emplacement[n]==1):
            ResBut1(aff,n,0)
        elif (list_emplacement[n]==2):
                OccupBut1(aff,n,0)

        #loota
        i=1
        j=1
        while (i<n):
            if (list_emplacement[i]==0):
                if(plusproche(list_emplacement)==i):
                    ProcheBut1(aff,n,0)
                else:
                    DispoBut2(aff,i,j)
            elif (list_emplacement[i]==1):
                ResBut2(aff,i,j)
            else:
                OccupBut2(aff,i,j)
    aff.mainloop()


#methode taa choix trod lista m réservation ==> occupé , w sinon tzid occupé  bl methode
#def valider()
 #tekhoo l res heki w trodha occupé

def choix():
    if (Methode):
        #tzid juste occupé
        print("testee")
    else:
        #tekhoo l res heki w trodha occupé
        print("testeezef")

def plusproche(liste):
    i=0
    while (i<len(liste)):
       if ((liste[i]==0)):
          return i
       else:
          i+=1
    return -1

#main
Home()


        



