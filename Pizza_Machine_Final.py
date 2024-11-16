class Pizza:
    def __init__(self, base, prix, diametre, style, ingredients):
        self.base = base
        self.prix = prix
        self.diametre = diametre
        self.style = style
        self.ingredients = ingredients
    
    def ajouter_ingredients(self, nouvel_ingredient):
        if nouvel_ingredient =="ananas":
            raise TypeError("Les ananas ne vont pas sur les pizzas")
        self.ingredients.append(nouvel_ingredient)
        self.prix = self.prix + 1
        
    
    def servir(self, table):
        print("J'ammène la pizza à la table", table)
    
    def livrer(self, adresse):
        print("Je livre la pizza à l'adresse :", adresse)

    def mode_de_paiement(self):
        print('BIP! Paiement en cours...')
    
    def fin_de_cycle(self):
        print('Votre pizza', pizza, 'est prete. Bon appetit!')



base = input("Sélectionner la base de votre pizza (tomate ou blanche) : ")
taille = input('Choisissez la diametre de votre pizza (medium ou large) : ')
style = input("Quelle style de pizza choisissez-vous?(calzone, margherita ou reine) : ")
ingredients = input("Quelle(s) ingredient(s) voulez-vous sur votre pizza? ")
lieu_repas = input("Préférez-vous manger sur place ou à emporter? (sur place ou à emporter) : ")



diametre = 30
if taille == 'grande':
    diametre = 35

ingredients = ingredients.split(', ')

prix = 5 + len(ingredients)

pizza = Pizza(
    base=base,
    diametre=diametre,
    style=style,
    ingredients=ingredients,
    prix=prix
)

print(pizza.ingredients, pizza.prix, 'euros')

payement = input("Comment souhaitez-vous regler ? (Carte ou, Espèces & Tickets restaurants) : ")
print('BIP! Paiement en cours...')

if lieu_repas == "sur place":
    table = input("quel est votre numéro de table? ")
    pizza.servir(table)
elif lieu_repas == "à emporter":
    adresse = input("Quelle est l'adresse de livraison? ")
    pizza.livrer(adresse)

ananas = input("Voulez-vous ajouter de l'ananas? (oui ou non) : ")
if ananas == "oui":
    pizza.ajouter_ingredients("ananas")

print('Votre pizza', style, 'est prete. Bon appetit!')

#J'AI REUSSI!!!