# Créez un programme qui affiche ses arguments reçus à l’envers.
# Afficher error et quitter le programme en cas de problèmes d’arguments.


# Exemples d’utilisation :
# $> python exo.py “Suis” “Je” “Drôle”
# Drôle
# Je
# Suis
#
#
# $> python exo.py ha ho
# ho
# ha
#
# $> python exo.py “Bonjour 36”
# Bonjour 36

import sys

def main():
    if len(sys.argv) > 1:
        for i in range(len(sys.argv) - 1, 0, -1):
            print(sys.argv[i])
    else:
        print("error")
        exit()

if __name__ == "__main__":
    main()




