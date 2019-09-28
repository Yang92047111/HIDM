from scipy.spatial import distance
import pandas as pd
from math import *

x = (1.4, 1.6)
x1 = (1.5, 1.7)
x2 = (2, 1.9)
x3 = (1.6, 1.8)
x4 = (1.2, 1.5)
x5 = (1.5, 1.0)

# Euclidean distance with dataset
def euclidean_distance(x, y):
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))

x1_EuDist = distance.euclidean(x, x1)
x2_EuDist = distance.euclidean(x, x2)
x3_EuDist = distance.euclidean(x, x3)
x4_EuDist = distance.euclidean(x, x4)
x5_EuDist = distance.euclidean(x, x5)

# Manhattan distance with dataset
def manhattan_distance(x, y):
     return sum(abs(a - b) for a,b in zip(x, y))

x1_ManDist = manhattan_distance(x, x1)
x2_ManDist = manhattan_distance(x, x2)
x3_ManDist = manhattan_distance(x, x3)
x4_ManDist = manhattan_distance(x, x4)
x5_ManDist = manhattan_distance(x, x5)

# Supremum distance with dataset 
def nth_root(value, n_root):
    root_value = 1 / float(n_root)
    return round (value ** root_value, 3)
 
def minkowski_distance(x, y, p_value):
    return nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)

x1_SupDist = minkowski_distance(x, x1, inf)
x2_SupDist = minkowski_distance(x, x2, inf)
x3_SupDist = minkowski_distance(x, x3, inf)
x4_SupDist = minkowski_distance(x, x4, inf)
x5_SupDist = minkowski_distance(x, x5, inf)

# Cosine similarity with dataset 
def square_rooted(x):
     
    return round(sqrt(sum([a * a for a in x])), 3)
 
def cosine_similarity(x, y):
    numerator = sum(a * b for a, b in zip(x, y))
    denominator = square_rooted(x) * square_rooted(y)
    return round(numerator / float(denominator), 3)

x1_CosSimilarity = cosine_similarity(x, x1)
x2_CosSimilarity = cosine_similarity(x, x2)
x3_CosSimilarity = cosine_similarity(x, x3)
x4_CosSimilarity = cosine_similarity(x, x4)
x5_CosSimilarity = cosine_similarity(x, x5)



 
