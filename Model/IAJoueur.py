from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *
from Model.Joueur import *

def placerPionJoueurUpgrade(joueur : dict) -> int:
    """
    Fonction permettant de retourner le coup jouer par l'IA en analysant les différentes possibilités

    :param joueur: Dictionnaire représentant le joueur
    :return: Entier correspondant au numéro de la colonne selectionnée
    """
    plateau = getPlateauJoueur(joueur)
    couleur = joueur[const.COULEUR]
    couleurOpp = 0
    if couleur == 0:
        couleurOpp = 1


    if getModeEtenduJoueur(joueur) == False:
        nb = -7
        i = 3
        while nb == -7 and i > 0: ## Cherche le premier coup pouvant être joué en regardant d'abord les pion alignés par 3, puis 2, puis 1 en prenant en priorité la couleur jouant.
            nb = alignerNplus1(joueur, plateau, i, couleur, False)
            if nb == -7:
                nb = alignerNplus1(joueur, plateau, i, couleurOpp, False)
            i -= 1
        if nb == -7: ## Selection aléatoire de la colonnes
            nb = randint(0, const.NB_COLUMNS - 1)
            while plateau[0][nb] != None:
                nb = randint(0, const.NB_COLUMNS - 1)
    else :
        nb = -7
        i = 3
        while nb == -7 and i > 0: ## Cherche le premier coup pouvant être joué en regardant d'abord les pion alignés par 3, puis 2, puis 1 en prenant en priorité la couleur jouant.
            nb = alignerNplus1(joueur, plateau, i, couleur, True)
            if nb == -7:
                nb = alignerNplus1(joueur, plateau, i, couleurOpp, True)
            i -= 1
        if nb == -7: ## Selection aléatoire de la colonnes ou de la ligne

            nb = randint(-const.NB_LINES, const.NB_COLUMNS + const.NB_LINES - 1)
            while nb > 0 and nb < const.NB_COLUMNS - 1 and plateau[0][nb] != None:
                nb = randint(-const.NB_LINES, const.NB_COLUMNS + const.NB_LINES - 1)

    return nb




def alignerNplus1(joueur : dict, plateau : list, n : int, couleur : int, modeE : bool) -> int:
    """
    Fonction permettant de trouver si une case est libre après un nombre n de cases alignées

    :param joueur: Dictionnaire représentant le joueur
    :param plateau: Tableau 2D représentant le plateau de jeu
    :param n: Entier correspondant au nombre de pion devant être alignés
    :param couleur: Entier correspondant à une couleur (0 = jaune/ 1 = rouge)
    :param modeE: Booléen indiquant si le joueur joue en mode etendu ou non
    :return: Entier correspondant à un numéro de colonne (ou -7 si aucune colonnes trouvées selon les critères)
    """


    nb = detecterNverticalPlateau(plateau, couleur, n) ## Cherche si n pions sont alignés verticalement
    if nb == -7:
        nb = detecterNhorizontalPlateau(plateau, couleur, n, modeE) ## Sinon cherche si n pions sont alignés horizontalement
        if nb == -7:
            nb = detecterNdiagonaleDirectePlateau(plateau, couleur, n) ## Sinon cherche si n pions sont alignés sur une diagonale directe
            if nb == -7:
                nb = detecterNdiagonaleIndirectePlateau(plateau, couleur, n) ## Sinon cherche si n pions sont alignés sur une diagonale indirecte

    return nb









def detecterNhorizontalPlateau(plateau : list, couleur : int, n : int, modeE : bool) -> int:
    """
    Fonction permettant de trouver si une case est libre avant ou après un nombre n de cases alignées horizontalement

    :param plateau: Tableau 2D représentant le plateau de jeu
    :param n: Entier correspondant au nombre de pion devant être alignés
    :param couleur: Entier correspondant à une couleur (0 = jaune/ 1 = rouge)
    :param modeE: Booléen indiquant si le joueur joue en mode etendu ou non
    :return: Entier correspondant à un numéro de colonne (ou -7 si aucune colonnes trouvées selon les critères)
    """

    res = -7
    i = 0
    status = False
    while i < const.NB_LINES and status == False: ## boucle sur chaque ligne
        j = 0
        while j <= const.NB_COLUMNS-n and status == False:
            compt = 0
            while compt < n and type_pion(plateau[i][j+compt]) and getCouleurPion(plateau[i][j+compt]) == couleur: ## compte le nombre de pion alignés
                compt += 1
            if compt == n :
                if j-1>=0 and verificationPlacement(plateau, i, j-1) == True: ## Vérifie si le pion peut être placé avant
                    res = j-1
                    status = True
                elif j+compt < const.NB_COLUMNS and verificationPlacement(plateau, i, j+compt) == True: ## Vérifie si le pion peut être placé après
                    res = j+compt
                    status = True
                elif j-1<0 and modeE == True: ## Vérifie si le pion peut être poussé avant
                    res = i - 1 - 2*i
                    status = True
                elif j + compt == const.NB_COLUMNS and modeE == True: ## Vérifie si le pion peut être poussé après
                    res = i + const.NB_COLUMNS
                    status = True
                else :
                    j += compt+1
            elif compt > 0:
                j += compt+1
            else :
                j += 1
        i+=1
    return res


def detecterNverticalPlateau(plateau : list, couleur : int, n : int) -> int:
    """
    Fonction permettant de trouver si une case est libre après un nombre n de cases alignées verticalement

    :param plateau: Tableau 2D représentant le plateau de jeu
    :param n: Entier correspondant au nombre de pion devant être alignés
    :param couleur: Entier correspondant à une couleur (0 = jaune/ 1 = rouge)
    :return: Entier correspondant à un numéro de colonne (ou -7 si aucune colonnes trouvées selon les critères)
    """


    if type_plateau(plateau) == False:
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : Le second paramètre n'est pas un entier")
    elif couleur != 0 and couleur != 1:
        raise ValueError(f"détecter4verticalPlateau : La valeur de la couleur {couleur} n'est pas correcte")

    res = -7
    j = 0
    status = False
    while j < const.NB_COLUMNS and status == False :
        i = const.NB_LINES-1
        while i >= n and status == False:
            compt = 0
            while compt < n and type_pion(plateau[i-compt][j]) and getCouleurPion(plateau[i-compt][j]) == couleur:
                compt += 1
            if compt == n:
                if i-compt >= 0 and plateau[i-compt][j] == None: ## Vérifie si le pion peut être placé au dessus
                    res = j
                    status = True
                else:
                    i -= compt + 1
            elif compt > 0:
                i -= compt + 1
            else:
                i -= 1
        j += 1
    return res



def detecterNdiagonaleDirectePlateau(plateau : list, couleur : int, n : int) -> int:
    """
    Fonction permettant de trouver si une case est libre avant ou après un nombre n de cases alignées sur une diagonale directe

    :param plateau: Tableau 2D représentant le plateau de jeu
    :param n: Entier correspondant au nombre de pion devant être alignés
    :param couleur: Entier correspondant à une couleur (0 = jaune/ 1 = rouge)
    :return: Entier correspondant à un numéro de colonne (ou -7 si aucune colonnes trouvées selon les critères)
    """

    if type_plateau(plateau) == False:
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n'est pas un entier")
    elif couleur != 0 and couleur != 1:
        raise ValueError(f"détecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")

    res = -7
    departi = const.NB_LINES-n
    departj = 0
    status = False
    while departj <= const.NB_COLUMNS-n and status == False:
        i = departi
        j = departj

        while j <= const.NB_COLUMNS-n and i <= const.NB_LINES-n and status == False:
            compt = 0
            while compt < n and type_pion(plateau[i+compt][j+compt]) and getCouleurPion(plateau[i+compt][j+compt]) == couleur:
                compt += 1
            if compt == n:
                if i+compt < const.NB_LINES and j+compt < const.NB_COLUMNS and verificationPlacement(plateau, i+compt, j+compt) == True: ## Vérifie si le pion peut être placé après
                    res = j+compt
                    status = True
                elif i-1 >= 0 and j-1 >= 0 and verificationPlacement(plateau, i-1, j-1) == True: ## Vérifie si le pion peut être placé avant
                    res = j-1
                    status = True
                else:
                    i += compt + 1
                    j += compt + 1
            elif compt > 1:
                i += compt + 1
                j += compt + 1
            else:
                i += 1
                j += 1

        if departi > 0:
            departi -= 1
        else:
            departj += 1

    return res


def detecterNdiagonaleIndirectePlateau(plateau : list, couleur : int, n : int) -> int:
    """
    Fonction permettant de trouver si une case est libre avant ou après un nombre n de cases alignées sur une diagonale indirecte

    :param plateau: Tableau 2D représentant le plateau de jeu
    :param n: Entier correspondant au nombre de pion devant être alignés
    :param couleur: Entier correspondant à une couleur (0 = jaune/ 1 = rouge)
    :return: Entier correspondant à un numéro de colonne (ou -7 si aucune colonnes trouvées selon les critères)
    """

    if type_plateau(plateau) == False:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) != int:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le second paramètre n'est pas un entier")
    elif couleur != 0 and couleur != 1:
        raise ValueError(f"détecter4diagonaleIndirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")

    res = -7
    departi = const.NB_LINES - n
    departj = const.NB_COLUMNS - 1
    status = False
    while departj >= n and status == False:
        i = departi
        j = departj

        while j >= n and i <= const.NB_LINES-n and status == False:
            compt = 0
            while compt < n and type_pion(plateau[i + compt][j - compt]) and getCouleurPion(plateau[i + compt][j - compt]) == couleur:
                compt += 1
            if compt == n:
                if i+compt < const.NB_LINES and j-compt >= 0 and verificationPlacement(plateau, i+compt, j-compt) == True: ## Vérifie si le pion peut être placé après
                    res = j-compt
                    status = True
                elif i-1 >= 0 and j+1 < const.NB_COLUMNS and verificationPlacement(plateau, i-1, j+1) == True: ## Vérifie si le pion peut être placé avant
                    res = j+1
                    status = True
                else:
                    i += compt + 1
                    j -= compt + 1
            elif compt > 1:
                i += compt + 1
                j -= compt + 1
            else:
                i += 1
                j -= 1

        if departi > 0:
            departi -= 1
        else:
            departj -= 1

    return res


def verificationPlacement(plateau : list, i : int, j :int) -> bool:
    """
    Fonction vérifiant si la case trouver est disponible et si elle peut être jouée (pas de trou en dessous)

    :param plateau: Tableau 2D représentant le plateau de jeu
    :param i: Entier correspondant à la ligne de la case
    :param j: Entier correspondant à la colonne de la case
    :return: Booléen avec la valeur True si la case peut être joué ou False sinon
    """
    status = False
    if plateau[i][j] is None:
        status = True
        if i < const.NB_LINES -1 and plateau[i+1][j] is None:
            status = False
    return status







