# Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans
# l’ordre croissant.


for i in range(0, 100):
    for j in range(0, 100):
        if i < j:
            print(i, j, end=", ")
