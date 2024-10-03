import numpy as np

# Existing arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([15, 25, 35, 45, 55])

# Condition array (this could be a condition based on anything, let's say elements greater than 30)
condition = array1 > 30

# Use np.where to select elements from array1 if condition is True, else from array2
result_array = np.where(condition, array1, array2)

print("Array 1:", array1)
print("Array 2:", array2)
print("Condition (array1 > 30):", condition)
print("Resulting array:", result_array)
