# Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri à section.
#
# Vous utiliserez une fonction de cette forme (selon votre langage) :
# my_bubble_sort(array) {
# # votre algorithme
# return (new_array)
# }
# ------------------------------------------------------
# Afficher error et quitter le programme en cas de problèmes d’arguments.
# Wikipedia vous présentera une belle description de cet algorithme de tri.


# Exemples d’utilisation :
# $> python exo.py 6 5 4 3 2 1
# 1 2 3 4 5 6
#
#
# $> python exo.py test test test
# error


import sys

def my_bubble_sort(array):
    # Vérifier si le tableau est vide ou ne contient qu'un seul élément
    if len(array) < 2:
        print("Erreur : le tableau doit contenir au moins deux éléments.")
        sys.exit(1)

    # Effectuer le tri par sélection
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        # Échanger les éléments
        array[i], array[min_index] = array[min_index], array[i]

    # Retourner le tableau trié
    return array


# Vérifier si au moins un argument a été passé en ligne de commande
if len(sys.argv) < 2:
    print("Erreur : veuillez spécifier les éléments du tableau.")
    sys.exit(1)

# Récupérer les arguments passés en ligne de commande (à partir du deuxième argument)
arguments = sys.argv[1:]


# Convertir les arguments en une liste de nombres
try:
    tableau = [str(argument) for argument in arguments]

except ValueError:
    print("Erreur : les éléments du tableau doivent être des nombres.")
    sys.exit(1)

# Appeler la fonction my_bubble_sort avec la string comme argument
sorted_array = my_bubble_sort(tableau)
sorted_string = ' '.join(sorted_array)

print("Tableau trié :", sorted_string)
