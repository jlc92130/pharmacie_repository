import datetime
from classe.bd_manager import Manager  # on importe la classe Manager
from classe.client import Client
from classe.medicament import Medicament

 

def commande_client(manager):
    client_surname = input("nom du client: ")
    client_name = input("prenom du client: ")
    resultat = manager.find_client(client_surname,client_name)           # we are looking if the client is in db. 
                        # if client is in db we return an instance of the object client else we return None
    if not resultat:  # if resultat == None
      print("Le client {}, {} n'existe pas".format(client_name,client_surname))
      reponse = input("voulez vous le rajouter dans la bdd ?(oui/non) ")
      if reponse == "oui":
        manager.add_client(client_surname,client_name)       # we had the client in the database
    else:
      pass
      #quitter(manager)



            
# """  medicine = input("medicament vendu")
#     quantity = input("nombre de boites vendues")"""
#    # qte_en_stock = """SELECT QUANTITE FROM MEDICAMENT WHERE EXISTS(SELECT QUANTITE FROM MEDICAMENT WHERE MEDICAMENT = "medicine")"""
#         cur = m.con.cursor()
#         test = False
#         if ((cur.execute.fetchall()) < quantity) & (test == False):
#             print("le nombre de boites commandes est superieur au stock")
#             input("merci de saisir une nouvelle quantite")
#             test = False
#         else:
#             test = True

#         date = input("datetime.datetime.today().strftime('%Y-%m-%d')")
    
#         m.add_client(client)  # we add the client in the database
#         commande_client()            # we call again commande_client()                  

# """"



#def commande_fournisseur():
  #  if verify_medicine(medicament.id):
  #      medicament_name = input() 


m = Manager("../basededonneepharmacy.db")  # relative bdd adress

print("1 : commande_client", 
"2 : commande_fournisseur",
"3 : etat_des_stock",
"4 : Ajout_nouveau_medicament" ,
"5 : ajout_nouveau_client",
"6 :  Quitter",sep='\n')



"""todo test choix coherant"""

choix = input("entrer votre choix: ")

if choix == "1":
  commande_client(m)

else:
  print("vous avez fait une erreur de saisie")
  choix = input("entrer à nouveau votre choix: ")









