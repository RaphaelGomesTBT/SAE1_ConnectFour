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
                if getCouleurPion(case) == 0:
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
            while compt <=3 and type_pion(plateau[i][j+compt]) and getCouleurPion(plateau[i][j+compt]) == couleur:
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
    Fonction permettant de vérifier si 4 pion de la couleur choisie sont alignés verticalement sur le plateau

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
            while compt <= 3 and type_pion(plateau[i+compt][j]) and getCouleurPion(plateau[i+compt][j]) == couleur:
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



def detecter4diagonaleDirectePlateau(plateau : list, couleur : int) -> list:
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

    res = []
    departi = 2
    departj = 0
    while departj <= 3:
        i = departi
        j = departj

        while j <= 3 and i <= 2:
            lst = []
            compt = 0
            while compt <= 3 and type_pion(plateau[i+compt][j+compt]) and getCouleurPion(plateau[i+compt][j+compt]) == couleur:
                lst.append(plateau[i+compt][j+compt])
                compt += 1
            if compt == 4:
                res.extend(lst)
                i += 4
                j += 4
            elif compt >= 2:
                i += compt
                j += compt
            else:
                i += 1
                j += 1

        if departi > 0:
            departi -= 1
        else:
            departj += 1

    return res


def detecter4diagonaleIndirectePlateau(plateau : list, couleur : int) -> list:
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

    res = []
    departi = 2
    departj = const.NB_COLUMNS - 1
    while departj >= 3:
        i = departi
        j = departj

        while j >= 3 and i <= 2:
            lst = []
            compt = 0
            while compt <= 3 and type_pion(plateau[i + compt][j - compt]) and getCouleurPion(plateau[i + compt][j - compt]) == couleur:
                lst.append(plateau[i + compt][j - compt])
                compt += 1
            if compt == 4:
                res.extend(lst)
                i += 4
                j -= 4
            elif compt >= 2:
                i += compt
                j -= compt
            else:
                i += 1
                j -= 1

        if departi > 0:
            departi -= 1
        else:
            departj -= 1

    return res


def getPionsGagnantsPlateau(plateau : list) -> list:
    """
    Fonction permettant de recupérer la liste de tous les pions de même couleur alignés par 4 sur le plateau.

    :param plateau: Tableau 2D représentant le plateau de jeu
    :return: Liste composée de toutes les séries de 4 pions de même couleur alignés sur le plateau
    :raise TypeError: Si le paramètre n'est pas un plateau
    """

    if type_plateau(plateau) == False:
        raise TypeError("getPionsGagnantsPlateau : Le paramètre n'est pas une plateau")

    res = []
    for couleur in range(2):
        res.extend(detecter4horizontalPlateau(plateau, couleur))
        res.extend(detecter4verticalPlateau(plateau, couleur))
        res.extend(detecter4diagonaleDirectePlateau(plateau, couleur))
        res.extend(detecter4diagonaleIndirectePlateau(plateau, couleur))
    return res


def isRempliPlateau(plateau : list)-> bool:
    """
    Fonction permettant de déterminer si le plateau de jeu est rempli.

    :param plateau: Tableau 2D représentant le plateau de jeu
    :return: Booléen avec la valeur True si le plateau est rempli ou False dans le cas contraire
    :raise TypeError: Si le paramètre n'est pas un plateau
    """

    if type_plateau(plateau) == False:
        raise TypeError("isRempliPlateau : Le paramètre n'est pas un plateau")

    statut = True
    j = 0
    while j < const.NB_COLUMNS and statut == True:
        if plateau[0][j] == None:
            statut = False
        j += 1
    return statut


def placerPionLignePlateau(plateau : list, pion : dict, ligne : int, left : bool) -> tuple:
    """
    Fonction permettant de placer un pion sur une ligne du plateau.

    :param plateau: Tableau 2D représentant le plateau de jeu
    :param pion: Dictionnaire représentant le joueur
    :param ligne: Entier correspondant au numéro de la ligne jouée
    :param left: Booléen avec pour valeur True si le joueur joue à gauche ou False s'il joue à droite
    :return: Tuple comprenant la liste des pions poussée et un entier correspondant à la ligne ou se trouve le dernier pion de la liste
    :raise TypeError: Si le premier paramètre n’est pas un plateau
    :raise TypeError: Si le second paramètre n’est pas un pion
    :raise TypeError: Si le troisième paramètre n’est pas un entier
    :raise ValueError: Si le troisième paramètre n'est pas compris entre 0 et 5
    :raise TypeError: Si le quatrième paramètre n’est pas un booléen
    """
    if type_plateau(plateau) == False :
        raise TypeError("placerPionLignePlateau : Le premier paramètre n’est pas un plateau")
    elif type_pion(pion) == False :
        raise TypeError("placerPionLignePlateau : Le second paramètre n’est pas un pion")
    elif type(ligne) != int :
        raise TypeError("placerPionLignePlateau : le troisième paramètre n’est pas un entier")
    elif ligne < 0 or ligne >= const.NB_LINES :
        raise ValueError(f"placerPionLignePlateau : Le troisième paramètre {ligne} ne désigne pas une ligne")
    elif type(left) != bool :
        raise TypeError("placerPionLignePlateau : le quatrième paramètre n’est pas un booléen")

    lst = []
    lastLigne = None

    ## Insertion par la gauche
    if left == True:
        j = - 1
        while j < const.NB_COLUMNS - 1 and type_pion(plateau[ligne][j + 1]) == True:
            j += 1
            lst.append(plateau[ligne][j])

        if j == const.NB_COLUMNS - 1:
            lastLigne = const.NB_LINES


        else :
            i = ligne
            while i < const.NB_LINES - 1 and plateau[i + 1][j + 1] == None:
                i += 1

            if j == -1:
                plateau[i][j + 1] = pion

            else:
                plateau[i][j + 1] = plateau[ligne][j]

            if i != ligne:
                lastLigne = i

        if len(lst)>= 2:
            for idx in range(len(lst)-2, -1, -1):
                plateau[ligne][idx + 1] = plateau[ligne][idx]

        if len(lst) >= 1:
            plateau[ligne][0] = pion




        lst = [pion] + lst

    ## Insertion par la droite
    else:
        j = 7
        lst.append(pion)
        while j > 0 and type_pion(plateau[ligne][j - 1]) == True:
            j -= 1
            lst.append(plateau[ligne][j])

        if j == 0:
            lastLigne = const.NB_LINES


        else :
            i = ligne
            while i < const.NB_LINES - 1 and plateau[i + 1][j - 1] == None:
                i += 1

            if j == 7:
                plateau[i][j - 1] = pion

            else:
                plateau[i][j - 1] = plateau[ligne][j]

            if i != ligne:
                lastLigne = i

        if len(lst) >= 2:
            diff = const.NB_COLUMNS + 1 - len(lst)
            for idx in range(1, len(lst)-1):
                plateau[ligne][diff + idx - 1] = plateau[ligne][diff + idx]

        if len(lst) >= 2:
            plateau[ligne][6] = pion



    return (lst, lastLigne)


def encoderPlateau(plateau : list) -> str:
    """
    Fonction encodant le plateau de jeu en une chaine de carractère

    :param plateau: Tableau 2D représentant le plateau de jeu
    :return: Chaine de carractère représentant les cases du plateau (_ = vide | R = pion rouge | J = pion jaune)
    :raise TypeError: Si le paramètre ne correspond pas à un plateau
    """

    if type_plateau(plateau) == False :
        raise TypeError("encoderPlateau : le paramètre ne correspond pas à un plateau")

    PlateauStr = ""
    for i in range(const.NB_LINES):
        for j in range(const.NB_COLUMNS):
            if type_pion(plateau[i][j]) == True:
                if getCouleurPion(plateau[i][j])== 0:
                    PlateauStr += "J"
                else:
                    PlateauStr += "R"
            else:
                PlateauStr += "_"
    return PlateauStr


def isPatPlateau(plateau : list, hist : dict)-> bool:
    """
    Fonction vérifiant si le plateau de jeu à déjà été identique 5 fois.

    :param plateau: Tableau 2D représentant le plateau de jeu
    :param hist: Dictionnaire sauvegardant les versions du plateau et leur nombre d'apparition
    :return: Booléen avec la valeur True si le plateau à déjà été identique 5 fois ou False dans le cas contraire
    :raise TypeError: Si le premier paramètre n’est pas un plateau
    :raise TypeError: Si le second paramètre n’est pas un dictionnaire
    """

    if type_plateau(plateau) == False:
        raise TypeError("isPatPlateau : Le premier paramètre n’est pas un plateau")
    elif type(hist) != dict:
        raise TypeError("isPatPlateau : Le second paramètre n’est pas un dictionnaire")

    status = False
    cle = encoderPlateau(plateau)
    if cle in hist:
        hist[cle] = hist[cle] + 1
        if hist[cle] >= 5:
            status = True
    else:
        hist[cle] = 1

    return status














