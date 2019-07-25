
class Pharmacy:

    def __init__(self):
        self.clients = []  # liste d'objet de clients
        self.medicaments = {} # dictionnaire

        self.total = {} # client.name clé et en value le montant de sa commande

    def addClient(self, client):

        # vérification de l'objet client est il dans la liste ?
        # stop les programme !!!
        if client in self.clients:
            raise Exception(
                "ce client {} est déjà dans la liste des clients".format(client.name))

        # si tu arrives ici c'est qu'il n'y a pas d'exception donc c'est un nouveau client
        self.clients.append(client)


    """

    """
    def addMedicament(self, medicament):
        # regarder si le produit est dans le dictionnaire

        if medicament.name in self.medicaments.keys():
            self.medicaments[medicament.name].quantity += medicament.quantity
            self.medicaments[medicament.name].price = medicament.price
            
        else:
            name = medicament.name # clé une chaine de caractères non mutable
            self.medicaments[name] = medicament

    """
    Methode buy pour acheter un medicament par client avec quantite

    """
    def buy(self, client, medicament, quantity = 1):  #ici client et medicament sont les objets

        # une exception arretera le programme
        if client not in self.clients or medicament.name not in self.medicaments.keys():
            raise Exception('le client {} ou le medicament {} n\'existe(nt) pas...'.format(client.name, medicament))
        
        if client.name not in self.total.keys():
            self.total[client.name] = 0

        self.total[client.name] += medicament.price * quantity

    def 



