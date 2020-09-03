class Client:

    def __init__(self,cin,res_exist=True):
        self.__cin=cin
        #chaque client ne peut pas faire une reservation si une autre existe.
        self.__res_exist=res_exist

    def res_finis(self):
        self.__res_exist=False

    def reservation(self):
        if (self.__res_exist):
            print("ce client ne peut pas faire une reservation")
            return False
        else:
            self.__res_exist= True
            return True

    #Getter & setter

    def get_cin(self):
        return self.__cin

    def set_cin(self,cin):
        self.__cin=cin

    def reservation_exist(self):
        return self.__res_exist

    
