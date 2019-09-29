from math import *
import numpy as np

x = (1.4, 1.6)
x1 = (1.5, 1.7)
x2 = (2, 1.9)
x3 = (1.6, 1.8)
x4 = (1.2, 1.5)
x5 = (1.5, 1.0)

# Euclidean distance with dataset
def euclidean_distance(x, y):
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))

EuDist = {}
EuDist['x1'] = euclidean_distance(x, x1)
EuDist['x2'] = euclidean_distance(x, x2)
EuDist['x3'] = euclidean_distance(x, x3)
EuDist['x4'] = euclidean_distance(x, x4)
EuDist['x5'] = euclidean_distance(x, x5)
print('Euclidean distance:', sorted(EuDist.items(), key = lambda item: item[1], reverse=True))

# Manhattan distance with dataset
def manhattan_distance(x, y):
     return sum(abs(a - b) for a,b in zip(x, y))

ManDist = {}
ManDist['x1'] = manhattan_distance(x, x1)
ManDist['x2'] = manhattan_distance(x, x2)
ManDist['x3'] = manhattan_distance(x, x3)
ManDist['x4'] = manhattan_distance(x, x4)
ManDist['x5'] = manhattan_distance(x, x5)
print('Manhattan distance:', sorted(ManDist.items(), key = lambda item: item[1], reverse=True))

# Supremum distance with dataset 
def supremum(x, y):
    maximum = 0
    for value in range(0, len(x)):
        test = np.abs(x[value] - y[value])
        if test >= maximum:
            maximum = test
    return maximum

SupDist = {}
SupDist['x1'] = supremum(x, x1)
SupDist['x2'] = supremum(x, x2)
SupDist['x3'] = supremum(x, x3)
SupDist['x4'] = supremum(x, x4)
SupDist['x5'] = supremum(x, x5)
print('Supremum distance:', sorted(SupDist.items(), key = lambda item: item[1], reverse=True))

# Cosine similarity with dataset 
def cosine_similarity(x, y):
    sum = 0
    sumArray1 = 0
    sumArray2 = 0
    for value in range(0, len(x)):
        sum += x[value] * y[value]
    for value in x:
        sumArray1 += np.square(value)
    for value in y:
        sumArray2 += np.square(value)
    array1Bars = np.sqrt(sumArray1)
    array2Bars = np.sqrt(sumArray2)
    return sum / (array1Bars * array2Bars)

CosSimilarity = {}
CosSimilarity['x1'] = cosine_similarity(x, x1)
CosSimilarity['x2'] = cosine_similarity(x, x2)
CosSimilarity['x3'] = cosine_similarity(x, x3)
CosSimilarity['x4'] = cosine_similarity(x, x4)
CosSimilarity['x5'] = cosine_similarity(x, x5)
print('Cosine similarity:', sorted(CosSimilarity.items(), key = lambda item: item[1], reverse=True))
