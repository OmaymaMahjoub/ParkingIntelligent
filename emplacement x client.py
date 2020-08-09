class Client:

    def __init__(self,cin,good_client=True,reservation=False):
        self.__cin=cin,
        #good_client become false if the client make more then 3 reservations and each time don't show up 
        self.__good_client=good_client
        #the client can't make another reservation if there is one still exist
        self.__reservation=reservation 

    def __getCin__(self):
        return self.__cin

    def can_make_reservation(self):
        return (self.__good_client and not(self.__reservation))

    def __setReservation__(self):
        self.__reservation= not(self.__reservation)

    def setBlackList(self):
        self.__good_client= not(self.__good_client)


class Emplacement:

    def __init__(self,N,state=0,hour=0):
        self.__N=N
        #State is 0 if the place is free 1 if rented and 2 if not available
        self.__state=state
        #hour it gives how much time the place will be not available or rented
        self.__hour

    def __getN__(self):
        return self.__N

    def __setHour__(self,h):
        self.__hour=h

    def __setState__(self,state):
        self.state=state



    
