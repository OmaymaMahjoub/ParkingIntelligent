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

#images utilisées dans l'interface
voitureRUP=PhotoImage(file = r".\images\RCarUp.png")
voitureRDOWN=PhotoImage(file = r".\images\RCarDown.png")
voitureBUP=PhotoImage(file = r".\images\BCarUp.png")
voitureBDOWN=PhotoImage(file = r".\images\BCarDown.png")
voitureGUP=PhotoImage(file=r".\images\GCarUp.png")
voitureGDOWN=PhotoImage(file=r".\images\GCarDown.png")
voitureWUP=PhotoImage(file=r".\images\WCarUP.png")
voitureWDOWN=PhotoImage(file=r".\images\WCarDown.png")


#prendre les données de base de donnée
bd=BD("parking.sql")
global list_client
global list_emplacement
list_client=bd.listClients()
list_emplacement=bd.listEmplacement()



###########################################Menu########################################################

#Menu principal
def Home(i=0):

    #i est utilisé pour connaitre l'exacte toplevel à supprimer lorsque on click annuler
    if (i==1):
        direct.destroy()
    elif (i==2):
        gres.destroy()
    elif (i==3):
        res.destroy()
    elif (i==4):
        aff.destroy()

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
    
    #Methode pour connaitre si l'action est une reservation ou direct
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

#le commande ne passe pas que si la durée est un entier et ne depasse pas 24H donc on doit le verifier avant confirmation avec cette methode
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

#la methode reservation() ne doit pas etre appeler que après verifier si le cin est de 8 numeros
def verif_cin():
    if((len(ciin.get())==8)and (ciin.get().isdigit())):
        reservartion()
    else:
        l2=Label(gres,text="*Verifiez le CIN", bg="LightSkyBlue4",fg="red")
        l2.pack(pady=2, before=reserver)
        
def reservartion():
    #Methode est le meme bool pour verifier quel est l'action à traiter
    global cin
    cin=str(ciin.get())
    gres.destroy()
    global res
    res=Toplevel()
    res['bg']='LightSkyBlue4'
    global Methode
    Methode=False
    global dure
    global heure
    global choisir

    #si le client exist deja dans la base de donnée
    if ((Recherche_Client(cin)!=-1)):
        #si le client n'a pas une reservation en cour 
        if (not(list_client[Recherche_Client(cin)].reservation_exist())):

            label= Label(res,text="On est heureux de vous revoir chez nous Mr/Mme "+list_client[Recherche_Client(cin)].get_nom()+",\nmerci d'indiquer l'heure et la durée de votre visite \net puis choisir votre emplacement,\nmerci ", bg='LightSkyBlue4', fg="SkyBlue3")
            label.config(font=("Roman bold", 30,"bold"))
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
        #si le client a deja une reservation en cour,on doit verifier si la date de debut de reservation depasse la date à l'instant ou la reservation pas valable à l'instant debut> temps à l'instant
        else:
            c=list_client[Recherche_Client(cin)]
            duration=c.get_periode()
            e=c.get_emplacement()

            #si le temps de reservation debut et ne termine pas on doit verifier si le client va annulée la reservation ou il arrive (c a d changé l'état de l'emplacement de reservé à occupé)
            if ((duration[0]<=datetime.datetime.now())and (datetime.datetime.now()<duration[1])):
                MsgBox=messagebox.askquestion("Reservation","Vous avez une reservation\n\tEmplacement:"+str(e)+"\n\tEtage:"+str(list_emplacement[e].get_etage())+"\n\tDebut:"+str(duration[0])+"\n\tFin:"+str(duration[1])+"\nCliquez non pour annuler la réservation")

                if (MsgBox=='yes'):
                    #change d'état de l'emplacement
                    list_emplacement[e].fin_reservation()
                    list_emplacement[e].occupe(duration[1])
                    bd.updateEmplacement(list_emplacement[e])
                    
                else:
                    #annulée la reservation
                    list_emplacement[e].fin_reservation()
                    c.res_finis()
                    bd.updateClient(c)
                    bd.updateEmplacement(list_emplacement[e])
                Home()

            #si le temps de reservation n'est pas encore debut donc on doit verifier si le client va attendre le temps exact ou annuler et faire une reservation sur place    
            elif (duration[0]>datetime.datetime.now()):
                MsgBox=messagebox.askquestion("Reservation mais pas valable à l'instant","Vous avez une reservation\n\tEmplacement:"+str(e)+"\n\tEtage:"+str(list_emplacement[e].get_etage())+"\n\tDebut:"+str(duration[0])+"\n\tFin:"+str(duration[1])+"\nCliquez oui pour annuler la réservation et faire une reservation à 'linstant et non pour attendre la date de reservation ")

                if (MsgBox=='yes'):
                    #si le client veut entre à l'instant
                    list_emplacement[e].fin_reservation()
                    bd.updateEmplacement(list_emplacement[e])
                    c.res_finis()
                    bd.updateClient(c)
                    parking_direct()
                else:
                    #attendre le temps de reservation
                    Home()
    else:
            #création d'un client
            label= Label(res,text="Merci pour avoir nous visiter\n Merci d'indiquer votre nom",bg='LightSkyBlue4', fg="SkyBlue3")
            label.config(font=("Roman bold", 40,"bold"))
            label.pack(pady=25)

            global nom
            nom= Entry(res,width=60,textvariable=DoubleVar(),bg='LightSkyBlue3', fg="SkyBlue4")
            nom.config(font=("Roman bold", 17,"bold"))
            nom.pack(pady=2)
            nom.insert(0,"Votre nom")

            heure= Entry(res, width=60,textvariable=DoubleVar(),bg='LightSkyBlue3', fg="SkyBlue4")
            heure.pack(pady=2)
            heure.insert(0,"L'heure de votre arrivé comme la suite YYYY-MM-DD HH:MM")
            heure.config(font=("Roman bold", 17,"bold"))

            dure= Entry(res, width=60,textvariable=DoubleVar(),bg='LightSkyBlue3', fg="SkyBlue4")
            dure.config(font=("Roman bold", 17,"bold"))
            dure.pack(pady=2)
            dure.insert(0,"Durée")

            choisir=Button(res,text="Chosir votre emplacement",bg='Deep Sky Blue3', fg="dark slate gray",height=2,width=25)
            choisir.pack(pady=15)
            choisir.config(font=("Roman bold", 10,"bold"))
            choisir.config(command=verif_date) 

            annuler= Button(res,text="Annuler",  bg='Deep Sky Blue3', fg="dark slate gray",height=2,width=15)
            annuler.pack(pady=8)
            annuler.config(font=("Roman bold", 10,"bold"))
            annuler.config(command = lambda: Home(3))

#cette methode vérifie si la date est de la forme "yyyy-mm-dd hh:mm" et que cette date exist et n'est pas depassé de plus verifie si la durée en minute(entier) et ne dépasse pas 24H
def verif_date():
    #test c'est pour connaitre le type d'erreur pour avoir l'exact message à afficher au client
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



######################################Affichage Parking##################################################

#les boutons des emplacements

#ROW1
        
def DispoBut1(arg,ii,jj):
    disponible= Button(arg,text="Emplacement Disponible",image=voitureGDOWN, bg="green")
    disponible.grid(row=3,column=ii+1)
    global e
    #pour avoir l'id de l'emplacement dans la base de donnée (list_emplacement)
    p=0
    for i in range(1,e):
       p+=len(parEtage(i))
    jj+=p
    disponible.config(command=lambda:confirmation(jj))

def ResBut1(arg,ii,jj):
    reserve=Button(arg,text="Emplacement Reservé",image=voitureBDOWN,bg='blue')
    reserve.grid(row=3,column=ii+1)

def OccupBut1(arg,ii,jj):
    occupé=Button(arg,text="Emplacement Occupé",image=voitureRDOWN,bg='red')
    occupé.grid(row=3,column=ii+1)

def ProcheBut1(arg,ii,jj):
    proche=Button(arg,text="Emplacement le plus proche",image=voitureWDOWN, bg="yellow")
    proche.grid(row=3,column=ii+1)
    global e
    p=0
    for i in range(1,e):
       p+=len(parEtage(i))
    jj+=p
    proche.config(command=lambda:confirmation(jj))

#ROW2

def DispoBut2(arg,ii,jj):
    disponible= Button(arg,text="Emplacement Disponible",image=voitureGUP,bg="green")
    disponible.grid(row=4,column=ii+1)
    disponible.config(command=lambda:confirmation(jj))

def ResBut2(arg,ii,jj):
    reserve=Button(arg,text="Emplacement Reservé",image=voitureBUP,bg='blue')
    reserve.grid(row=4,column=ii+1)

def OccupBut2(arg,ii,jj):
    occupé=Button(arg,text="Emplacement Occupé",image=voitureRUP,bg='red')
    occupé.grid(row=4,column=ii+1)

def ProcheBut2(arg,ii,jj):
    proche=Button(arg,text="Emplacement le plus proche",image=voitureWUP,bg="yellow")
    proche.grid(row=4,column=ii+1)
    global e
    p=0
    for i in range(1,e):
       p+=len(parEtage(i))
    jj+=p
    proche.config(command=lambda:confirmation(jj))

#pour avoir le plus proche emplacement libre
def plusproche(liste):
    l=0
    while (l<len(liste)):
       if (liste[l].state(debut,fin)==0):
          return l
       else:
          l+=1
    return -1

#lorsque le client clique sur etage le page passe à l'etage suivant jusqu'à revenir à le premier étage
def newEtage():
    global e
    e+=1
    if (parEtage(e)==[]):
        e=1
    global j
    j=0
    Affichage(e)

#cette methode donne une list des emplacement dans l'etage "numEtage"
def parEtage(numEtage):
    l=[]
    for c in list_emplacement:
        if (c.get_etage()==numEtage):
            l.append(c)
    return l

#cette methode retourne liste des information sur l'état de parking (combient d'emplacements libre combient occupée combient réservé) pendant les dates donnée par le client
def Info():
    inf=[0]*3
    for e in list_emplacement:
        if (e.state(debut,fin)==0):
            inf[0]+=1
        elif (e.state(debut,fin)==1):
            inf[1]+=1
        else:
            inf[2]+=1
    return inf

#affichage l'état du parking pendant les dates donnée [debut,fin]
def Affichage(etage=0):
    global debut
    global fin
    #la methode sera rappeler lorsque on clique sur etage pour afficher les emplacements de l'etage suivant
    #si l'affichage est pour la première fois
    if (etage==0):
        if(Methode==True):
           #si l'action est sur place on doit fermer "direct" et fixer la date de debut en le temps à l'instant 
           d=getint(duree.get())
           debut=datetime.datetime.now()
           fin = datetime.timedelta(minutes=d)+datetime.datetime.now()
           direct.destroy()
        else:
           #si l'action est une reservation
           d=getint(dure.get())
           fin=datetime.timedelta(minutes=d)+debut
           if (Recherche_Client(cin)==-1):
               #si le client est nouveau on doit sauvegarder le nom et les info avant de supprimer res (res.destroy())
               global nom
               global name
               name=str(nom.get())
           res.destroy()
        #création de aff
        global aff
        aff= Toplevel()
        aff['bg']='LightSkyBlue4'
        global e
        e=1

    #si l'affichage est appelée après clique sur étage
    else:
        aff.destroy()
        aff= Toplevel()
        aff['bg']='LightSkyBlue4'
        e=etage

    #e represante le numéro d'etage et j l'index de l'emplacement mais dans son étage n'est pas son général id

    if (etage==0): 
        affEmpl()
    else:
        global j
        affEmpl(j)
    #les informations du parking
    info=Info()

    libre=Label(aff,text="Emplacements Libres:\t"+str(info[0]),bg='LightSkyBlue4', fg="green")
    libre.grid(row=6,column=1, columnspan=5,pady=20)
    libre.config(font=("Roman bold", 13,"bold"))

    proche=Label(aff,text="L'Emplacement Le Plus Proche:\t"+str(plusproche(list_emplacement)+1000*list_emplacement[plusproche(list_emplacement)].get_etage()),bg='LightSkyBlue4', fg="yellow")
    proche.grid(row=7,column=1, columnspan=5,pady=20)
    proche.config(font=("Roman bold", 13,"bold"))

    reserv=Label(aff,text="Emplacements Reservés:\t"+str(info[2]),bg='LightSkyBlue4', fg="blue")
    reserv.grid(row=6,column=7, columnspan=5,pady=20)
    reserv.config(font=("Roman bold", 13,"bold"))

    occupe=Label(aff,text="Emplacements Occupées:\t"+str(info[1]),bg='LightSkyBlue4', fg="red")
    occupe.grid(row=7,column=7, columnspan=5,pady=20)
    occupe.config(font=("Roman bold", 13,"bold"))

    #bouton d'annulation
    annuler= Button(aff,text="Annuler",  bg='Deep Sky Blue3', fg="dark slate gray",height=2,width=12)
    annuler.grid(row=8,column=6)
    annuler.config(font=("Roman bold", 10,"bold"))
    annuler.config(command = lambda: Home(4))


def affEmpl(k=0):

    #Bouton de l'étage et lorsque on le clique il rappele la methode affichage mais pour l'étage e+1
    global e
    etage= Button(aff,text="ETAGE"+str(e),  bg='Deep Sky Blue3', fg="dark slate gray",height=2,width=12)
    etage.grid(row=1,column=6)
    etage.config(font=("Roman bold", 10,"bold"))
    etage.config(command=newEtage)  

    #l est la list des emplacement de ce étage 
    l=parEtage(e)
    n=len(l)
    #j est l'index de premier emplacement que l'on affichera
    global j
    j=k

    #p est un bouton qui navigue au emplacements prècedantes si ils existent
    if (j!=0):
        p=Button(aff,text="<", bg='Deep Sky Blue3', fg="dark slate gray",height=28)
        p.grid(row=2, column=0,rowspan=4)
        p.config(command=lambda:affEmpl(k-22))

    #affichages des boutons des emplacements selon leur état
    for i in range(0,11):
        #row1
        if (l[j].state(debut,fin)==0):
            if (plusproche(list_emplacement)==l[j].get_id()):
                ProcheBut1(aff,i,j)
            else:
                DispoBut1(aff,i,j)
        elif (l[j].state(debut,fin)==2):
            ResBut1(aff,i,j)
        else:
            OccupBut1(aff,i,j)
        #affichage des id des emplacements
        numEmpl= Label(aff,text=str(l[j].get_id()+(1000*e)),  bg='LightSkyBlue4', fg="dark slate gray",width=15)
        numEmpl.grid(row=2,column=i+1)
        j+=1
        if (j==n):
            #si la liste se termine
            break

        #row2
        else:
            if (l[j].state(debut,fin)==0):
                if (plusproche(list_emplacement)==l[j].get_id()):
                    ProcheBut2(aff,i,j)
                else:
                    DispoBut2(aff,i,l[j].get_id())
            elif (l[j].state(debut,fin)==2):
                ResBut2(aff,i,j)
            else:
                OccupBut2(aff,i,j)
        #affichage des id des emplacements
        numEmpl= Label(aff,text=str(l[j].get_id()+(1000*e)),  bg='LightSkyBlue4', fg="dark slate gray",width=15)
        numEmpl.grid(row=5,column=i+1)
        j+=1
        
        if (j==n):
            #si la liste se termine
            break
    #bouton qui affiche les prochaines 22 emplacement dans l'etage e si ils existent
    if(j<n):
        nextp=Button(aff,text=">", bg='Deep Sky Blue3', fg="dark slate gray",height=28)
        nextp.grid(row=2, column=13, columnspan=2, rowspan=4)
        nextp.config(command=lambda:nextt(k))

#methode pour afficher les prochaines 22 emplacement dans l'etage e si ils existent
def nextt(k):
    global j
    j=k+22
    Affichage(e)
#si le client clique sur un emplacement libre il doit confirme son choix
def choix(x):
    global list_emplacement
    global list_client

    #si une reservation sur place
    if (Methode):
        #change l'état de l'emplacement
        list_emplacement[x].occupe(fin)
        aff.destroy()
        #mise à jour de base de donnée
        bd.updateEmplacement(list_emplacement[x])
        #retourner au menu principal
        Home()

    #si c'est une réservation
    else:
        #change l'état de l'emplacement et mettre à jours la base de données 
        list_emplacement[x].add_reservation(debut,fin)
        bd.updateEmplacement(list_emplacement[x])
        
        if (Recherche_Client(cin)==-1):
        #si le client n'existe pas dans la base de donnée 
           c=Client(name,cin,x,True,[debut,fin])
           bd.addClient(c)
           list_client=bd.listClients()
        else:
        #si il exist 
           k=Recherche_Client(cin)
           list_client[k].reservation([debut,fin],x)
           bd.updateClient(list_client[k])
        aff.destroy()
        Home()

#l'alert de confirmation
def confirmation(x):
    global e
    MsgBox=messagebox.askquestion("Confirmation","Prière confirmer votre choix:\n\tEmplacement:"+str(list_emplacement[x].get_id()+e*1000)+"\n\tEtage:"+str(e)+"\n\tDebut:"+str(debut)+"\n\tFin:"+str(fin))

    if (MsgBox=='yes'):
        choix(x)
        
#main
Home()


        



