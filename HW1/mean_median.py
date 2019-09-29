from numpy import mean, median

age_dataset = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
fat_dataset = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

def dataset_mean(x):
    return (sum(x)) / max(len(x), 1)

def dataset_median(x):
    array = sorted(x)
    half, odd = divmod(len(array), 2)
    if odd:
        return array[half]
    return (array[half - 1] + array[half]) / 2.0

if __name__ == "__main__":
    print('age mean:', dataset_mean(age_dataset))
    print('age median:', dataset_median(age_dataset))
    print('fat mean:', dataset_mean(fat_dataset))
    print('fat median:', dataset_median(fat_dataset))