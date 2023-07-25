# Créez un programme qui affiche la différence minimum absolue entre deux éléments d’un
# tableau constitué uniquement de nombres. Nombres négatifs acceptés.

# Afficher error et quitter le programme en cas de problèmes d’arguments.


# Exemples d’utilisation :
# $> python exo.py 5 1 19 21
# 2
#
#
# $> python exo.py 20 5 1 19 21
# 1
#
# $> python exo.py -8 -6 4
# 2



import sys

# Vérifier si au moins un argument a été passé en ligne de commande
if len(sys.argv) < 2:
    print("Erreur : veuillez spécifier les éléments du tableau.")
    sys.exit(1)

# Récupérer les arguments passés en ligne de commande (à partir du deuxième argument)
arguments = sys.argv[1:]

# Convertir les arguments en une liste de nombres
tableau = []
for argument in arguments:
    try:
        nombre = int(argument)
        tableau.append(nombre)
    except ValueError:
        print("Erreur : les éléments du tableau doivent être des nombres.")
        sys.exit(1)

def difference_minimale_absolue(tableau):
    # Vérifier si le tableau est vide ou ne contient qu'un seul élément
    if len(tableau) < 2:
        print("Erreur : le tableau doit contenir au moins deux éléments.")
        return

    # Initialiser la différence minimale absolue avec la première paire d'éléments
    difference_min = abs(tableau[0] - tableau[1])

    # Parcourir toutes les paires d'éléments du tableau
    for i in range(len(tableau)):
        for j in range(i + 1, len(tableau)):
            # Calculer la différence absolue entre les éléments i et j
            difference = abs(tableau[i] - tableau[j])

            # Mettre à jour la différence minimale absolue si nécessaire
            if difference < difference_min:
                difference_min = difference

    # Afficher la différence minimale absolue
    print("Différence minimale absolue :", difference_min)

# Appeler la fonction difference_minimale_absolue avec le tableau
difference_minimale_absolue(tableau)
