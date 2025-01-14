import numpy as np

# >>>> Indexing and Slicing in NumPy Arrays
# Basic Indexing: Accessing Elements Using Indices


# 1. 1D Arrays

arr = np.array([10, 20, 30, 40, 50])
print(arr[0])  # First element
print(arr[2])  # Third element
print(arr[-1]) # Last element (negative indexing)

# 2. 2D Arrays

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0, 0])  # Element at row 0, column 0
print(arr[1, 2])  # Element at row 1, column 2
print(arr[-1, -1]) # Last element in the last row


# 3. 3D Arrays

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr[0, 0, 1])  # Element at depth 0, row 0, column 1
print(arr[1, 1, 0])  # Element at depth 1, row 1, column 0


# >>> Out-of-Bounds Index:

arr = np.array([1, 2, 3])
# print(arr[3])  # IndexError



# >>>>> Slicing in NumPy Arrays

# Syntax
#      array[start:stop:step]


# 1. Slicing in 1D Arrays
arr = np.array([10, 20, 30, 40, 50])

# Slicing examples
print(arr[1:4])    # Elements from index 1 to 3
print(arr[:3])     # Elements from start to index 2
print(arr[2:])     # Elements from index 2 to the end
print(arr[::2])    # Every second element
print(arr[::-1])   # Reverse the array


# 2. Slicing in 2D Arrays

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Slicing rows and columns
print(arr[1:, :2])  # Rows from index 1 onward, first 2 columns
print(arr[:2, 1:])  # First 2 rows, columns from index 1 onward
print(arr[:, ::2])  # All rows, every second column


# 3. Slicing in 3D Arrays
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# Slicing examples
print(arr[:, 0, :])  # All depths, first row, all columns
print(arr[1, :, 1])  # Depth 1, all rows, second column




# >>>>> Fancy Indexing in NumPy: Accessing Elements Using Arrays of Indices

# 1. Fancy Indexing in 1D Arrays

arr = np.array([10, 20, 30, 40, 50])

# Access elements at indices 0, 2, and 4
result = arr[[0, 2, 4]]
print(result)

# 2. Fancy Indexing in 2D Arrays
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Access rows at indices 0 and 2
result = arr[[0, 2]]
print(result)

# Access Specific Elements (Row-Column Pair):
# Access elements at (0,1), (1,2), and (2,0)
result = arr[[0, 1, 2], [1, 2, 0]]
print(result)


# 3. Fancy Indexing with Boolean Arrays
arr = np.array([10, 15, 20, 25, 30])

# Create a Boolean mask for elements greater than 20
mask = arr > 20

# Use the mask for indexing
result = arr[mask]
print(result)


# 4. Combining Fancy Indexing with Slicing
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Access the first two rows and columns 0 and 2
result = arr[:2, [0, 2]]
print(result)



# >>>>> Boolean Masking in NumPy: Filtering Elements Based on Conditions

# 1. Basic Boolean Masking

arr = np.array([10, 20, 30, 40, 50])

# Create a mask for elements greater than 25
mask = arr > 25
print(mask)  # Boolean mask
result = arr[mask]
print(result)  # Filtered elements


# 2. Applying Complex Conditions (& (and),| (or),~ (not))

# Elements greater than 15 and less than 45
result = arr[(arr > 15) & (arr < 45)]
print(result)

# Elements not greater than 25
result = arr[~(arr > 25)]
print(result)


# 3. Boolean Masking in 2D Arrays

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Mask for elements greater than 5
mask = arr > 5
print(mask)

result = arr[mask]
print(result)


# 4. Modifying Arrays Using Masks

# Replace elements greater than 25 with -1
arr = np.array([10, 20, 30, 40, 50])
arr[arr > 25] = -1
print(arr)

# 5. Combining Boolean Masking with np.where
arr = np.array([10, 20, 30, 40, 50])
result = np.where(arr > 25, arr, -1)
print(result)


