from tkinter import *
from tkinter import messagebox 
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




#Menu principal
def Home(i=0):
    if (i==1):
        direct.destroy()
    elif (i==2):
        gres.destroy()
    elif (i==3):
        res.destroy()
    global homePage
    homePage = Toplevel()
    homePage['bg']='LightSkyBlue4'
    label = Label(homePage, text="Bienvenue",bg='LightSkyBlue4', fg="SkyBlue3" )
    label.config(font=("Roman bold", 60,"bold"))
    label.pack(pady=5)
    reservation=Button(homePage,text ="Gestion de réservartion", bg='Deep Sky Blue3' ,fg='dark slate gray',height=4,width=25)
    reservation.pack(pady=40)
    reservation.config(font=("Roman bold", 17,"bold"))
    reservation.config(command = gest_reservation)
    surplace=Button(homePage,text ="Parking direct", bg='Deep Sky Blue3', fg="dark slate gray",height=4,width=25 )
    surplace.pack(pady=10)
    surplace.config(font=("Roman bold", 17,"bold"))
    surplace.config(command = parking_direct)
    homePage.mainloop()

#Parking sur place
def parking_direct():
    global Methode
    Methode=True
    homePage.destroy()
    global direct 
    direct = Toplevel()
    direct['bg']='LightSkyBlue4'
    l=Label(direct, text="Bienvenue, merci d'indiquer la durée de \nvotre visite et puis choisir votre emplacement",bg='LightSkyBlue4', fg="SkyBlue3")
    l.pack(pady=50)
    l.config(font=("Roman bold", 40,"bold"))
    global duree
    duree= Entry(direct,width= 60,textvariable=DoubleVar(), bg='LightSkyBlue3', fg="SkyBlue4")
    duree.insert(0,"Durée de visite en minutes")
    duree.config(font=("Roman bold", 17,"bold"))
    duree.pack(pady=2)
    global confirmd
    confirmd= Button(direct,text="Choisir",  bg='Deep Sky Blue3', fg="dark slate gray",height=2,width=15)
    confirmd.pack()
    confirmd.config(font=("Roman bold", 10,"bold"))
    confirmd.config(command = validation)
    annuler= Button(direct,text="Annuler",  bg='Deep Sky Blue3', fg="dark slate gray",height=2,width=15)
    annuler.pack(pady=8)
    annuler.config(font=("Roman bold", 10,"bold"))
    annuler.config(command = lambda: Home(1))

def validation():
    if ((duree.get().isdigit())and(getint(duree.get())>0)):
        if (getint(duree.get())>1440):
            l2=Label(direct,text="*La durée ne dépasse pas 1440 minutes (24H)", bg="LightSkyBlue4",fg="red")
            l2.pack(pady=2, before=confirmd)   
        else :
            Affichage()
    else:
        l2=Label(direct,text="*La durée doit etre en minutes", bg="LightSkyBlue4",fg="red")
        l2.pack(pady=2, before=confirmd)


#Vérification du client
def Recherche_Client(num):
   i=0
   test= False
   for c in list_client:
      if (c.get_cin()==int(num)):
         test= True
         break
      else:
         i+=1
   if (test==True):
      return i
   else:
      return -1

#Recherche emplacement
def Recherche_Emplacement(id):
   test= False
   i=0
   for c in list_emplacement[0]:
      if (c.get_id()==id):
         test=True
         break
      else:
          i+=1
   if (test==True):
      return i
   else:
      return -1

#Gestion de reservartion  
def gest_reservation():
    homePage.destroy()
    global gres
    gres= Toplevel()
    gres['bg']='LightSkyBlue4'
    labelr = Label(gres, text="Gestion De Réservartion", bg='LightSkyBlue4', fg="SkyBlue3" )
    labelr.config(font=("Roman bold", 40,"bold"))
    labelr.pack(pady=5)
    cin=Entry(gres,width= 60, textvariable=DoubleVar(), bg='LightSkyBlue3', fg="SkyBlue4")
    cin.insert(0,"Merci de nous fournir votre numéro de CIN")
    cin.config(font=("Roman bold", 17,"bold"))
    cin.pack(pady=20)
    global ciin
    ciin=cin
    global reserver
    reserver = Button(gres,text="Reserver",  bg='Deep Sky Blue3', fg="dark slate gray",height=2,width=15)
    reserver.pack(pady=5)
    reserver.config(font=("Roman bold", 10,"bold"))
    reserver.config(command=verif_cin)
    annuler= Button(gres,text="Annuler",  bg='Deep Sky Blue3', fg="dark slate gray",height=2,width=15)
    annuler.pack(pady=8)
    annuler.config(font=("Roman bold", 10,"bold"))
    annuler.config(command = lambda: Home(2))

def verif_cin():
    if((len(ciin.get())==8)and (ciin.get().isdigit())):
        reservartion()
    else:
        l2=Label(gres,text="*Verifiez le CIN", bg="LightSkyBlue4",fg="red")
        l2.pack(pady=2, before=reserver)
        
def reservartion():
    global cin
    cin=str(ciin.get())
    print('testeee')
    gres.destroy()
    global res
    res=Toplevel()
    res['bg']='LightSkyBlue4'
    global Methode
    Methode=False
    global dure
    global heure
    global choisir
    if ((Recherche_Client(cin)!=-1)):
        if (not(list_client[Recherche_Client(cin)].reservation_exist())):
            label= Label(res,text="On est heureux de vous revoir chez nous Mr/Mme "+list_client[Recherche_Client(cin)].get_nom()+",\nmerci d'indiquer l'heure et la durée de votre visite \net puis choisir votre emplacement,\nmerci ", bg='LightSkyBlue4', fg="SkyBlue3")
            label.config(font=("Roman bold", 40,"bold"))
            label.pack(pady=25)
            global heure
            heure= Entry(res, width=60,textvariable=DoubleVar(),bg='LightSkyBlue3', fg="SkyBlue4")
            heure.insert(0,"L'heure de votre arrivé comme la suite YYYY-MM-DD HH:MM")
            heure.config(font=("Roman bold", 17,"bold"))
            heure.pack(pady=2)
            global dure
            dure= Entry(res, width=60,textvariable=DoubleVar(),bg='LightSkyBlue3', fg="SkyBlue4")
            dure.insert(0,"Durée") # bch taamel mise à jour 
            dure.config(font=("Roman bold", 17,"bold"))
            dure.pack(pady=2)
            choisir=Button(res,text="Chosir votre emplacement", bg='Deep Sky Blue3', fg="dark slate gray",height=2,width=25)
            choisir.pack(pady=2)
            choisir.config(font=("Roman bold", 10,"bold"))
            choisir.config(command=verif_date)
            annuler= Button(res,text="Annuler",  bg='Deep Sky Blue3', fg="dark slate gray",height=2,width=15)
            annuler.pack(pady=8)
            annuler.config(font=("Roman bold", 10,"bold"))
            annuler.config(command = lambda: Home(3))
        else:
            c=list_client[Recherche_Client(cin)]
            duration=c.get_periode()
            if ((duration[0]<=datetime.datetime.now())and (datetime.datetime.now()<duration[1])):
                MsgBox=messagebox.askquestion("Reservation","Vous avez une reservation\n\tEmplacement:"+str(c.get_emplacement())+"\n\tEtage:"+str(1)+"\n\tDebut:"+str(duration[0])+"\n\tFin:"+str(duration[1])+"\nCliquez non pour annuler la réservation")
                if (MsgBox=='yes'):
                    e=Recherche_Emplacement(c.get_emplacement())
                    list_emplacement[0][e].fin_reservation()                        
                    list_emplacement[0][e].occupe(duration[1])
                    bd.updateEmplacement(list_emplacement[0][e])
                else:
                    e=Recherche_Emplacement(c.get_emplacement())
                    list_emplacement[0][e].fin_reservation()
                    bd.updateEmplacement(list_emplacement[0][e])
            Home()
    else:
            #création d'un client
            label= Label(res,text="Merci pour avoir nous visiter\n Merci d'indiquer votre nom",bg='LightSkyBlue4', fg="SkyBlue3")
            label.config(font=("Roman bold", 40,"bold"))
            label.pack(pady=25)
            nom= Entry(res,width=60,textvariable=DoubleVar(),bg='LightSkyBlue3', fg="SkyBlue4")
            nom.insert(0,"Votre nom")
            nom.config(font=("Roman bold", 17,"bold"))
            nom.pack(pady=2)
            global name
            name=nom.get()
            heure= Entry(res, width=60,textvariable=DoubleVar(),bg='LightSkyBlue3', fg="SkyBlue4")
            heure.pack(pady=2)
            heure.insert(0,"L'heure de votre arrivé comme la suite YYYY-MM-DD HH:MM")
            heure.config(font=("Roman bold", 17,"bold"))
            dure= Entry(res, width=60,textvariable=DoubleVar(),bg='LightSkyBlue3', fg="SkyBlue4")
            dure.config(font=("Roman bold", 17,"bold"))
            dure.pack(pady=2)
            dure.insert(0,"Durée") # bch taamel mise à jour
            choisir=Button(res,text="Chosir votre emplacement",bg='Deep Sky Blue3', fg="dark slate gray",height=2,width=25)
            choisir.pack(pady=15)
            choisir.config(font=("Roman bold", 10,"bold"))
            choisir.config(command=verif_date) #fct taamel l affichag
            annuler= Button(res,text="Annuler",  bg='Deep Sky Blue3', fg="dark slate gray",height=2,width=15)
            annuler.pack(pady=8)
            annuler.config(font=("Roman bold", 10,"bold"))
            annuler.config(command = lambda: Home(3))

def verif_date():
    test=0
    test1=0
    if ((heure.get().count("-")==2)and (heure.get().count(":")==1)):
        l=(heure.get()).split(" ")
        l1=l[0].split("-")
        l2=l[1].split(":")
        l=[]
        l=l1+l2
        if (len(l)!=5):
            test=1
        else:
            for i in range(len(l)):
                if (not(l[i].isdigit())):
                    test=1
            if (test==0):
                try:
                    global debut
                    debut=datetime.datetime(int(str(l[0])),int(str(l[1])),int(str(l[2])),int(str(l[3])),int(str(l[4])))
                    if (debut<datetime.datetime.now()):
                        test=2
                except ValueError:
                    test=1
    else:
        test=1
    if ((dure.get().isdigit())and(getint(dure.get())>0)):
        if (getint(dure.get())>1440):
            l3=Label(res,text="*La durée ne dépasse pas 1440 minutes (24H)", bg="LightSkyBlue4",fg="red")
            l3.pack(pady=2, before=choisir)   
        else :
            test1=1
    else:
        l3=Label(res,text="*La durée doit etre en minutes", bg="LightSkyBlue4",fg="red")
        l3.pack(pady=2, before=choisir)
    if (test==1):
        l2=Label(res,text="*Verifiez la date", bg="LightSkyBlue4",fg="red")
        l2.pack(pady=2, before=dure)
    elif (test==2):
        l2=Label(res,text="*Date ne doit pas etre depassé", bg="LightSkyBlue4",fg="red")
        l2.pack(pady=2, before=dure)
    elif ((test==0) and(test1==1)):
        Affichage()
#Affichage Parking
#ROW1
def DispoBut1(arg,ii,jj):
    disponible= Button(arg,text="Emplacement Disponible",image=voitureGDOWN, bg="green")
    disponible.grid(row=1,column=ii-jj)
    disponible.config(command=lambda:confirmation(ii))
def ResBut1(arg,ii,jj):
    reserve=Button(arg,text="Emplacement Reservé",image=voitureBDOWN,bg='blue')
    reserve.grid(row=1,column=ii-jj)
def OccupBut1(arg,ii,jj):
    occupé=Button(arg,text="Emplacement Occupé",image=voitureRDOWN,bg='red')
    occupé.grid(row=1,column=ii-jj)
def ProcheBut1(arg,ii,jj):
    proche=Button(arg,text="Emplacement le plus proche",image=voitureWDOWN, bg="yellow")
    proche.grid(row=1,column=ii-jj)
    proche.config(command=lambda:confirmation(ii))
#ROW2
def DispoBut2(arg,ii,jj):
    disponible= Button(arg,text="Emplacement Disponible",image=voitureGUP,bg="green")
    disponible.grid(row=2,column=ii-jj)
    disponible.config(command=lambda:confirmation(ii))
def ResBut2(arg,ii,jj):
    reserve=Button(arg,text="Emplacement Reservé",image=voitureBUP,bg='blue')
    reserve.grid(row=2,column=ii-jj)
def OccupBut2(arg,ii,jj):
    occupé=Button(arg,text="Emplacement Occupé",image=voitureRUP,bg='red')
    occupé.grid(row=2,column=ii-jj)
def ProcheBut2(arg,ii,jj):
    proche=Button(arg,text="Emplacement le plus proche",image=voitureWUP,bg="yellow")
    proche.grid(row=2,column=ii-jj)
    proche.config(command=lambda:confirmation(ii))

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
       fin=datetime.timedelta(minutes=d)+debut
       res.destroy
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

def confirmation(x):
    MsgBox=messagebox.askquestion("Confirmation","Prière confirmer votre choix:\n\tEmplacement:"+str(list_emplacement[0][x].get_id())+"\n\tEtage:"+str(1)+"\n\tDebut:"+str(debut)+"\n\tFin:"+str(fin))
    if (MsgBox=='yes'):
        choix(x)
def choix(x):
    if (Methode):
        list_emplacement[0][x].occupe(fin)
        aff.destroy()
        bd.updateEmplacement(list_emplacement[0][x])
        Home()
    else:
        list_emplacement[0][x].add_reservation(debut,fin)
        bd.updateEmplacement(list_emplacement[0][x])
        if (Recherche_Client(cin)==-1):     
           c=Client(name,cin,x,True,[debut,fin])
           list_client.append(c)
           bd.addClient(c)
        else:
           k=Recherche_Client(cin)
           list_client[k].reservation([debut,fin],x)
           bd.updateClient(list_client[k])
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


        



