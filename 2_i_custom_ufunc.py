import numpy as np
from scipy import stats

# Part 1: Custom ufunc that adds 10
def add_10(x):
    return x + 10

add_10_ufunc = np.frompyfunc(add_10, 1, 1)

array = np.array([1, 2, 3, 4])
result = add_10_ufunc(array)
print("Result after adding 10:", result)
