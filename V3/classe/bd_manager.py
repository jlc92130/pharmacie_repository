import sqlite3


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



    def add_client(self,clt):
        cmd = """INSERT INTO CLIENT (ID,NOM,PRENOM) VALUES('{}','{}','{}')""".format(clt.id,clt.surname,clt.name)
        cur = self.con.cursor()         # on demande a la bdd de renvoyer le curseur
        cur.execute(cmd)
        self.con.commit()
        cur.close()         # on ferme le curseur

    def verify_clt(self,id):
        cur = self.con.cursor()
        cur.execute("SELECT ID FROM CLIENT WHERE ID=id") # if no value id in table CLIENT
        if len(cur.fetchall()) == 0:
            return False
        else:
            return True

    def verify_medicine(self,id):
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



