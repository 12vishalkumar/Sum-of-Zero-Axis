import numpy as np
N, M = map(int, input().split())
arr = np.array([input().split() for i in range(N)],int)
print(np.prod(np.sum(arr, axis=0),axis = 0))
