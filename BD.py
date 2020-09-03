import sqlite3


class BD:
    def __init__(self,nomBD):
        self.nomBD=nomBD
        self.conn=sqlite3.connect(nomBD)
        self.curseur=conn.cursor()
    
    def CreateTabl 
