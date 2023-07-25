# Créez un programme qui affiche le N-ème élément de la célèbre
# suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0.

# Afficher -1 si le paramètre est négatif ou mauvais.


# Exemples d’utilisation :
# $> python exo.py 3
# 2
# $>


import sys


def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))