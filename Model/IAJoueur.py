from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *
from Model.Joueur import *

def placerPionJoueurUpgrade(joueur : dict) -> int:
    plateau = getPlateauJoueur(joueur)
    couleur = joueur[const.COULEUR]
    couleurOpp = 0
    if couleur == 0:
        couleurOpp = 1

    if getModeEtenduJoueur(joueur) == False:
        nb = alignerNplus1(joueur,plateau,3, couleur)
        if nb == -1:
            nb = alignerNplus1(joueur,plateau,3, couleurOpp)
            if nb == -1:
                nb = alignerNplus1(joueur,plateau, 2 , couleur)
                if nb == -1:
                    nb = alignerNplus1(joueur,plateau,2 , couleurOpp)
                    if nb == -1:
                        nb = alignerNplus1(joueur,plateau,1,couleur)
                        if nb == -1:
                            nb = alignerNplus1(joueur,plateau, 1, couleurOpp)
                            if nb == -1:
                                nb = randint(0, const.NB_COLUMNS - 1)
                                while plateau[0][nb] != None:
                                    nb = randint(0, const.NB_COLUMNS - 1)


    return nb




def alignerNplus1(joueur : dict, plateau : list, n : int, couleur) -> int:

    couleur = getCouleurJoueur(joueur)
    nb = detecterNverticalPlateau(plateau,couleur, n)
    if nb == -1:
        nb = detecterNverticalPlateau(plateau,couleur, n)
        if nb == -1:
            nb = detecterNdiagonaleDirectePlateau(plateau, couleur, n)
            if nb == -1:
                nb = detecterNdiagonaleIndirectePlateau(plateau, couleur, n)
                if nb == -1:
                    nb = -1
    return nb







    status = False




def detecterNhorizontalPlateau(plateau : list, couleur : int, n : int) -> int:

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
                if j-1>0 and plateau[i][j-1] is None:
                    res = j-1
                    status = True
                elif j+compt < const.NB_COLUMNS and plateau[i][j+compt] is None:
                    res = j+compt
                    status = True
            elif compt > 0:
                j += compt+1
            else :
                j += 1
        i+=1
    return res


def detecterNverticalPlateau(plateau : list, couleur : int, n : int) -> int:


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
                if i-compt >= 0 and plateau[i-compt][j] is None:
                    res = j
                    status = True
            elif compt > 0:
                i -= compt + 1
            else:
                i -= 1
        j += 1
    return res



def detecterNdiagonaleDirectePlateau(plateau : list, couleur : int, n : int) -> int:
    """
    Fonction permettant de vérifier si 4 pion de la couleur choisie sont alignés sur une diagonale directe sur le plateau

    :param plateau: tableau 2D représentant le plateau de jeu
    :param couleur: Entier représentant la couleur des pions sélectionnés (0 = jaune / 1 = rouge)
    :return: Liste des pions (de la couleur choisie) alignés sur une diagonale directe par 4 sur le plateau
    :raise TypeError: Si le premier paramètre ne correspond pas à un plateau
    :raise TypeError: Si le second paramètre n'est pas un entier
    :raise ValueError: Si la valeur de la couleur n'est pas 0 ou 1
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
                elif i-1 > 0 and j-1 > 0 and plateau[i-1][j-1] is None:
                    res = j-1
                    status = True
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
    Fonction permettant de vérifier si 4 pion de la couleur choisie sont alignés sur une diagonale indirecte sur le plateau

    :param plateau: tableau 2D représentant le plateau de jeu
    :param couleur: Entier représentant la couleur des pions sélectionnés (0 = jaune / 1 = rouge)
    :return: Liste des pions (de la couleur choisie) alignés sur une diagonale indirecte par 4 sur le plateau
    :raise TypeError: Si le premier paramètre ne correspond pas à un plateau
    :raise TypeError: Si le second paramètre n'est pas un entier
    :raise ValueError: Si la valeur de la couleur n'est pas 0 ou 1
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
    while departj >= const.NB_COLUMNS-n and status == False:
        i = departi
        j = departj

        while j >= const.NB_COLUMNS-n and i <= const.NB_LINES-n and status == False:
            compt = 0
            while compt < n and type_pion(plateau[i + compt][j - compt]) and getCouleurPion(plateau[i + compt][j - compt]) == couleur:
                compt += 1
            if compt == n:
                if i+compt < const.NB_LINES and j-compt < const.NB_COLUMNS and plateau[i+compt][j-compt] is None:
                    res = j-compt
                    status = True
                elif i-1 > 0 and j+1 > 0 and plateau[i-1][j+1] is None:
                    res = j+1
                    status = True
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









