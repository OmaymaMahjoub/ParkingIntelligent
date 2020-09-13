import sqlite3
import datetime
import time
from Clients import Client
from Emplacement import Emplacement

class BD:
    def __init__(self,nomBD):
        self.nomBD=nomBD
        conn=sqlite3.connect(nomBD)
        curseur=conn.cursor()
        conn.commit()
        curseur.close()
        conn.close()
    
    def CreateParking(self,nbrEtage,nbrEmplacement):
    #nbrEmplacement est une liste qui porte le nombre des emplacement dans chaque etage
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        #creation de tableau de Parking
        sql1="CREATE TABLE PARKING(idEmp INTEGER PRIMARY KEY,idEtage INTEGER,reservation TEXT,occupe TEXT)"
        curseur.execute(sql1)
        #creation de tableau de clients
        sql2="CREATE TABLE CLIENT( cin INTEGER PRIMARY KEY, reservation INTEGER,idEmpl INTEGER,FOREIGN KEY(idEmpl) REFERENCES EMPLACEMENT(id))"
        curseur.execute(sql2)
        #ajouter les emplacement au BD
        n=0
        for i in range(0,nbrEtage):
            for j in range(0,nbrEmplacement[i]):
                sql3="insert into PARKING values (?,?,?,'')"
                curseur.execute(sql3,[n,i+1,datetime.datetime.now()])
                n+=1        
        conn.commit()
        curseur.close()
        conn.close()

    #client
    def listClients(self):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql="SELECT * FROM CLIENT"
        curseur.execute(sql)
        l=curseur.fetchall()
        clients=[]
        for i in range(0,len(l)):
            c=Client(l[i][0],l[i][2],l[i][1])
            clients+=[c]
        curseur.close()
        conn.close()
        return clients

    def addClient(self,client):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql="INSERT INTO CLIENT VALUES(?,?,?)"
        curseur.execute(sql,[client.get_cin(),client.reservation_exist(),client.get_emplacement()])
        conn.commit()
        curseur.close()
        conn.close()

    def updateClient(self,client):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql="UPDATE CLIENT SET reservation=? , idEmpl=? WHERE cin=?"
        curseur.execute(sql,[client.reservation_exist(),client.get_emplacement(),client.get_cin()])
        conn.commit()
        curseur.close()
        conn.close()

    def deleteClient(self,client):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql="DELETE FROM CLIENT WHERE cin=?"
        conn.execute(sql,[client.get_cin()])
        conn.commit()
        curseur.close()
        conn.close()

    def deleteAllClients(self,clients):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql="DELETE FROM CLIENT"
        conn.execute(sql,[client.get_cin()])
        conn.commit()
        curseur.close()
        conn.close()


    #Parking
        
    def stringtotime(self,c):
        l=c.split(" ")
        l1=l[0].split("-")
        l2=l[1].split(":")
        l2[2]=l2[2].split(".")[0]
        return datetime.datetime(int(l1[0]),int(l1[1]),int(l1[2]),int(l2[0]),int(l2[1]),int(l2[2]))
    
    def listEmplacement(self):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        #nombre des etages
        sql="SELECT MAX(idEtage) FROM PARKING"
        curseur.execute(sql)
        N=curseur.fetchall()[0][0]
        parking=[[0]]*N
        #liste des tuple des données
        sql2="SELECT * FROM PARKING "
        curseur.execute(sql2)
        l=curseur.fetchall()
        for i in range(len(l)):
            id=int(l[i][0])
            etage=int(l[i][1])
            #date reservation
            r=[]
            r=l[i][2].split("*")
            for j in range (0,len(r)):
                r[j]=self.stringtotime(r[j])
            #date occupée
            o=[]
            o=l[i][2].split("*")
            for j in range (0,len(o)):
                o[j]=self.stringtotime(o[j])
            emplacement=Emplacement(id,etage,r,o)
            parking[etage-1].append(emplacement)
        for i in range(0, len(parking)):
            parking[i].pop(0)
        curseur.close()
        conn.close()
        return parking

    def updateEmplacement(self,e):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        #time to string
        rstr=""
        r=e.get_date_de_res()
        for i in range (0,len(r)):
            rstr=rstr+"*"+str(r)
        ostr=""
        o=e.get_occupe()
        for i in range (0,len(o)):
            ostr=ostr+"*"+str(o)
        #update
        sql="UPDATE PARKING SET reservation=?, occupe=? WHERE idEmpl=?"
        curseur.execute(sql,[rstr,ostr,e.get_id()])
        curseur.commit()
        curseur.close()
        conn.close()
    
        
    

    
