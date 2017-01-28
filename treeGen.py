############### Tree generation for random forest ##################

import csv
import math
import random

# Ouverture du fichier csv
with open("iris.csv", "r") as data:
    reader = csv.DictReader(data, delimiter = ',')
    headers = reader.fieldnames
    varNum = len(headers)
    print(headers)
    # for i in reader :
    #     print(i)

# data doit contenir les donnees a entrer.
# varNum est le nombre de variables du fichier.
# opCol est la colonne contenant la réponse pour l'entrainement.
# def create_tree(data, varNum, opCol):
#     varNum = math.sqrt(varNum) # Par défaut, l'arbre prend en compte la racine carree du nombre total de variables
#
#     boostrap = random.randint(1, len(reader))
#     n = 0
#     for var in reader.fieldnames:
#         if n < varNum:
