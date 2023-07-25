# Créez un programme qui affiche le premier index d’un élément recherché dans un tableau.
# Le tableau est constitué de tous les arguments sauf le dernier.
# L’élément recherché est le dernier argument. Afficher -1 si l’élément n’est pas trouvé.

# ATTENTION : Afficher error et quitter le programme en cas de problèmes d’arguments.

# Exemples d’utilisation :
# $> python exo.py Ceci est le monde qui contient Charlie un homme sympa Charlie
# 6

# $> python exo.py test test test
# 0

# $> python exo.py test boom
# -1



import sys

# Vérifier le nombre d'arguments
if len(sys.argv) < 3:
    print("Erreur : Le programme nécessite au moins deux arguments.")
    sys.exit(1)

# Récupérer les arguments
tableau = sys.argv[1:-1]
element_recherche = sys.argv[-1]

# Vérifier si l'élément recherché est présent dans le tableau
if element_recherche in tableau:
    index = tableau.index(element_recherche)
    print("Le premier index de l'élément recherché est :", index)
else:
    print("L'élément recherché n'est pas présent dans le tableau.")
    print("Premier index : -1")
