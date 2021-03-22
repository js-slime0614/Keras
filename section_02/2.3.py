import numpy as np

#원소별 연산

def native_relu(x):
    assert len(x.shape) == 2    #x 는 넘파이 배열
    
    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = max(x[i,j], 0)
    return x

def naive_add(x,y):
    assert len(x.shape) == 2 #x와 y는 2D 넘파이 배열입니다.
    assert x.shape == y.shape

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[i, j]
    return x        