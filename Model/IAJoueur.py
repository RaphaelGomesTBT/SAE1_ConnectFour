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
        nb = -1
        i = 3
        while nb == -1 and i > 0:
            nb = alignerNplus1(joueur, plateau, i, couleur)
            if nb == -1:
                nb = alignerNplus1(joueur, plateau, i, couleurOpp)
            i -= 1
        if nb == -1:
            nb = randint(0, const.NB_COLUMNS - 1)
            while plateau[0][nb] != None:
                nb = randint(0, const.NB_COLUMNS - 1)
    else :
        nb = randint(-const.NB_LINES, const.NB_COLUMNS + const.NB_LINES - 1)
        while nb > 0 and nb < const.NB_COLUMNS - 1 and plateau[0][nb] != None:
            nb = randint(-const.NB_LINES, const.NB_COLUMNS + const.NB_LINES - 1)



    return nb




def alignerNplus1(joueur : dict, plateau : list, n : int, couleur : int) -> int:
    """
    Fonction permettant de trouver si une case est libre après un nombre n de cases alignées

    :param joueur: Dictionnaire représentant le joueur
    :param plateau: Tableau 2D représentant le plateau de jeu
    :param n: Entier correspondant au nombre de pion devant être alignés
    :param couleur: Entier correspondant à une couleur (0 = jaune/ 1 = rouge)
    :return: Entier correspondant à un numéro de colonne (ou -1 si aucune colonnes trouvées selon les critères)
    """


    nb = detecterNverticalPlateau(plateau, couleur, n)
    if nb == -1:
        nb = detecterNhorizontalPlateau(plateau, couleur, n)
        if nb == -1:
            nb = detecterNdiagonaleDirectePlateau(plateau, couleur, n)
            if nb == -1:
                nb = detecterNdiagonaleIndirectePlateau(plateau, couleur, n)

    return nb







    status = False




def detecterNhorizontalPlateau(plateau : list, couleur : int, n : int) -> int:
    """
    Fonction permettant de trouver si une case est libre avant ou après un nombre n de cases alignées horizontalement

    :param plateau: Tableau 2D représentant le plateau de jeu
    :param n: Entier correspondant au nombre de pion devant être alignés
    :param couleur: Entier correspondant à une couleur (0 = jaune/ 1 = rouge)
    :return: Entier correspondant à un numéro de colonne (ou -1 si aucune colonnes trouvées selon les critères)
    """

    if type_plateau(plateau) == False:
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : Le second paramètre n'est pas un entier")
    elif couleur != 0 and couleur != 1:
        raise ValueError(f"détecter4horizontalPlateau : La valeur de la couleur {couleur} n'est pas correcte")

    res = -1
    i = 0
    status = False
    while i < const.NB_LINES and status == False:
        j = 0
        while j <= const.NB_COLUMNS-n and status == False:
            compt = 0
            while compt < n and type_pion(plateau[i][j+compt]) and getCouleurPion(plateau[i][j+compt]) == couleur:
                compt += 1
            if compt == n :
                if j-1>=0 and plateau[i][j-1] is None:
                    res = j-1
                    status = True
                elif j+compt < const.NB_COLUMNS and plateau[i][j+compt] is None:
                    res = j+compt
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
    :return: Entier correspondant à un numéro de colonne (ou -1 si aucune colonnes trouvées selon les critères)
    """


    if type_plateau(plateau) == False:
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : Le second paramètre n'est pas un entier")
    elif couleur != 0 and couleur != 1:
        raise ValueError(f"détecter4verticalPlateau : La valeur de la couleur {couleur} n'est pas correcte")

    res = -1
    j = 0
    status = False
    while j < const.NB_COLUMNS and status == False :
        i = const.NB_LINES-1
        while i >= n and status == False:
            compt = 0
            while compt < n and type_pion(plateau[i-compt][j]) and getCouleurPion(plateau[i-compt][j]) == couleur:
                compt += 1
            if compt == n:
                if i-compt >= 0 and plateau[i-compt][j] == None:
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
    :return: Entier correspondant à un numéro de colonne (ou -1 si aucune colonnes trouvées selon les critères)
    """

    if type_plateau(plateau) == False:
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n'est pas un entier")
    elif couleur != 0 and couleur != 1:
        raise ValueError(f"détecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")

    res = -1
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
                if i+compt < const.NB_LINES and j+compt < const.NB_COLUMNS and plateau[i+compt][j+compt] is None:
                    res = j+compt
                    status = True
                elif i-1 >= 0 and j-1 >= 0 and plateau[i-1][j-1] is None:
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
    :return: Entier correspondant à un numéro de colonne (ou -1 si aucune colonnes trouvées selon les critères)
    """

    if type_plateau(plateau) == False:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) != int:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le second paramètre n'est pas un entier")
    elif couleur != 0 and couleur != 1:
        raise ValueError(f"détecter4diagonaleIndirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")

    res = -1
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
                if i+compt < const.NB_LINES and j-compt >= 0 and plateau[i+compt][j-compt] is None:
                    res = j-compt
                    status = True
                elif i-1 >= 0 and j+1 < const.NB_COLUMNS and plateau[i-1][j+1] is None:
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









