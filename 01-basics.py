import numpy as np

# numpy.ndarray is core datastructure of Numpy.

# >> Array Creation

# Creating an ndarray from a list
arr = np.array([1, 2, 3, 4])
print(arr)
# Output: [1 2 3 4]

# Creating a 2D ndarray from a list of lists (matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
# Output:
# [[1 2 3]
#  [4 5 6]]


# >>: Key Attributes

# 1: ndarray.shape
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)    # Output: (2, 3)


# 2 : ndarray.ndim
arr = np.array([1, 2, 3, 4])
print(arr.ndim)  # Output: 1 (1-dimensional array)

# 3: ndarray.size
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.size)  # Output: 6 (2x3 matrix has 6 elements)


# 4 : ndarray.dtype
arr = np.array([1.5, 2.5, 3.5])
print(arr.dtype)  # Output: float64 (by default, NumPy stores numbers as 64-bit floats)


# 5 : ndarray.itemsize
arr = np.array([1, 2, 3])
print(arr.itemsize)  # Output: 4 (for 32-bit integer)


# 6: ndarray.T (Transpose)
arr = np.array([[1, 2], [3, 4]])
print(arr.T)
# Output:
# [[1 3]
#  [2 4]]



# >>> Common Operations on ndarray:

# 1: Element-wise operations:
arr = np.array([1, 2, 3])
print(arr + 2)  # Output: [3 4 5] (adds 2 to each element)
print(arr * 3)  # Output: [3 6 9] (multiplies each element by 3)


# 2: Broadcasting:
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])
print(arr1 + arr2)  # Output: [11 22 33]


# 3: Reshaping arrays:
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)  # Reshape to a 2x3 matrix
print(reshaped_arr)
# Output:
# [[1 2 3]
#  [4 5 6]]
