from numpy import std, cov, mean
from scipy import stats

age_dataset = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
fat_dataset = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

# z_score
def dataset_std(x):
    return std(x)

def z_score(x):
    return (x - mean(x)) / dataset_std(x)

# correlation coefficient
def covariance(x, y):
    return cov(x, y)

def pearson(x, y):
    return covariance(x, y) / (dataset_std(x) * dataset_std(y))

if __name__ == "__main__":
    print(z_score(age_dataset))
    print(covariance(age_dataset, fat_dataset))
    print(pearson(age_dataset, fat_dataset))
    print(stats.pearsonr(age_dataset, fat_dataset))