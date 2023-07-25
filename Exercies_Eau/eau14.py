# Créez un programme qui trie les éléments donnés en argument par ordre ASCII.

# ATTENTION : Afficher error et quitter le programme en cas de problèmes d’arguments.


# Exemples d’utilisation :
# $> python exo.py Alfred Momo Gilbert
# Alfred Gilbert Momo
#
#
# $> python exo.py A Z E R T Y
# A E R T Y Z


import sys

# Vérifier si au moins un argument a été passé en ligne de commande
if len(sys.argv) < 2:
    print("Erreur : veuillez spécifier les éléments à trier.")
    sys.exit(1)

# Récupérer les arguments passés en ligne de commande (à partir du deuxième argument)
arguments = sys.argv[1:]

# Trier les arguments par ordre ASCII
sorted_arguments = sorted(arguments)

# Convertir la liste triée en une chaîne de caractères
sorted_string = ' '.join(sorted_arguments)

# Afficher la chaîne de caractères triée
print(sorted_string)


