from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
            and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
        not type_plateau(joueur[const.PLATEAU])):
        return False
    return True


def construireJoueur(couleur : int) -> dict:
    """
    Fonction permettant de créer un dictionnaire contenant les informations du joueur

    :param couleur: Entier représentant la couleur (0 = jaune / 1 = rouge)
    :return: Dictionnaire contenant la couleur du joueur, le plateau ainsi que la fonction permettant de le faire jouer
    :raise TypeError: Si le paramètre n'est pas un entier
    :raise ValueError: Si l'entier donné n'est pas 0 ou 1
    """

    if type(couleur) != int :
        raise TypeError("construireJoueur : Le paramètre n'est pas un entier")
    elif couleur != 1 and couleur != 0:
        raise ValueError(f"construireJoueur : L’entier donné {couleur} n’est pas une couleur")

    joueur = {const.COULEUR : couleur, const.PLATEAU : None, const.PLACER_PION : None}
    return joueur

def getCouleurJoueur(joueur : dict)-> int:
    """
    Fonction qui retourne la couleur d'un joueur

    :param joueur: Dictionnaire représentant le joueur
    :return: Entier représentant la couleur (0 = jaune / 1 = rouge)
    :raise TypeError: Si le paramètre ne correspond pas à un joueur
    """
    if type_joueur(joueur) == False:
        raise TypeError("getCouleurJoueur : Le paramètre ne correspond pas à un joueur")
    couleur = joueur[const.COULEUR]
    return couleur


def getPlateauJoueur(joueur : dict) -> list:
    """
    Fonction qui retourne le plateau d'un joueur

    :param joueur: Dictionnaire représentant le joueur
    :return: Tableau 2D représentant le plateau de jeu
    :raise TypeError: Si le paramètre ne correspond pas à un joueur
    """

    if type_joueur(joueur) == False:
        raise TypeError("getPlateauJoueur : Le paramètre ne correspond pas à un joueur")
    plateau = joueur[const.PLATEAU]
    return plateau


def getPlacerPionJoueur(joueur : dict) -> callable:
    """
    Fonction qui retourne la fonction permettant au joueur de jouer

    :param joueur: Dictionnaire représentant le joueur
    :return: Fonction permettant au joueur de jouer
    :raise TypeError: Si le paramètre ne correspond pas à un joueur
    """

    if type_joueur(joueur) == False:
        raise TypeError("getPlacerPionJoueur : Le paramètre ne correspond pas à un joueur")
    fonction = joueur[const.PLACER_PION]
    return fonction


def getPionJoueur(joueur : dict) -> dict:

    if type_joueur(joueur) == False:
        raise TypeError("getPionJoueur : Le paramètre ne correspond pas à un joueur")

    couleur = getCouleurJoueur(joueur)
    pion = construirePion(couleur)
    return pion

def setPlateauJoueur(joueur : dict, plateau : dict) -> None:
    """
    Fonction permettant d'affecter un plateau à un joueur

    :param joueur: Dictionnaire représentant le joueur
    :param plateau: Tableau 2D représentant le plateau de jeu
    :return: La fonction ne retourne rien
    :raise TypeError: Si le premier paramètre ne correspond pas à un joueur
    :raise TypeError: Si le second paramètre ne correspond pas à un plateau
    """

    if type_joueur(joueur) == False:
        raise TypeError("setPlateauJoueur : Le premier paramètre ne correspond pas à un joueur")
    elif type_plateau(plateau) == False:
        raise TypeError("setPlateauJoueur : Le second paramètre ne correspond pas à un plateau")

    joueur[const.PLATEAU] = plateau
    return None


def setPlacerPionJoueur(joueur : dict, fonction : callable ) -> None:
    """
    Fonction permettant d'affecter la fonction permettant de jouer au joueur

    :param joueur: Dictionnaire représentant le joueur
    :param fonction: Fonction permettant au joueur de jouer
    :return: La fonction ne retourne rien
    :raise TypeError: Si le premier paramètre ne correspond pas à un joueur
    :raise TypeError: Si le second paramètre n'est pas une fonction
    """

    if type_joueur(joueur) == False:
        raise TypeError("setPlacerPionJoueur : Le premier paramètre ne correspond pas à un joueur")
    if callable(fonction) == False:
        raise TypeError("setPlacerPionJoueur : le second paramètre n’est pas une fonction")

    joueur[const.PLACER_PION] = fonction
    return None


from random import randint

def _placerPionJoueur(joueur : dict) -> int:
    """
    Fonction chosissant aléatoirement une colonne du plateau

    :param joueur: Dictionnaire représentant le joueur
    :return: Entier correspondant au numéro de la colonne choisie
    """
    if getModeEtenduJoueur(joueur) == True:
        nb = randint(-const.NB_LINES, const.NB_COLUMNS + const.NB_LINES - 1)
        plateau = getPlateauJoueur(joueur)
        while nb > 0 and nb < const.NB_COLUMNS - 1 and plateau[0][nb] != None:
            nb = randint(-const.NB_LINES, const.NB_COLUMNS + const.NB_LINES - 1)

    else:
        nb = randint(0,const.NB_COLUMNS - 1)
        plateau = getPlateauJoueur(joueur)
        while plateau[0][nb] != None:
            nb = randint(0, const.NB_COLUMNS - 1)
    return nb


def initialiserIAJoueur(joueur : dict, place : bool) -> None:
    """
    Fonction permettant d'affecter la fonction _placerPionJoueur au joueur

    :param joueur: Dictionnaire représentant le joueur
    :param place: Booléen avec la valeur True si le joueur joue en premier ou False s'il joue en second
    :return: La fonction ne retourne rien
    :raise TypeError: Si le premier paramètre n’est pas un joueur
    :raise TypeError: Si le second paramètre n’est pas un booléen
    """

    if type_joueur(joueur) == False:
        raise TypeError("initialiserIAJoueur : Le premier paramètre n’est pas un joueur")
    elif type(place) != bool:
        raise TypeError("initialiserIAJoueur : Le second paramètre n’est pas un booléen")

    setPlacerPionJoueur(joueur, _placerPionJoueur)
    return None


def getModeEtenduJoueur(joueur : dict) -> bool:
    """
    Fonction peremttant de savoir le mode de jeu du joueur

    :param joueur: Dictionnaire représentant le joueur
    :return: Booléen avec la valeur True si le joueur joue en mode étendu ou False dans le cas contraire
    :raise TypeError: Si le paramètre ne correspond pas à un joueur
    """

    if type_joueur(joueur) == False:
        raise TypeError("getModeEtenduJoueur : le paramètre ne correspond pas à un joueur")

    status = const.MODE_ETENDU in joueur
    return status




def setModeEtenduJoueur(joueur : dict, status : bool = True) -> None:
    """
    Fonction modifiant le mode de jeu du joueur

    :param joueur: Dictionnaire représentant le joueur
    :param status: Booléen avec la valeur True pour passer en mode étendu ou False pour le retirer
    :return: La fonction ne retourne rien
    :raise TypeError: Si le premier paramètre ne correspond pas à un joueur
    :raise TypeError: Si le second paramètre ne correspond pas à un booléen
    """

    if type_joueur(joueur) == False:
        raise TypeError("setModeEtenduJoueur : le premier paramètre ne correspond pas à un joueur")
    elif type(status) != bool:
        raise TypeError("setModeEtenduJoueur : le second paramètre ne correspond pas à un booléen")

    if status == True:
        joueur[const.MODE_ETENDU] = True
    else:
        del joueur[const.MODE_ETENDU]

    return None

