import random

def get_choices():
    player_choice = input("Entrer votre choix [ pierre,papier,ciseaux ] : ")
    choix_ordi = ["pierre","papier","ciseaux"]
    #Le cpu va choisir parmi les elements de la liste par hasard
    computer_choice = random.choice(choix_ordi)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"Vous avez choisi {player} ,l'ordinateur a choisi {computer}")
    if player == computer:
        return "egaliter"
    elif player == "pierre":
        if computer == "siceaux":
            return "La pierre detruit le siceaux: Vous avez gagner"
        else:
            return "Le papier enveloppe le pierre: Vous avez perdu"
    elif player == "papier":
        if computer == "pierre":
            return "Le papier enveloppe la pierre: Vous avez gagner"
        else:
            return "Le ciseaux coupe le papier: Vous avez perdu"
    elif player == "ciseaux":
        if computer == "papier":
            return "Le ciseaux coupe le papier: Vous avez gagner"
        else:
            return "La pierre detruit le ciseaux: Vous avez perdu"
#renvoie une dictionnaire
choices = get_choices()

#recuperation des elements de la dico
p_choix = choices["player"]
c_choix = choices["computer"]

#insertion des valeurs dans la fonction check_win
result = check_win(p_choix,c_choix)

#Affichage du gagnant
print(result)

