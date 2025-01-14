import numpy as np

# >>> Array Creation

# 1: Creating an Array from a List:
arr = np.array([1, 2, 3, 4])
print(arr)


# 2: Creating a 2D array from a list of lists
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)


# 3: Creating an Array from a Tuple
# Creating a 1D array from a tuple
arr_tuple = np.array((10, 20, 30))
print(arr_tuple)


# 4. Specifying the Data Type (dtype):
arr_float = np.array([1, 2, 3], dtype=np.float32)
print(arr_float)
print(arr_float.dtype)  # Output: float32


# 5. Creating a 3D Array:
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d)


# >>> Predefined Array Creation

# 1: np.zeros() - Creating Arrays with Zeros

# Creating a 1D array of zeros with 5 elements
arr_1d = np.zeros(5)   
print(arr_1d)


# Creating a 2D array (3 rows, 4 columns) of zeros
arr_2d = np.zeros((3, 4))
print(arr_2d)


# 2: np.ones() - Creating Arrays with Ones

arr = np.ones(5)   #1-D
print(arr)

arr_2d = np.ones((3, 4))    #2-D
print(arr_2d)


# 3: np.empty() - Creating Uninitialized Arrays
arr = np.empty(5)   # 1-D
print(arr)


arr_2d = np.empty((2, 3))   #2-D
print(arr_2d)


# 3: np.arange() - Creating Arrays with a Range of Values

# Generate an array from 0 to 4
arr = np.arange(5)
print(arr)


# Generate an array from 2 to 8 (excluding 8)
arr = np.arange(2, 8)
print(arr)


# Generate an array from 1 to 10 with a step of 2
arr = np.arange(1, 10, 2)
print(arr)


# Generate an array from 10 to 1 (excluding 1), with a step of -2
arr = np.arange(10, 1, -2)
print(arr)



# 4: np.linspace() - Generating Arrays with Specified Number of Points

# Generate 5 evenly spaced numbers between 0 and 10
arr = np.linspace(0, 10, 5)
print(arr)


# Generate numbers between 0 and 10, excluding 10
arr = np.linspace(0, 10, 5, endpoint=False)
print(arr)


# Generate numbers and get the step size
arr, step = np.linspace(0, 10, 5, retstep=True)
print("Array:", arr)
print("Step size:", step)



# 5: np.eye() - Creating Identity Matrices

# Create a 3x3 identity matrix
arr = np.eye(3)
print(arr)


# Create a 3x4 matrix with ones on the diagonal
arr = np.eye(3, 4)
print(arr)


# Create a matrix with the diagonal above the main
arr = np.eye(3, 3, k=1)
print(arr)


# Create a matrix with the diagonal below the main
arr = np.eye(3, 3, k=-1)
print(arr)
