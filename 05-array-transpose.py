import numpy as np

# >>>>>  Transposing an Array in NumPy: transpose() and .T

# 1. Using .T

arr = np.array([[1, 2], [3, 4], [5, 6]])

# Transpose using .T
transposed = arr.T
print(transposed)


# 2. Using transpose()
transposed = arr.transpose()
print(transposed)


# Example (Higher-Dimensional Array):
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Transpose specific axes
transposed = arr_3d.transpose(1, 0, 2)
print(transposed)


# 4. Transposing 1D Arrays
arr_1d = np.array([1, 2, 3])

# Transposing a 1D array
print(arr_1d.T)
print(arr_1d.transpose())
