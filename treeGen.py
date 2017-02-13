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

    def __init__(self, indiv, vars, tar):
        self._nodesNames = list() # Contient le nom des variables sélectionnées à chaque noeud
        self._conditions = list() # Contient la condition de chaque noeud
        self._individuals = indiv # Contient la liste des individus
        self._variables = vars # Contient la liste des variables
        self._target = tar # Pour la construction de l'arbre : détermine la variable cible

    # Getters & setters

    def getNodesNames(self):
        return self._nodesNames

    def getCondition(self):
        return self._conditions

    def getIndividuals(self):
        return self._individuals

    def getVariables(self):
        return self._variables

    # Methods



def bootstrap(list, proportion):
    numToTake = int(round(len(list) * proportion, 0))
    result = []
    for i in range(1, numToTake, 1):
        randnum = random.randint(0, len(list)-1)
        result.append(list[randnum])
        list.remove(list[randnum])
    return result

def columnNames(data):
    names = data[1].keys()
    return list(names)




# Test de la construction d'un arbre.
reader = opendata()

tree = RandomTree(bootstrap(reader, 0.63), columnNames(reader), "sexe")
