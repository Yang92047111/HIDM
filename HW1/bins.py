#equal frequency 
def equifreq(data, m): 
      
    a = len(data) 
    n = int(a / m) 
    for i in range(0, m): 
        arr = [] 
        for j in range(i * n, (i + 1) * n): 
            if j >= a: 
                break
            arr = arr + [data[j]] 
        print(arr) 
  
#equal width 
def equiwidth(data, m): 
    a = len(data) 
    w = int((max(data) - min(data)) / m) 
    min1 = min(data) 
    arr = [] 
    for i in range(0, m + 1): 
        arr = arr + [min1 + w * i] 
    arri=[] 
      
    for i in range(0, m): 
        temp = [] 
        for j in data: 
            if j > arr[i] and j < arr[i+1]: 
                temp += [j] 
        arri += [temp] 
    print(arri)  
  
#data to be binned 
dataset = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215] 
#no of bins 
m = 3 
  
print("equal frequency binning") 
equifreq(dataset, m) 
  
print("\nequal width binning") 
equiwidth(dataset, m) 