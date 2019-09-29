from numpy import std, cov, mean
from matplotlib import pyplot

age_dataset = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
fat_dataset = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

# z_score
def dataset_std(x):
    return std(x)

def z_score(x):
    return (x - mean(x)) / dataset_std(x)

print(z_score(age_dataset))

# correlation coefficient
def covariance(x, y):
    return cov(x, y)

def pearson(x, y):
    return covariance(x, y) / (dataset_std(x) * dataset_std(y))

print(covariance(age_dataset, fat_dataset))
print(pearson(age_dataset, fat_dataset))

pyplot.scatter(age_dataset, fat_dataset)
pyplot.show()