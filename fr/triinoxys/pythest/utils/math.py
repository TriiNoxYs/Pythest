"""module multipli contenant la fonction table"""

import os

def table(nb=1, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'à max * nb"""
    i = 1
    while i <= max:
        print(i, "*", nb, "=", i * nb)
        i += 1
