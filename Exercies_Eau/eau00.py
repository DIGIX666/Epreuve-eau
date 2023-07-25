# Créez un programme qui affiche toutes les différentes combinaisons possibles de trois chiffres
# dans l’ordre croissant, dans l’ordre croissant. La répétition est volontaire.

# ATTENTION :
# 987 n’est pas là parce que 789 est présent.
# 020 n’est pas là parce que 0 apparaît deux fois.
# 021 n’est pas là parce que 012 est présent.
# 000 n’est pas là parce que cette combinaison ne comporte pas exclusivement des chiffres différents les uns des autres.


for i in range(10):
    for j in range(i, 10):
        for k in range(j, 10):
            if i != j and i != k and j != k:
                print(f"{i}{j}{k}", end = ", ")
print()
