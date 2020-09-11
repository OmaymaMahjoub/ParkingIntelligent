from tkinter import * 

homePage = Tk()
homePage['bg']='gray'

voitureRUP=PhotoImage(file = r".\images\RCarUp.png")
voitureRDOWN=PhotoImage(file = r".\images\RCarDown.png")
voitureBUP=PhotoImage(file = r".\images\BCarUp.png")
voitureBDOWN=PhotoImage(file = r".\images\BCarDown.png")

#liste client tkoon global
#liste emplacemnt , w methode te3ha
#methode add client

Methode= True    # True direct , Fasle réservartion

#Vérification du client
def Recherche_Client(num):
   i=0
   test= False
   while (c in list_client):
       if (c.get_cin()==num.get()):
           test= True
           break
        else:
            i++
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
    reservation.config(command = gest_reservation )
    surplace=Button(homePage,text ="Parking direct", bg='red', )
    surplace.pack()
    surplace.config(command = parking_direct)
    homePage.mainloop()

#Parking sur place
def parking_direct():
    Methode=True
    homePage.destroy()
    direct = Tk()
    direct['bg']='gray'
    ed = Entry(direct, width= 60)
    ed.insert(0, "Bienvenue, merci d'indiquer la durée de votre visite et puis choisir votre emplacement")
    ed.pack()
    confirmd= Button(direct,text="Choisir", bg='red')
    confirmd.pack()
    confirmd.config(command = Affichage(direct,ed.get()))

#Gestion de reservartion
def gest_reservation():
    homePage.destroy()
    gres= Tk()
    gres['bg']='gray'
    labelr = Label(gres, text="Gestion de réservartion", bg="gray", fg="SlateBlue4" )
    labelr.config(font=("Roman bold", 30))
    labelr.pack()
    print("test")
    er=Entry(arg,width=60)
    er.insert(0,"Merci de nous fournir votre numéro de CIN")
    reserver = Button(gres,text="Reserver", bg="red")
    reserver.pack()
    reserver.config(command = reservartion(gres,er.get()) )

def reservartion(arg,num):
    arg.destroy():
    arg=Tk()
    arg['bg']='gray'
    Methode=False
    if ((Recherche_Client(num)!=-1)):
        if (!(list_client[Recherche_Client(num)].reservation_exist())):
            label= Label(arg,text="On est heureux de vous revoir chez nous, merci d'indiquer l'heure et la durée de votre visite et puis choisir votre emplacement,merci ", bg="gray",fg="SlateBlue4")
            label.config(font=("Roman bold", 30))
            label.pack()
            heure= Entry(arg, width=60)
            heure.insert(0,"L'heure de votre arrivé")
            dure= Entry(arg, width=60)
            dure.insert(0,"Durée") # bch taamel mise à jour 
            chosisir=Button(arg,text="Chosir votre emplacement")
            choisir.config(command=Affichage(arg,heure,dure)) #fct taamel l affichage
        else:
            #aando réser bch yconformi li hoa je 
            confirm=Button(arg,text="Confirmer")
            choisir.config(command= valider())        
    else:
            #création d'un client
            label= Label(arg,text="Merci pour avoir nous visiter, Merci d'indiquer votre nom")
            label.config(font=("Roman bold", 30))
            label.pack()
            nom= Entry(arg,width=60)
            nom.insert(0,"Votre nom")

            Client(num,nom.get()).add_client() # nouveau client

            heure= Entry(arg, width=60)
            heure.insert(0,"L'heure de votre arrivé")
            dure= Entry(arg, width=60)
            dure.insert(0,"Durée") # bch taamel mise à jour 
            chosisir=Button(arg,text="Chosir votre emplacement")
            choisir.config(command=Affichage(arg,heure,dure)) #fct taamel l affichag
        


#Affichage Parking
def Affichage(arg,h,d): #paramtre l durée wl wakt 
    arg.destroy()
    arg= Tk()
    arg['bg']='gray'
    #updateliste_emplacmenet()
    if (((len(list_emplacement))/2)==0):
        for i in range(len(list_emplacement)+1):
            if (i<(len(list_emplacement)/2)):
                if (list_emplacemnt[i]==0):
                    disponible= Button(arg,text="Emplacement Disponible",bg="green",command=choix(arg,i))
                    disponible.grid(row=1,column=i)
                elif (list_emplacement[i]==1):
                    reservé=Button(arg,text="Emplacement Reservé",image=voitureBDOWN,bg='blue',command=choix(arg,i))
                    reservé.grid(row=1,column=i)
                else:
                    occupé=Button(arg,text="Emplacement Occupé",image=voitureRDOWN,bg='red')
                    occupé.grid(row=1,column=i)
            else:
                if (list_emplacemnt[i]==0):
                        disponible= Button(arg,text="Emplacement Disponible",bg="green",command=choix(arg,i))
                        disponible.grid(row=2,column=i-(len(list_emplacement)/2))
                elif (list_emplacement[i]==1):
                        reservé=Button(arg,text="Emplacement Reservé",image=voitureBUP,bg='blue',command=choix(arg,i))
                        reservé.grid(row=2,column=i-(len(list_emplacement)/2))
                else:
                        occupé=Button(arg,text="Emplacement Occupé",image=voitureRUP,bg='red',command=choix(arg,i))
                        occupé.grid(row=2,column=i-(len(list_emplacement)/2))
    else:
        for i in range(len(list_emplacement)+1):
            if (i<((len(list_emplacement)+1)/2)):
                if (list_emplacemnt[i]==0):
                    disponible= Button(arg,text="Emplacement Disponible",bg="green",command=choix(arg,i))
                    disponible.grid(row=1,column=i)
                elif (list_emplacement[i]==1):
                    reservé=Button(arg,text="Emplacement Reservé",image="",bg='blue',command=choix(arg,i))
                    reservé.grid(row=1,column=i)
                else:
                    occupé=Button(arg,text="Emplacement Occupé",image=voiture,bg='red')
                    occupé.grid(row=1,column=i)
            else:
                if (list_emplacemnt[i]==0):
                        disponible= Button(arg,text="Emplacement Disponible",bg="green",command=choix(arg,i))
                        disponible.grid(row=2,column=i-((len(list_emplacement)+1)/2))
                elif (list_emplacement[i]==1):
                        reservé=Button(arg,text="Emplacement Reservé",image="",bg='blue',command=choix(arg,i))
                        reservé.grid(row=2,column=i-((len(list_emplacement)+1)/2))
                else:
                        occupé=Button(arg,text="Emplacement Occupé",image=voiture,bg='red',command=choix(arg,i))
                        occupé.grid(row=2,column=i-((len(list_emplacement)+1)/2))



#methode taa choix trod lista m réservation ==> occupé , w sinon tzid occupé  bl methode
def choix():
    if (Methode):
        #tzid juste occupé
    else:
        #tekhoo l res heki w trodha occupé


#main
Home()


        



