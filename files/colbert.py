"""
    TP		: 1
    file 	: colbert.py
    author 	: ...
    date	: 19/09/2024
"""

from tris import *
from collections import namedtuple

eleve = namedtuple("Eleve", ["id", "genre", "birth"])

def creer_date(d:str) -> tuple:
    """
        d est une chaine de la forme "jj/mm/aaaa"
        En sortie, on souhaite avoir (jj, mm, aaaa)
        
        Exemple :
        >>> creer_date("22/07/1987")
        (22, 7, 1987)
    """
    pass

def creer_eleve(L:list) -> tuple:
    """
        L est une liste de chaines de caractères.
        Par exemple ["WROBEL David", "22/07/1987", "G"]
    """
    res = eleve(..., ..., ...)
    return res

def charger_data() -> list:
    """
        Ouvre le fichier eleve.csv et créer tous les
        élèves associés à toutes les entrées
    """
    pass
    