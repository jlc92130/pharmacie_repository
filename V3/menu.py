

import datetime
from classe.bd_manager import Manager  # on importe la classe Manager
from classe.client import Client
from classe.medicament import Medicament
 



m = manager("../basededonneepharmacy")  # relative bdd adress



def commande_client():
    client_surname = input("nom du client")
    client_name = input("prenom du client")
    client = find_client(client_surname,client_name) # return True if client exist False if not

    if not client:
        print("Le client {}, {} n'existe pas".format(client_name,client_surname))
        reponse = input("voulez vous rajouter dans la bdd ?(oui/non) ")
        if reponse == oui:       # rajouter clt dans la bdd  

    else:
      print("Le client")
      
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



menu = {"1" : commande_client, 
"2": "commande_fournisseur",
"3" :"etat_des_stock",
"4" : "Ajout_nouveau_medicament" ,
"5" : "ajout_nouveau_client",
"6" : " Quitter"}
print(menu)    

choix = input("entrer votre choix: ")
menu[choix]()       






