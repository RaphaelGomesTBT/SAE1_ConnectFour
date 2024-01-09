from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True


def construirePlateau()-> list:
    """
    Fonction permettant de construire la Plateau de jeu

    La fonction n'admet aucun paramètre
    :return: tableau 2D de 6 lignes et 7 colonnes ou toutes les cases ont pour valeur None
    """
    plateau = []
    for i in range(const.NB_LINES):
        ligne = []
        for j in range(const.NB_COLUMNS):
            ligne.append(None)
        plateau.append(ligne)
    return plateau


def placerPionPlateau(plateau : list, pion : dict, num_col : int) -> int:
    """
    Fonction permettant de déposer un pion dans une colonne du plateau

    :param plateau: tableau 2D représentant le plateau
    :param pion: dictionnaire représentant le plateau
    :param num_col: Entier correspondant au numéro de la colonne choisi pour déposer le pion
    :return: retourne un entier correspondant à la ligne où se trouve le pion déposé ou -1 si la colonne était déjà pleine
    :raise TypeError: Si le premier paramètre ne correspond pas à un plateau
    :raise TypeError: Si le second paramètre n’est pas un pion
    :raise TypeError: Si le troisième paramètre n’est pas un entier
    :raise ValueError: Si le valeur de la colonne n'est pas comprise entre 0 et 6
    """
    if type_plateau(plateau) == False:
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type_pion(pion) == False:
        raise TypeError("placerPionPlateau : Le second paramètre n’est pas un pion")
    elif type(num_col) != int :
        raise TypeError("placerPionPlateau : Le troisième paramètre n’est pas un entier")
    elif num_col < 0 or num_col >= const.NB_COLUMNS:
        raise ValueError(f"placerPionPlateau : La valeur de la colonne {num_col} n'est pas correcte")

    ligne = const.NB_LINES - 1
    while ligne >= 0 and plateau[ligne][num_col] != None:
        ligne -= 1
    if ligne >= 0:
        plateau[ligne][num_col] = pion
    return ligne

def toStringPlateau(plateau : list) -> str:
    """
    Fonction permettant de transformer le plateau en chaine de carractère

    :param plateau: tableau 2D représentant le plateau de jeu
    :return: Chaine de caractère représentant le plateau et les pions placés dedans
    """
    res = ""
    for i in range(const.NB_LINES):
        for j in range(const.NB_COLUMNS):
            res += "|"
            case = plateau[i][j]
            if type_pion(case):
                if case[const.COULEUR] == 0:
                    res += "\x1B[43m \x1B[0m"
                else :
                    res += "\x1B[41m \x1B[0m"
            else :
                res += " "
        res += "|\n"

    res += "-"*15
    res += "\n 0 1 2 3 4 5 6"
    return res


def detecter4horizontalPlateau(plateau : list, couleur : int) -> list:
    """
    Fonction permettant de vérifier si 4 pion de la couleur choisi sont alignés horizontalement sur le plateau

    :param plateau: tableau 2D représentant le plateau de jeu
    :param couleur: Entier représentant la couleur des pions sélectionnés (0 = jaune / 1 = rouge)
    :return: Liste des pions (de la couleur choisie) alignés horizontalement par 4 sur le plateau
    :raise TypeError: Si le premier paramètre ne correspond pas à un plateau
    :raise TypeError: Si le second paramètre n'est pas un entier
    :raise ValueError: Si la valeur de la couleur n'est pas 0 ou 1
    """
    if type_plateau(plateau) == False:
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : Le second paramètre n'est pas un entier")
    elif couleur != 0 and couleur != 1:
        raise ValueError(f"détecter4horizontalPlateau : La valeur de la couleur {couleur} n'est pas correcte")

    res = []
    for i in range(const.NB_LINES):
        j = 0
        while j <= 3 :
            compt = 0
            lst = []
            while compt <=3 and type_pion(plateau[i][j+compt]) and plateau[i][j+compt][const.COULEUR] == couleur:
                lst.append(plateau[i][j+compt])
                compt += 1
            if compt == 4 :
                res.extend(lst)
                j += 4
            elif compt >= 2:
                j += compt
            else :
                j += 1
    return res


def detecter4verticalPlateau(plateau : list, couleur : int) -> list:
    """
    Fonction permettant de vérifier si 4 pion de la couleur choisi sont alignés verticalement sur le plateau

    :param plateau: tableau 2D représentant le plateau de jeu
    :param couleur: Entier représentant la couleur des pions sélectionnés (0 = jaune / 1 = rouge)
    :return: Liste des pions (de la couleur choisie) alignés verticalement par 4 sur le plateau
    :raise TypeError: Si le premier paramètre ne correspond pas à un plateau
    :raise TypeError: Si le second paramètre n'est pas un entier
    :raise ValueError: Si la valeur de la couleur n'est pas 0 ou 1
    """

    if type_plateau(plateau) == False:
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    elif type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : Le second paramètre n'est pas un entier")
    elif couleur != 0 and couleur != 1:
        raise ValueError(f"détecter4verticalPlateau : La valeur de la couleur {couleur} n'est pas correcte")

    res = []
    for j in range(const.NB_COLUMNS):
        i = 0
        while i <= 2:
            compt = 0
            lst = []
            while compt <= 3 and type_pion(plateau[i+compt][j]) and plateau[i+compt][j][const.COULEUR] == couleur:
                lst.append(plateau[i+compt][j])
                compt += 1
            if compt == 4:
                res.extend(lst)
                i += 4
            elif compt >= 2:
                i += compt
            else:
                i += 1
    return res












