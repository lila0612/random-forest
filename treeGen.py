############### Tree generation for random forest ##################

import csv
import math
import random

# Ouverture du fichier csv
def opendata():
    with open("bidon.csv", "r") as data:
        reader = csv.DictReader(data, delimiter=";")
        headers = reader.fieldnames
        # print(headers)
        # for i in reader:
        #     print(i)
        return list(reader)

class RandomTree():

    def __init__(self):
        self._nodesName = list() # Contient le nom des variables sélectionnées à chaque noeud
        self._condition = list() # Contient la condition de chaque noeud
        self._individuals = list() # Contient la liste des individus
        self._variables = list() # Contient la liste des variables


def bootstrap(list, proportion):
    numToTake = int(round(len(list) * proportion, 0))
    result = []
    for i in range(1, numToTake, 1):
        randnum = random.randint(0, len(list)-1)
        result.append(list[randnum])
        list.remove(list[randnum])
    return result



# reader = opendata()
#
# print(len(bootstrap(reader, 0.63)))
