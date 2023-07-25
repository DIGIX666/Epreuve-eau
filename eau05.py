# Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre.
# Afficher error et quitter le programme en cas de problèmes d’arguments.


# Exemples d’utilisation :
# $> python exo.py bonjour jour
# true
#
#
# $> python exo.py bonjour joure
# false
#
#
# $> python exo.py 42
# error



import sys

if len(sys.argv) != 3:
    print("error")
    exit()

if sys.argv[1] in sys.argv[2] or sys.argv[2] in sys.argv[1] :
    print("true")

else:
    print("false")

