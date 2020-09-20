from tkinter import * 
from BD import *
from Clients import Client
from Emplacement import Emplacement
import datetime
import time
h = Toplevel()
h['bg']='blue'
h.destroy()

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
    global homePage
    homePage = Toplevel()
    homePage['bg']='gray'
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
    global Methode
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

#Gestion de reservartion
def gest_reservation():
    homePage.destroy()
    global gres
    gres= Toplevel()
    gres['bg']='gray'
    labelr = Label(gres, text="Gestion de réservartion", bg="gray", fg="SlateBlue4" )
    labelr.config(font=("Roman bold", 30))
    labelr.pack()
    cin=Entry(gres,width=60, textvariable=DoubleVar())
    cin.insert(0,"Merci de nous fournir votre numéro de CIN")
    cin.pack()
    global ciin
    ciin=cin
    reserver = Button(gres,text="Reserver", bg="red")
    reserver.pack()
    reserver.config(command=reservartion)
    

def reservartion():
    global cin
    cin=getint(ciin.get())
    print('testeee')
    gres.destroy()
    global res
    res=Toplevel()
    res['bg']='gray'
    global Methode
    Methode=False
    if ((Recherche_Client(cin)!=-1)):
        if (not(list_client[Recherche_Client(cin)].reservation_exist())):
            label= Label(res,text="On est heureux de vous revoir chez nous, merci d'indiquer l'heure et la durée de votre visite et puis choisir votre emplacement,merci ", bg="gray",fg="SlateBlue4")
            label.config(font=("Roman bold", 30))
            label.pack()
            global heure
            heure= Entry(res, width=60,textvariable=DoubleVar())
            heure.insert(0,"L'heure de votre arrivé")
            global dure
            dure= Entry(res, width=60,textvariable=DoubleVar())
            dure.insert(0,"Durée") # bch taamel mise à jour 
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
            global name
            name=nom.get()
            #bd.addClient(Client(n,nom.get()))
            heure= Entry(res, width=60,textvariable=DoubleVar())
            heure.pack()
            heure.insert(0,"L'heure de votre arrivé")
            dure= Entry(res, width=60,textvariable=DoubleVar())
            dure.pack()
            dure.insert(0,"Durée") # bch taamel mise à jour             
            choisir=Button(res,text="Chosir votre emplacement")
            choisir.pack()
            choisir.config(command=Affichage) #fct taamel l affichag
            
        


#Affichage Parking
#ROW1
def DispoBut1(arg,ii,jj):
    disponible= Button(arg,text="Emplacement Disponible",image=voitureGDOWN, bg="green")
    disponible.grid(row=1,column=ii-jj)
    disponible.config(command=lambda:choix(ii))
def ResBut1(arg,ii,jj):
    reserve=Button(arg,text="Emplacement Reservé",image=voitureBDOWN,bg='blue')
    reserve.grid(row=1,column=ii-jj)
def OccupBut1(arg,ii,jj):
    occupé=Button(arg,text="Emplacement Occupé",image=voitureRDOWN,bg='red')
    occupé.grid(row=1,column=ii-jj)
def ProcheBut1(arg,ii,jj):
    proche=Button(arg,text="Emplacement le plus proche",image=voitureWDOWN, bg="yellow")
    proche.grid(row=1,column=ii-jj)
    proche.config(command=lambda:choix(ii))
#ROW2
def DispoBut2(arg,ii,jj):
    disponible= Button(arg,text="Emplacement Disponible",image=voitureGUP,bg="green")
    disponible.grid(row=2,column=ii-jj)
    disponible.config(command=lambda:choix(ii))
def ResBut2(arg,ii,jj):
    reserve=Button(arg,text="Emplacement Reservé",image=voitureBUP,bg='blue')
    reserve.grid(row=2,column=ii-jj)
def OccupBut2(arg,ii,jj):
    occupé=Button(arg,text="Emplacement Occupé",image=voitureRUP,bg='red')
    occupé.grid(row=2,column=ii-jj)
def ProcheBut2(arg,ii,jj):
    proche=Button(arg,text="Emplacement le plus proche",image=voitureWUP,bg="yellow")
    proche.grid(row=2,column=ii-jj)
    proche.config(command=lambda:choix(ii))

def Affichage():
    global debut
    global fin
    print(Methode)
    if(Methode==True):
       d=getint(duree.get())
       debut=datetime.datetime.now()
       fin = datetime.timedelta(minutes=d)+datetime.datetime.now()
       direct.destroy()
    else:
       d=getint(dure.get())
       l=(heure.get()).split("-")
       debut=datetime.datetime(int(str(l[0])),int(str(l[1])),int(str(l[2])),int(str(l[3])),int(str(l[4])))
       fin=datetime.timedelta(minutes=d)+debut
       gres.destroy
    global aff
    aff= Toplevel()
    aff['bg']='gray'
    #updateliste_emplacmenet(heure,dure)
    n=len(list_emplacement[0])
    if ((n%2)==0):
        #l foo9
        i=0
        j=0
        while (i<n-1):

            if (list_emplacement[0][i].state(debut,fin)==0):
                if (plusproche(list_emplacement)==i):
                    ProcheBut1(aff,i,j)
                else:
                    DispoBut1(aff,i,j)
            elif (list_emplacement[0][i].state(debut,fin)==2):
                ResBut1(aff,i,j)
            else:
                OccupBut1(aff,i,j)
            i+=2
            j+=1
        #loota   
        i=1
        j=1
        while(i<n):

            if (list_emplacement[0][i].state(debut,fin)==0):
                if (plusproche(list_emplacement)==i):
                    ProcheBut2(aff,i,j)
                else:
                    DispoBut2(aff,i,j)
            elif (list_emplacement[0][i].state(debut,fin)==2):
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

            if (list_emplacement[0][i].state(debut,fin)==0):
                if (plusproche(list_emplacement)==i):
                    ProcheBut1(aff,i,j)
                else:
                    DispoBut1(aff,i,j)
            elif (list_emplacement[0][i].state(debut,fin)==2):
                ResBut1(aff,i,j)
            else:
                OccupBut1(aff,i,j)
            i+=2
            j+=1

        #loota
        i=1
        j=1
        while (i<n):
 
            if (list_emplacement[0][i].state(debut,fin)==0):
                if(plusproche(list_emplacement)==i):
                    ProcheBut2(aff,i,j)
                else:
                    DispoBut2(aff,i,j)
            elif (list_emplacement[0][i].state(debut,fin)==2):
                ResBut2(aff,i,j)
            else:
                OccupBut2(aff,i,j)
            
                #l foo9 ekher kaaba
            i+=2
            j+=1

        if (list_emplacement[0][n].state(debut,fin)==0):
            if (plusproche(list_emplacement)==n):
                ProcheBut1(aff,n,0)
            else:
                DispoBut1(aff,n,0)
        if (list_emplacement[0][n].state(debut,fin)==2):
            ResBut1(aff,n,0)
        if (list_emplacement[0][n].state(debut,fin)==1):
                OccupBut1(aff,n,0)
    aff.mainloop()



def choix(x):
    if (Methode):
        list_emplacement[0][x].occupe(fin)
        aff.destroy()
        bd.updateEmplacement(list_emplacement[0][x])
        Home()
    else:
        print(name)
        print(cin)
        print(x)
        list_emplacement[0][x].add_reservation(debut,fin)
        bd.updateEmplacement(list_emplacement[0][x])
        if (Recherche_Client(cin)==-1):
           
           c=Client(name,cin,x,True,[debut,fin])
           list_client.append(c)
           bd.addClient(c)
        else:
           c=Client(name,cin,x,True,[debut,fin])
           k=Recherche_Client(cin)
           list_client[k]=c
           bd.updateClient(c)
        aff.destroy()
        Home()
        
#plus proche
def plusproche(liste):
    l=0
    while (l<len(liste[0])):
       if (liste[0][l].state(debut,fin)==0):
          return l
       else:
          l+=1
    return -1

#main
Home()


        



