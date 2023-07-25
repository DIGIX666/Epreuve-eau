# Créez un programme qui détermine si une chaîne de caractères ne contient que des chiffres.

# ATTENTION : Afficher error et quitter le programme en cas de problèmes d’arguments.

# Exemples d’utilisation :
# $> python exo.py “4445353”
# true
#
#
# $> python exo.py 42
# true
#
# $> python exo.py “Bonjour 36”
# false


import sys

if len(sys.argv) != 2:
    print("error")
    sys.exit()

for i in sys.argv[1]:
    if not i.isdigit():
        print("false")
        sys.exit()

print("true")
