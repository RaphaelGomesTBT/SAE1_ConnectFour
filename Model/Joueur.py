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


def getPlacerPionJoueur(joueur : dict):
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

