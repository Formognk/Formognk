#Jeu du Pendu
mot_myst = "marie"

nb_vies = 7

mot_affiche = "_"*len(mot_myst)

lettre_trouvee =[]
print("Bienvenue dans le Jeu du Pendu!")
while nb_vies > 0 and mot_myst != mot_affiche:
    lettre = input("Veuillez saisir une lettre : ")
    if lettre in lettre_trouvee :
        print("Vous avez déjà deviné cette lettre. Réessayez.")  
    if lettre in mot_myst and lettre :
        print("Bien joué ! La lettre est dans le mot mystère.")
        lettre_trouvee.append(lettre) 
        for i in range(len(mot_myst)):
            if mot_myst[i] == lettre :
                mot_affiche = mot_affiche[:i] + lettre + mot_affiche[i + 1:]
    else:
        nb_vies -= 1   
                 
    if mot_affiche == mot_myst :
        print("Félicitations! Le mot mystère est", mot_myst)
    elif nb_vies == 0 :
        print("Game Over. Try again in the next one!") 
    else : 
        print ("Il vous reste", nb_vies, "vies restantes")
        print("Le mot est :", mot_affiche)
