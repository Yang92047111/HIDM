import sys
from math import asin, atan2, cos, exp, floor, isnan, log, pi

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.pyplot import subplots, tight_layout
from mpl_toolkits.mplot3d import Axes3D
from tqdm import trange

Horizontal_Resolution = 0.1

Vertical_Resolution = 2
Vertical_FoV = 30

Channel = 32

Distance_Resolution = 0.03
Distance_FoV = 100

def coordinate_system_transform(data):
    out = []
    for i in data:
        x = i[0]
        y = i[1]
        z = i[2]
        r = pow((i*i).sum(),0.5)
        v = asin(z/r)*180/pi
        h = atan2(y, x)*180/pi
        out.append([h,r,v])
    return np.array(out)
def read_csv(file_name):
    df = pd.read_csv(file_name)
    np_out = df.values
    np_out = np.array(np_out)
    return np_out
def choice_data(data,index_list):
    data = [iteration[index_list] for iteration in data]
    return np.array(data)
def threeD2twoD(data):
    '''
    data: shape(n,3)
    Return: 2-D matrix
    '''
    v = np.array([i[2] for i in data])

    # for i in data:
    #     print(i[0])

    # print(v.min())
    data = np.array([[floor((iteration[2]-v.min())/Vertical_FoV*Channel-1), floor(iteration[0]/Horizontal_Resolution-1), Distance_FoV-iteration[1]] for iteration in data])#[pitch, yaw, distance]->[row,col,color]

    # for i in data:
    #     print(i[0])

    two_D_plane = np.zeros([Channel, int(360/Horizontal_Resolution)])
    for iteration in data:
        two_D_plane[int(iteration[0]), int(iteration[1])] = iteration[2]
    return two_D_plane
def local_variance(data, r):
    '''
    data: 2-D raw plane\n
    r: a number > 0 ,referance distance\n
    
    Return: a local variance plane
    '''
    np_out = np.array(data)

    window_size_h = 1/(r*r*3.14*Vertical_FoV/360*1/Channel)#50cm
    window_size_h = int(window_size_h+(1-window_size_h%2))
    window_size_w = 1/(r*r*3.14*Horizontal_Resolution/360)#50cm
    window_size_w = int(window_size_w+(1-window_size_w%2))

    pad_size_h = int(window_size_h/2)
    pad_size_w = int(window_size_w/2)
    
    variance_plane = np.pad(data, ((pad_size_h, pad_size_h), (pad_size_w, pad_size_w)), 'reflect')
    temp = np.array(variance_plane)
    # sys.exit()
    maxV = 0
    minV = Distance_FoV
    coco = []
    
    print('window size = ',[window_size_h,window_size_w],'\npadding size = ',[pad_size_h,pad_size_w])

    for row in range(pad_size_h, variance_plane.shape[0]-pad_size_h):
        for col in range(pad_size_w, variance_plane.shape[1]-pad_size_w):
            if(variance_plane[row, col] != 0):
                xi = []
                mean = 0
                variance = 0
                for i in range(0 - pad_size_h, window_size_h - pad_size_h):
                    for j in range(0 - pad_size_w, window_size_w - pad_size_w):
                        if(variance_plane[row+i, col+j] != 0):
                            xi.append(variance_plane[row+i, col+j])
                xi  = np.array(xi)
                if(len(xi) != 0):
                    mean = xi.sum() / len(xi)
                    variance = ((xi-mean)*(xi-mean)).sum()/len(xi)
                    # variance = (abs(xi-mean)).sum()/len(xi)
                    if(isnan(variance)):
                        coco.append([row,col])
                        print(xi)
                    if(variance<minV):
                        minV = variance
                    if(variance>maxV):
                        maxV = variance
                    temp[row, col] = (variance-minV)/(maxV-minV)

    for row in range(0, data.shape[0]):
        for col in range(0, data.shape[1]):
            np_out[row, col] = temp[row+pad_size_h, col+pad_size_w]
    return np_out
def gamma_transform(data, gamma):
    np_out = np.array(data)
    for i in range(len(data)):
        np_out[i] = pow(data[i], gamma)
    return np_out
def normalize(data):
    np_out = np.array(data)
    M = 0
    m = Distance_FoV
    for i in range(len(data)):
        if(max(data[i])>M):
            M = max(data[i])
        if(min(data[i])<m):
            m = min(data[i])
    for i in range(len(np_out)):
        np_out[i] = (np_out[i]-m)/(M-m)
    return np_out

if __name__ == "__main__":
    # filename = 'points_output(frame01_frame02)'
    # filename = 'points_output(frame02_frame03)'
    # filename = 'points_output(frame03_frame04)'
    filename = 'points_output(frame04_frame05)'
    # filename = 'output'
    data = read_csv('PointData/'+filename+'.csv')
    # print(data)
    data = choice_data(data, [8,9,12])# [yaw*100(resolution 0.1), distance(m)(0~120m), pitch(degree)(resolution 0.33)]
    
    data = coordinate_system_transform(data)

    # sys.exit()

    two_D_plane = threeD2twoD(data)
    aspect=20
    plt.grid(True)
    plt.imshow(gamma_transform(normalize(two_D_plane), 1), aspect=aspect)
    plt.colorbar(cax=None,ax=None,shrink=0.5)
    plt.ylim(0, Channel-1)
    '''
    local_variance_plane = local_variance(two_D_plane, 5)
    
    plt.subplot(312)
    plt.grid(True)
    plt.imshow(gamma_transform(local_variance_plane, 0.5), aspect=aspect)
    plt.colorbar(cax=None,ax=None,shrink=0.5)
    plt.ylim(0, Channel)
    '''
    plt.show()
