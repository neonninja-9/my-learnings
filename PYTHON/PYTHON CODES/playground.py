import numpy as np
arr = np.array([1, 2, 3]) #1-D Iteration
for x in arr:
    print(x)
arr1 = np.array([[1, 2, 3], [4, 5, 6]]) # 2 -D Iteration
for x in arr1:
    print(x)
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr3:
    print(x)