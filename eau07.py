# Créez un programme qui met en majuscule la première lettre de chaque mot d’une chaîne de caractères.
# Les autres lettres devront être en minuscules.
# Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.

# ATTENTION : Afficher error et quitter le programme en cas de problèmes d’arguments.

# Exemples d’utilisation :
# $> python exo.py “bonjour mathilde, comment vas-tu ?!”
# Bonjour Mathilde, Comment Vas-tu ?!
#
#
# $> python exo.py 42
# error


import sys

if len(sys.argv) != 2 or sys.argv[1] == "" or sys.argv[1].isnumeric():
    print("error")
    sys.exit()

text = sys.argv[1]
text = text.split(" ")
for i in range(len(text)):
    text[i] = text[i][0].upper() + text[i][1:]

print(" ".join(text))
