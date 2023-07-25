# Créez un programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant.
# Min inclus, max exclus.

# ATTENTION : Afficher error et quitter le programme en cas de problèmes d’arguments.


# Exemples d’utilisation :
# $> python exo.py 20 25
# 20 21 22 23 24
#
#
# $> python exo.py 25 20
# 20 21 22 23 24
#
# $> python exo.py hello
# error


import sys


def main():
    if len(sys.argv) != 3:
        print("Error")
        sys.exit()

    min = int(sys.argv[1])
    max = int(sys.argv[2])


    for i in range(min, max) or range(max, min):
        print(i,  end=" ")

if __name__ == "__main__":
    main()