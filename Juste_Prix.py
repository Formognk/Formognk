print("Bienvenue dans le Juste Prix!")
Juste_Prix = 6
nbvies = 5
while nbvies > 0 : 
    Answer = int(input("Devinez le juste prix! Le nombre est compris entre 1 et 10 : "))
    if Answer < 6 :
        nbvies -= 1
        print("Dommage, c'est plus! Retentez votre chance!")
    elif Answer > 6 :
        nbvies -= 1
        print("Dommage, c'est moins! Retentez votre chance!")
    elif Answer == Juste_Prix :
        print("Felicitations! Le juste prix était,", Juste_Prix)
        break
    if nbvies == 0 :
        print("C'est la fin du jeu, dommage! Réessayez encore.")