import sqlite3
from classe.client import Client


class Manager:

    # Add client 
    # Add Medicaments
    # Update medicine stock
    # Check medicine stock   
    # Add purchase stock      ???? c est quoi la difference avec update
    # get list client
    # get list medicament
    # get purchase client 
    # get purchase by_date

           

    def __init__(self,path_db):
        self.path_db = path_db
        self.con = sqlite3.connect(path_db)

    """def curseur(self,cmd):    est ce que c est bon ?
        cur = self.con.cursor()
        cur.execute(cmd)
        self.con.commit()
        cur.close()"""


    def find_client(self,surname,name):  # function that look in database if the client is already there
        #cmd = """SELECT NOM,PRENOM from CLIENT WHERE NOM={} PRENOM={} """.format(surname,name)
        cmd = """SELECT * FROM CLIENT """
        # self.curseur(cmd)  est ce que c est bon  ??
        cur = self.con.cursor()
        cur.execute(cmd)
        self.con.commit()
        data = cur.fetchall() # data is a list of tuple(the row of CLIENT table)
        cur.close()
        for row in data:
            if row[1] == "surname" and row[2] == "name":
                id_ = cur.fetchone()[0] # cur is a tuple with id, surname, name
                nom = cur.fetchone()[1]
                prenom = cur.fetchone()[2]
                client = Client(id_,nom,prenom)
                return client   # return client object
                break      
        return None    


    def add_client(self,nom,prenom):
        client = self.creation_client(nom,prenom)
           
# we add client in database
        cmd = """INSERT INTO CLIENT (ID,NOM,PRENOM) VALUES('{}','{}','{}')""".format(id_,client.surname,client.name)
        cur = self.con.cursor()         # on demande a la bdd de renvoyer le curseur
        cur.execute(cmd)
        self.con.commit()
        cur.close()         # we close cursor
        # retourner l objet clt

        # recherche le 1er id libre dans la table client 
    def premier_identifiant_vacant(table_id):
        """find the first missing value of an ordered list that begin by 1
            liste_id: an ordered list of integer that start at one
            return: integer"""
        cmd = """SELECT ID FROM {}""".format(table_id)     
        cur = self.con.cursor()
        cur.execute(cmd)
        self.con.commit()
        cur.close()
        liste_id = cur.fetchall()  # we get the list of all the row of ID column
        for i,v in enumerate(liste_id):
            if (i+1)!=v:
                return i+1
        return len(liste)+1

        
        # we create client object
    def creation_client(nom,prenom):
        table_id_client = """CLIENT"""
        id_ = self.premier_identifiant_vacant(table_id_client)
        client = Client(id_,nom,prenom)
        return client

        

    def client_exist(self,id):
        cur = self.con.cursor()
        cur.execute("SELECT ID FROM CLIENT WHERE ID=id") # if no value id in table CLIENT
        if len(cur.fetchall()) == 0:
            return False
        else:
            return True

    def medicine_exist(self,id):
        cur = self.con.cursor()
        cur.execute("SELECT ID FROM MEDICAMENT WHERE ID=id") # if no id in table MEDICAMENT 
        if len(cur.execute.fetchall())==0:
            return False
        else:
            return True


    def add_medicine(self,md):
        cmd = """INSERT INTO MEDICAMENT (ID, NOM, PRIX, QUANTITE) VALUES('{}','{}','{}',{}')""".format(md.id,md.name,md.price,md.quantity)
        cur = self.con.cursor()
        cur.execute(cmd)
        self.con.commit()
        cur.close()

    def check_medicine_stock(self,md):      # retourne le stock pour un medicament donne
        cur = self.con.cursor()
        cmd = """SELECT NOM,QUANTITE FROM MEDICAMENT WHERE VALUES('{}')""".format(md.id)
        cur.execute(cmd)
        cur.close()

        print(cur)



    def update_cl_medicine_stock(self,md):
        cmd="""SELECT QUANTITE FROM MEDICAMENT WHERE VALUES('{}')""".format(md.name)
        cur = self.con.cursor()
        cur.execute(cmd)
        resultat = cur.fetchone()
        quantity_old = resultat[0]
        self.con.commit()
        new_quantity = quantity_old - md.quantity
        # Je souhaite injecter new_quantity dans la bdd en lieu et place de la valeur presente, comment ecraser un enregistrement dans une bdd  ?

        #le client achete x boite de medicament. On soustrait x a la valeur en bdd pour mettre a jour le stock


    def update_ph_medicine_stock(self,md):
        cmd="""SELECT QUANTITE FROM MEDICAMENT WHERE VALUES('{}')""".format(md.name)
        cur = self.con.cursor()
        cur.execute(cmd)
        resultat = cur.fetchone()
        quantity_old = resultat[0]
        self.con.commit()
        new_quantity = quantity_old + md.quantity

        #le pharmacien achete y boites de medicament au fournisseur on ajoute ces boites a la quantite presente en bdd 
        


    def get_list_client(self):
        cur = self.con.cursor()
        cmd = """SELECT ID,NOM,PRENOM FROM CLIENT"""
        cur.execute(cmd)
        raw = cur.fetchone()
        while row is not None:
            print(row[0],row[1],row[2])
            row = cur.fechone()
        cur.close()



