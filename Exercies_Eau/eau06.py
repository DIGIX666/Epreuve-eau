# Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères.
# Seule les lettres (A-Z, a-z) sont prises en compte.

# ATTENTION : Afficher error et quitter le programme en cas de problèmes d’arguments.


# Exemples d’utilisation :
# $> python exo.py “Hello world !”
# HeLlO wOrLd !
#
#
# $> python exo.py 42
# error



import sys

if len(sys.argv) != 2 or sys.argv[1].isnumeric():
    print("error")
    quit()

for i in range(len(sys.argv[1])):
    if i % 2 == 0:
        print(sys.argv[1][i].upper(), end="")
    else:
        print(sys.argv[1][i], end="")

print()
