#MACHINE à PIZZA
blanche = 'blanche'
rouge = 'rouge'
medium = 'medium'
large = 'large'
reine = 'reine'
merguez = 'merguez'
taille = 'taille'
prix_reine_medium = '8.90'
prix_merguez_medium = '11.90'
prix_reine_large = '11.40'
prix_merguez_large = '14.40'

class pizza:
    def __init__(self, base_pizza, taille, type_p, prix):
        self.base_pizza = base_pizza
        self.taille = taille
        self.type = type_p
        self.prix = prix

    def base_blanche(self):
        print('Splash! Vous venez de mettre la base crème fraiche!')

    def base_rouge(self):
        print('Splash! Vous venez de mettre la base sauce tomate!')
    
    def pate_size(self, taille):
        print('ZIP! Vous avez choisi la taille', taille)
    
    def cuisson_pizza(self):
        print('La pizza est en cours de préparation')
    
    def prix_reine_m(self):
        print('Cela vous fera', prix_reine_medium, 'euros à regler.')
    
    def prix_merguez_m(self):
        print('Cela vous fera', prix_merguez_medium, 'euros à regler.')
    
    def prix_reine_L(self):
        print('Cela vous fera', prix_reine_large, 'euros à regler.')
    
    def prix_merguez_L(self):
        print('Cela vous fera', prix_merguez_large, 'euros à regler.')

    def mode_de_paiement(self):
        print('BIP! Paiement en cours...')

    def fin_de_cycle(self):
        print('Votre pizza', type_p, 'est prete. Bon appetit!')
        
    
reine = pizza(base_pizza='tomate', taille='medium' or 'large', type_p='reine', prix='8.90' or '11.40')
merguez = pizza(base_pizza='crème fraiche', taille= 'medium' or 'large', type_p='merguez', prix= '11.90' or '14.40')
 
type_p = input('Sélectionnez votre pizza (merguez ou reine) : ')


if type_p == 'reine':
    Base_pizza = input("Sélectionner la base de votre pizza (rouge ou blanche) : ")
    if Base_pizza == 'rouge':
        reine.base_rouge()
    elif Base_pizza == 'blanche':
        reine.base_blanche()
    taille = input('Choisissez la taille de votre pizza (medium ou large) : ')
    if taille == 'medium':
        reine.pate_size(taille)
        reine.prix_reine_m()
        mode_de_payement = input('Comment souhaitez-vous regler ? (Carte ou, Espèces & Tickets restaurants) : ')
        reine.mode_de_paiement()
        reine.cuisson_pizza()
        reine.fin_de_cycle()

    elif taille == 'large':
        reine.pate_size(taille)
        reine.prix_reine_L()
        mode_de_payement = input('Comment souhaitez-vous regler ? (Carte ou, Espèces & Tickets restaurants) : ')
        reine.mode_de_paiement()
        reine.cuisson_pizza()
        reine.fin_de_cycle()
    else:
        print('Saisie invalide, veuillez recommencer.')
        
elif type_p == 'merguez':
    Base_pizza = input("Sélectionner la base de votre pizza (rouge ou blanche): ")
    if Base_pizza == 'rouge':
        merguez.base_rouge()
    elif Base_pizza == 'blanche':
        merguez.base_blanche()
    
    taille = input('Choisissez la taille de votre pizza (medium ou large) : ')
    
    if taille == 'medium':
        merguez.pate_size(taille)
        merguez.prix_merguez_m()
        mode_de_payement = input('Comment souhaitez-vous regler ? (Carte ou, Espèces & Tickets restaurants) : ')
        merguez.mode_de_paiement()
        merguez.cuisson_pizza()
        merguez.fin_de_cycle()

    elif taille == 'large':
        merguez.pate_size(taille)
        merguez.prix_merguez_L()
        mode_de_payement = input('Comment souhaitez-vous regler ? (Carte ou, Espèces & Tickets restaurants) : ')
        merguez.mode_de_paiement()
        merguez.cuisson_pizza()
        merguez.fin_de_cycle()
    else:
        print('Saisie invalide, veuillez recommencer.')

else:
    print('Saisie invalide, veuillez recommencer.')


