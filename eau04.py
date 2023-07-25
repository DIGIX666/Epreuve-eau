# Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.

# Afficher -1 si le paramètre est négatif ou mauvais.

# Exemples d’utilisation :
# $> python exo.py 14
# 17
# $>


import sys


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def next_prime(number):
    if number < 0:
        return -1
    while True:
        if is_prime(number):
            return number
        number += 1


if __name__ == "__main__":
    print(next_prime(int(sys.argv[1])))