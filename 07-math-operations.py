import numpy as np

# >>>>  Mathematical Operations in NumPy

# 1. Element-wise Addition

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = arr1 + arr2
print(result)


# 2. Element-wise Subtraction
result = arr1 - arr2
print(result)

# 3. Element-wise Multiplication
result = arr1 * arr2
print(result)


# 4. Element-wise Division
result = arr1 / arr2
print(result)


# 5. Scalar Operations
arr = np.array([1, 2, 3])

# Scalar operations
print(arr + 2)  # Add 2 to each element
print(arr * 3)  # Multiply each element by 3
print(arr / 2)  # Divide each element by 2
