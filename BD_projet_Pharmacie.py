import os
import sqlite3
conn = sqlite3.connect('../basededonneepharmacy.db')  # creation du connecteur a la base de donnee 

print(os.getcwd())
c = conn.cursor()
#c.execute("""DROP TABLE MEDICAMENT""")
#c.execute("""DROP TABLE CLIENT""")
#c.execute("""DROP TABLE ACHAT""")

c.execute("""CREATE TABLE MEDICAMENT(ID INT PRIMARY KEY, NOM TEXT UNIQ, PRIX REAL, QUANTITE INT)""")
c.execute("""CREATE TABLE CLIENT(ID INT PRIMARY KEY, NOM TEXT, PRENOM TEXT, UNIQUE(NOM,PRENOM))""")
c.execute("""CREATE TABLE ACHAT(ID INT PRIMARY KEY, CLIENT_ID INT, MEDICAMENT_ID INT, DATE INT, PRIX REAL, QUANTITE INT,
FOREIGN KEY(CLIENT_ID) REFERENCES CLIENT(ID), FOREIGN KEY(MEDICAMENT_ID) REFERENCES MEDICAMENT(ID))""")



conn.commit()
conn.close()
