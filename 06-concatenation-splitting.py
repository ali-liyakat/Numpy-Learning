import numpy as np

# Concatenating Arrays in NumPy:

# >>>> 1: np.concatenate()

# 1. Concatenating 1D Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.concatenate((arr1, arr2))
print(result)

# 2. Concatenating 2D Arrays
# (Vertical Concatenation, axis=0):

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

result = np.concatenate((arr1, arr2), axis=0)
print(result)

#  (Horizontal Concatenation, axis=1):
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5], [6]])

result = np.concatenate((arr1, arr2), axis=1)
print(result)

# 3. Concatenating Higher-Dimensional Arrays
arr1 = np.array([[[1, 2]], [[3, 4]]])
arr2 = np.array([[[5, 6]], [[7, 8]]])

result = np.concatenate((arr1, arr2), axis=0)
print(result)


'''4. Important Notes
Array Shapes Must Match:
For concatenation along a particular axis, the dimensions of the other axes must match.
Example:
axis=0: All arrays must have the same number of columns.
axis=1: All arrays must have the same number of rows.

Concatenation on Different Axes:

For 1D arrays → Default axis=0 (flat concatenation).
For 2D arrays → axis=0 (rows), axis=1 (columns).'''



# >>>>> 2: np.stack()

# 1. Stacking 1D Arrays

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.stack((arr1, arr2), axis=0)  # Default axis=0
print(result)

# 2. Changing the Axis
result = np.stack((arr1, arr2), axis=1)
print(result)


# 3. Stacking 2D Arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

result = np.stack((arr1, arr2), axis=0)
print(result)


# 4. Higher-Dimensional Stacking
arr1 = np.ones((2, 2, 2))
arr2 = np.zeros((2, 2, 2))

result = np.stack((arr1, arr2), axis=3)
print(result)
print(result.shape)


# >>> 1. np.hstack() (Horizontal Stack)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

result = np.hstack((arr1, arr2))
print(result)


# >>> 2. np.vstack() (Vertical Stack)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

result = np.vstack((arr1, arr2))
print(result)


# 3. Stacking 1D Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

h_result = np.hstack((arr1, arr2))
v_result = np.vstack((arr1, arr2))

print("Horizontal Stack:\n", h_result)
print("Vertical Stack:\n", v_result)




# >>>>>   Splitting Arrays in NumPy

# 1. np.split()

#  1: Splitting 1D Arrays

arr = np.array([1, 2, 3, 4, 5, 6])

# Split into 3 equal parts
result = np.split(arr, 3)
print(result)


# 2: Splitting 2D Arrays

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Split into 3 equal parts along axis=1 (columns)
result = np.split(arr, 3, axis=1)
print(result)



# 2. np.array_split()

# 1: Splitting 1D Arrays Unequally

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Split into 3 parts
result = np.array_split(arr, 3)
print(result)

# 2: Splitting 2D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Split into 4 parts along axis=1 (columns)
result = np.array_split(arr, 4, axis=1)
print(result)
