
class Pharmacy:

    def __init__(self):
        self.clients = []  # liste d'objet de clients [client1,client2....]
        self.medicaments = {} # dictionnaire {"nom_medoc":objetmedicament1,.....}
        self.commande_client = {} # clé (client.name), value le montant de sa commande à la date du jour, ex:{"toto":[(20,02/02/2018,"advil"),(50,02/06/2018,"rhino"),...],"titi":[(60,03/12/2018,"rhino")...],...}
        self.medicament_date = {}  # clé (medicament.name) value un tuple  montant de l'achat et date d'achat ex: {"advil":[(10,02/02/2018),(5,01/03/2018..],"aspro":[...],.....}
        self.CA_client = {}  # clé (client.name), value le montant du CA genere par un client entre 2 dates {"toto":120,"titi":150,...}
        self.CA_medicament = # clé (medicament) , value le CA généré par un medicament entre 2 dates

    def addClient(self, client):

        # vérification de l'objet client est il dans la liste ?
        # stop les programme !!!
        if client in self.clients:
            raise Exception(
                "Le client {} est deja dans la liste des clients".format(client.name))
        self.clients.append(client)
   
    def addMedicament(self, medicament):
        # regarder si le produit est dans le dictionnaire

        if medicament.name in self.medicaments.keys():
            self.medicaments[medicament.name].quantity += medicament.quantity
            self.medicaments[medicament.name].price = medicament.price
            
        else:
            name = medicament.name # clé une chaine de caractères non mutable
            self.medicaments[name] = medicament

    """
    Methode buy pour acheter x boites d'un medicament par un client à une date donnée

    """
    def client_buy_medicament(self, client, medicament, quantity = 1):  #ici client et medicament sont des objets, le client existe car soit il est ancien et deja présent dans la BDD
                                                             #soit nouveau et dans ce cas il a été ajouté au préalable dans la BDD
        if medicament.name not in self.medicaments.keys():
            raise Exception('le medicament {} n\'existe pas il faut le commander.'.format(medicament.name))
        
        if quantity > self.medicaments[name].quantity:           
            raise Exception("le nombre de {} en stock est de : {}".format(medicament.name,self.medicaments[name].quantity)
                            
        else:
            self.commande_client[client.name].append(medicament.price * quantity,datetime.datetime.today().strftime('%d/%m/%Y')) # est ce qu on ajoute bien un tuple a une liste???????
            self.medicament_date[medicament].append(medicament.price * quantity,datetime.datetime.today().strftime('%d/%m/%Y'))
            self.medicaments[medicament.name].quantity -= quantity  # Suite à l'achat du médicament, on met a jour sa quantite dans le stock
             
  

    def CA_client(self,client,date1,date2):          # Pour le client x on calcul combien il a depense entre 2 dates(date1<date2), client represente l'objet client
        for client.name in self.commande_client:
            for value in self.commande_client[client.name]:
                if date1 <= value[1] <= date2:
                    total += value[0]
        return total

    def CA_medicament(self,medicament,date1,date2):  # On calcul le CA genere par le medicament x entre 2 dates(date1<date2), medicament represente l'objet medicament
        for medicament.name in self.medicament_date:
            for value in self.medicament_date[medicament.name]:
                if date1 <= value[1] <= date2:
                    total += value[0]
        return total
            

        
    def withdraw_medicament(self,client,medicament,quantity):     # retirer un medicament de la commande avant validation commande
        self.medicaments[medicament.name].quantity += quantity  # on rajoute le nombre de boite dans le stock  
        self.commande_client[name] = 
        
    def cancel_order(self,client):            # on annule la commande
                              

    
        
        



