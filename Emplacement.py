#class datetime est utilisé dans les listes date_de_res et occupe
import datetime
import time

class Emplacement:

    def __init__(self,id,etage,date_res=[],occupe=[]):
        #id selon le plus proche à la porte
        self.__id=id
        self.__etage=etage
        #on peut avoir plusieurs réservations pour le meme emplacement pour des dates séparé l'element paire est l'heure de début de réservation est l'impaire de fin
        self.__date_res=date_res
        #occupé est une liste de deux elements la première est l'heure de début d'occupation la deuxième de fin
        self.__occupe=occupe
        

    def get_id(self):
        return self.__id

    def get_etage(self):
        return self.__etage

    def get_date_de_res(self):
        return self.__date_res

    def get_occupe(self):  
        return self.__occupe

    def state(self,debut,fin):
        #return 0 si l emplacement lire 1 si il est occupé et 2 si il est reservé pendant [debut,fin]
        if (len(self.__occupe)!=0):
            if (self.__occupe[-1]>debut):
                return 1
        if(len(self.__date_res)==0):
            return 0
        else:
            if(fin<=self.__date_res[0]):
                return 0
            else:
                i=1
                while(i<len(self.__date_res)-1):
                    if((debut>=self.__date_res[i])and(fin<=self.__date_res[i+1])):
                        return 0
                    else:
                        i+=2
                if(i==len(self.__date_res)-1):
                    if(debut>=self.__date_res[i]):
                        return 0
            return 2

    def update(self):
        if (len(self.__occupe)!=0):
            if(self.__occupe[-1]<=datetime.datetime.now()):
                self.libre()
        if (len(self.__date_res)!=0):
            n=1
            for i in range(1,len(self.__date_res),2):
                n+=2
                if (self.__date_res[i]>datetime.datetime.now()):
                    break
            if(n!=len(self.__date_res)):
                self.__date_res=self.__date_res[i+1:]
        print(self.__occupe)
        print(self.__date_res)

    def add_reservation(self,debut,fin):
        if (debut>=fin):
            print("Prière vérifiée la date")
            return False
        if( self.state(debut,fin)!=0):
            return False
        if (len(self.__date_res)==0):
            self.__date_res=[debut,fin]
        else:
            if(fin<=self.__date_res[0]):
                self.__date_res=[debut,fin]+self.__date_res
            else:
                i=1
                while(i<len(self.__date_res)-1):
                    if((debut>=self.__date_res[i])and(fin<=self.__date_res[i+1])):
                        self.__date_res.insert(i+1, debut)
                        self.__date_res.insert(i+2, fin)
                        return True
                    else:
                        i+=2
                if(i==len(self.__date_res)-1):
                    if(debut>=self.__date_res[i]):
                        self.__date_res=self.__date_res+[debut,fin]
                    else:
                        print("on ne peut pas faire une reservation à cette date")
                        return False
        return True


    def occupe(self,fin):
        if(fin<=datetime.datetime.now()):
            print("Prière vérifiée la date")
            return False
        elif (not(self.state(datetime.datetime.now(),fin)==0)):
            print("on ne peut pas avoir ce emplacement")
            return False
        else:
            self.__occupe=[datetime.datetime.now(),fin]
            return True

    def fin_reservation(self):
        if (len(self.__date_res)<=2):
            self.__date_res=[]
        else:
            self.__date_res=self.__date_res[2:]

    def libre(self):
        self.__occupe=[]


                    
