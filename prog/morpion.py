#==============================================================
#                  Morpion full by Me
#==============================================================

import random

#init affichage
print("Voila ma version du morpion, les case sont numéroté de 1 à 9. "
      "A chaque tour, le joueur doit entre le numéro correspondant a la case ou il veux jouer. "
      "L'ordinateur peut determiner le gagnant.")

#init jeu
n=0
tab = [".",".",".",".",".",".",".",".","."]
j=0
print(tab[0:3])
print(tab[3:6])
print(tab[6:9])
played = []

#choix du mode de jeu (PvP ou PvO)
mode = int(input("entrer le nombre de joueurs (1 contre l'ordinateur ou 2) : "))

#boucle principale PvP
if mode == 2:
    while n<9 and j==0:
        n+=1
        if n%2==0:
            case = int(input("le joueur 2 entre le numero de la case : "))
            while case in played:
                case = int(input("déja joué, essayez une autre case : "))
            tab[case-1] = "◊"
            played.append(case)
        else:
            case = int(input("le joueur 1 entre le numero de la case : "))
            while case in played:
                case = int(input("déja joué, essayez une autre case : "))
            tab[case-1] = "X"
            played.append(case)
        print(tab[0:3])
        print(tab[3:6])
        print(tab[6:9])

        #detection victoire
        for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            result = True
            for nb in combo:
                if tab[nb] != "X":
                    result = False
            if result==True:
                print("le joueur 1 à gagné")
                j=1
        for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            result = True
            for nb in combo:
                if tab[nb] != "◊":
                    result = False
            if result==True:
                print("l'ordinateur à gagné")
                j=1
    if n==9 and j==0:
        print("c'est un match nul")

#boucle principale PvO
if mode == 1:
    while n<9 and j==0:
        n+=1
        if n%2==0:
            case = int(input("le joueur 1 entre le numero de la case : "))
            while case in played:
                case = int(input("déja joué, essayez une autre case : "))
            tab[case-1] = "◊"
            played.append(case)
        else:

            #controle IA
            print("l'ordinateur joue : ")
            if n==1:
                case = 5
            else:
                case = random.randint(0,8)
                while case in played:
                    case = random.randint(0,8)
            tab[case] = "X"
            played.append(case)
        print(tab[0:3])
        print(tab[3:6])
        print(tab[6:9])

        #detection victoire
        for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            result = True
            for nb in combo:
                if tab[nb] != "X":
                    result = False
            if result==True:
                print("le joueur 1 à gagné")
                j=1
        for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            result = True
            for nb in combo:
                if tab[nb] != "◊":
                    result = False
            if result==True:
                print("l'ordinateur à gagné")
                j=1
    if n==9 and j==0:
        print("c'est un match nul")
