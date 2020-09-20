import datetime
import time

class Client:

    def __init__(self,nom,cin,idEmpl=-1,res_exist=False,periode=[]):
        self.__nom=nom
        self.__cin=cin
        #chaque client ne peut pas faire une reservation si une autre existe.
        self.__res_exist=res_exist
        self.__idEmpl=idEmpl
        self.__periode=periode
        

    def res_finis(self):
        self.__res_exist=False
        self.__periode=[]
        self.__idEmpl=-1

    def reservation(self,periode,idEmpl):
        if (self.__res_exist):
            print("ce client ne peut pas faire une reservation")
            return False
        else:
            self.__res_exist= True
            self.__idEmpl=idEmpl
            self.__periode=periode
            return True

    #Getter & setter

    def get_nom(self):
        return self.__nom
    
    def get_cin(self):
        return self.__cin

    def reservation_exist(self):
        if(len(self.__periode)!=0):
            if (self.__periode[-1]<=datetime.datetime.now()):
                self.res_finis()
        return self.__res_exist

    def get_emplacement(self):
        return self.__idEmpl

    def get_periode(self):
        return self.__periode
    
    
