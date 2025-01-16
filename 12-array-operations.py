import numpy as np

# >>>>>  Advanced Array Operations:

# >>>>>   Sorting

# 1. np.sort()

# Sorting a 1D Array:

arr = np.array([3, 1, 4, 1, 5, 9])
sorted_arr = np.sort(arr)
print("Original:", arr)        # Output: [3 1 4 1 5 9]
print("Sorted:", sorted_arr)   # Output: [1 1 3 4 5 9]

# Sorting Along an Axis:

arr_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
sorted_rows = np.sort(arr_2d, axis=1)  # Sort each row
sorted_cols = np.sort(arr_2d, axis=0)  # Sort each column

print("Row-wise Sort:\n", sorted_rows)
# Output:
# [[1 3 4]
#  [1 5 9]
#  [2 5 6]]

print("Column-wise Sort:\n", sorted_cols)
# Output:
# [[1 1 4]
#  [2 5 5]
#  [3 6 9]]

# Flattening and Sorting:

sorted_flat = np.sort(arr_2d, axis=None)  # Flattens and sorts
print("Flattened and Sorted:", sorted_flat)
# Output: [1 1 2 3 4 5 5 6 9]



# 2. np.argsort()

# Sorting Indices for a 1D Array:

arr = np.array([3, 1, 4, 1, 5, 9])
sorted_indices = np.argsort(arr)
print("Sorted Indices:", sorted_indices)  # Output: [1 3 0 2 4 5]

# Reordering the original array using the indices
sorted_arr = arr[sorted_indices]
print("Sorted Array:", sorted_arr)        # Output: [1 1 3 4 5 9]


# Using argsort() with Multi-Dimensional Arrays:

arr_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
sorted_row_indices = np.argsort(arr_2d, axis=1)

print("Row-wise Sorted Indices:\n", sorted_row_indices)
# Output:
# [[1 0 2]
#  [0 1 2]
#  [0 2 1]]



# >>>>>   Unique Elements: np.unique()

# 1. Basic Usage: Finding Unique Elements


arr = np.array([3, 1, 2, 3, 4, 2, 1, 5])
unique_elements = np.unique(arr)
print("Unique Elements:", unique_elements)
# Output: [1 2 3 4 5]

# 2. Returning Indices

arr = np.array([3, 1, 2, 3, 4, 2, 1, 5])
unique_elements, indices = np.unique(arr, return_index=True)
print("Unique Elements:", unique_elements)   # Output: [1 2 3 4 5]
print("Indices:", indices)                   # Output: [1 2 0 4 7]

# 3. Reconstructing the Original Array

arr = np.array([3, 1, 2, 3, 4, 2, 1, 5])
unique_elements, inverse_indices = np.unique(arr, return_inverse=True)
print("Unique Elements:", unique_elements)    # Output: [1 2 3 4 5]
print("Inverse Indices:", inverse_indices)    # Output: [2 0 1 2 3 1 0 4]

# Reconstruct the original array:
reconstructed = unique_elements[inverse_indices]
print("Reconstructed Array:", reconstructed)  # Output: [3 1 2 3 4 2 1 5]


# 4. Counting Occurrences

arr = np.array([3, 1, 2, 3, 4, 2, 1, 5])
unique_elements, counts = np.unique(arr, return_counts=True)
print("Unique Elements:", unique_elements)  # Output: [1 2 3 4 5]
print("Counts:", counts)                    # Output: [2 2 2 1 1]


# 5. Using axis for Multi-Dimensional Arrays

arr_2d = np.array([[1, 2, 3], [1, 2, 3], [4, 5, 6]])
unique_rows = np.unique(arr_2d, axis=0)
print("Unique Rows:\n", unique_rows)
# Output:
# [[1 2 3]
#  [4 5 6]]



# >>>>>>   Searching in Arrays:

# 1. np.where()

# Finding Indices Where a Condition is Met:


arr = np.array([10, 15, 20, 25, 30])
indices = np.where(arr > 20)
print("Indices where arr > 20:", indices)
# Output: (array([3, 4]),)

# Using the Indices to Access Values:

values = arr[indices]
print("Values where arr > 20:", values)
# Output: [25 30]


# Conditional Value Assignment:

arr = np.array([10, 15, 20, 25, 30])
result = np.where(arr > 20, "Above 20", "20 or Below")
print("Result:", result)
# Output: ['20 or Below' '20 or Below' '20 or Below' 'Above 20' 'Above 20']


# Multi-Dimensional Arrays:

arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
indices = np.where(arr_2d > 3)
print("Indices where arr_2d > 3:", indices)
# Output: (array([1, 2, 2]), array([1, 0, 1]))

values = arr_2d[indices]
print("Values where arr_2d > 3:", values)
# Output: [4 5 6]



# 2. np.nonzero()

# Finding Indices of Non-Zero Elements:

arr = np.array([0, 2, 0, 3, 4])
indices = np.nonzero(arr)
print("Indices of non-zero elements:", indices)
# Output: (array([1, 3, 4]),)


# Using Indices to Access Non-Zero Elements:

values = arr[indices]
print("Non-zero elements:", values)
# Output: [2 3 4]

# Multi-Dimensional Arrays:

arr_2d = np.array([[0, 1, 0], [2, 0, 3]])
indices = np.nonzero(arr_2d)
print("Indices of non-zero elements:", indices)
# Output: (array([0, 1, 1]), array([1, 0, 2]))

values = arr_2d[indices]
print("Non-zero elements:", values)
# Output: [1 2 3]




# >>>>>>>  Conditions in NumPy

# 1. np.all()

# Basic Usage:


arr = np.array([True, True, True])
print(np.all(arr))  # Output: True

arr = np.array([True, False, True])
print(np.all(arr))  # Output: False

# Using Conditions:

arr = np.array([1, 2, 3, 4, 5])
print(np.all(arr > 0))  # Output: True (All elements are greater than 0)
print(np.all(arr > 3))  # Output: False (Not all elements are greater than 3)

# Multi-Dimensional Arrays:

arr_2d = np.array([[1, 2], [3, 4]])
print(np.all(arr_2d > 0, axis=0))  # Output: [True True] (Column-wise)
print(np.all(arr_2d > 0, axis=1))  # Output: [True True] (Row-wise)



# 2. np.any()

# Basic Usage:

arr = np.array([False, False, True])
print(np.any(arr))  # Output: True

arr = np.array([False, False, False])
print(np.any(arr))  # Output: False

# Using Conditions:

arr = np.array([1, 2, 3, 4, 5])
print(np.any(arr > 3))  # Output: True (At least one element is greater than 3)
print(np.any(arr < 0))  # Output: False (No elements are less than 0)

# Multi-Dimensional Arrays:

arr_2d = np.array([[1, 2], [0, 4]])
print(np.any(arr_2d == 0, axis=0))  # Output: [True False] (Column-wise)
print(np.any(arr_2d == 0, axis=1))  # Output: [False True] (Row-wise)
