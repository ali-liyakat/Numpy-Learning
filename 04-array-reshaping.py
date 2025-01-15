import numpy as np

# >>>>> Reshaping Arrays in NumPy

# syntax
# reshaped_array = array.reshape(new_shape)

# 1. Basic Example

arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape to a 2x3 array
reshaped = arr.reshape(2, 3)
print(reshaped)


# 2. Reshaping to Higher Dimensions
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape to a 3D array (2x1x3)
reshaped = arr.reshape(2, 1, 3)
print(reshaped)


# 3. Automatic Dimension Inference: -1
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape to a 3x2 array (automatically infer)
reshaped = arr.reshape(3, -1)
print(reshaped)


# 4. Flattening with reshape()

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Flatten to 1D
flattened = arr.reshape(-1)
print(flattened)


# 5. Reshaping with Incompatible Shapes
arr = np.array([1, 2, 3, 4])

# Attempt to reshape to 3x2 (incompatible)
try:
    reshaped = arr.reshape(3, 2)
except ValueError as e:
    print(e)



# >>>>> Flattening an Array in NumPy: flatten()

# Syntax
# flattened_array = array.flatten(order='C')

# 1. Basic Example

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Flatten the array
flattened = arr.flatten()
print(flattened)

# 2. Flattening in Column-Major Order (order='F')
# Flatten column by column
flattened = arr.flatten(order='F')
print(flattened)


# 3. Effect of Flattening
flattened[0] = 99
print(flattened)  # Modified flattened array
print(arr)        # Original array remains unchanged


# 4. Comparison with ravel()
flattened = arr.ravel()
flattened[0] = 99

print(flattened)  # Modified flattened array
print(arr)        # Original array is also modified


# 5. Flattening Higher Dimensional Arrays
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Flatten the 3D array
flattened = arr.flatten()
print(flattened)




# >>>>> Flattening an Array in NumPy: ravel()

# Syntax
# flattened_array = array.ravel(order='C')

# 1. Basic Example

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Flatten the array
flattened = arr.ravel()
print(flattened)


# 2. Memory Efficiency: View vs Copy
# Modify the flattened array
flattened[0] = 99
print(flattened)  # Flattened array
print(arr)        # Original array


# 3. Flattening in Column-Major Order
arr = np.array([[1, 2, 3], [4, 5, 6]])

flattened = arr.ravel(order='F')
print(flattened)


# 4. Flattening Higher Dimensional Arrays
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Flatten a 3D array
flattened = arr.ravel()
print(flattened)
