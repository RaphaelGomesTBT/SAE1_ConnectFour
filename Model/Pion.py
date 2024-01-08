# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)

def construirePion(couleur : int) -> dict:
    """
    Fonction permettant de construire un pion

    :param couleur: Couleur du pion à construire
    :return: Dictionnaire représentant un pion
    :raise TypeError: Si le paramètre n'est pas un entier
    :raise ValueError: Si l'entier ne représente pas une couleur
    """
    if type(couleur) != int:
        raise TypeError("construirePion : le paramètre n'est pas de type entier")
    elif couleur != 0 and couleur != 1:
        raise ValueError(f"constuirePion : la couleur {couleur} n'est pas correcte")

    pion = {const.COULEUR : couleur, const.ID : None}
    return pion

def getCouleurPion(pion : dict) -> int:
    """
    Fonction permettant de recupérer la couleur d'un pion

    :param pion: dictionnaire représentant le pion
    :return: Entier représentant la couleur du pion (0 = jaune / 1 = rouge)
    :raise TypeError: Si le paramètre n'est pas un pion
    """
    if type_pion(pion) == False:
        raise TypeError("getCouleurPion : Le paramètre n'est pas un pion")

    couleur = pion[const.COULEUR]
    return couleur

def setCouleurPion(pion : dict, couleur : int) -> None:
    """
    Fonction permettant de changer la couleur d'un pion

    :param pion: dictionnaire représentant le pion
    :param couleur: Entier représentant la nouvelle couleur du pion (0 = jaune / 1 = rouge)
    :return: La fonction ne retourne rien
    :raise TypeError: Si le premier paramètre n'est pas un pion
    :raise TypeError: Si le second paramètre n'est pas un entier
    :raise ValueError: Si le second paramètre n'est pas une couleur (!= 0 ou 1)
    """

    if type_pion(pion) == False:
        raise TypeError("setCouleurPion : Le premier paramètre n'est pas un pion")
    elif type(couleur) != int :
        raise TypeError("setCouleurPion : Le second paramètre n'est pas un entier")
    elif couleur != 0 and couleur != 1:
        raise ValueError(f"setCouleurPion : Le second paramètre {couleur} n'est pas une couleur")

    pion[const.COULEUR] = couleur
    return None

def getIdPion(pion : dict) -> int:
    """
    Fonction permettant de recupérer l'identifiant d'un pion

    :param pion: dictionnaire repésentant le pion
    :return: Entier correspondant au numéro d'identifiant du pion (ou None si pas d'identifiant)
    :raise TypeError: Si le paramètre n'est pas un pion
    """
    if type_pion(pion) == False:
        raise TypeError("getIdPion : Le paramètre n'est pas un pion")

    id = pion[const.ID]
    return id

def setIdPion(pion : dict, id : int)-> None:
    """
    Fonction permettant de changer l'identifiant d'un pion

    :param pion: dictionnaire représentant le pion
    :param id: entier représentant le nouvel identifiant
    :return: La fonction ne retourne rien
    :raise TypeError: Si le premier paramètre n'est pas un pion
    :raise TypeError: Si le second paramètre n'est pas un entier
    """
    if type_pion(pion) == False:
        raise TypeError("setIdPion : Le premier paramètre n'est pas un pion")
    elif type(id) != int:
        raise TypeError("setIdPion : Le second paramètre n'est pas un entier")

    pion[const.ID] = id
    return None
