import numpy as np

# >>>>>  What is Broadcasting?
    # When performing operations, If the arrays have different shapes, NumPy automatically broadcasts the smaller array to match the larger array's shape.

# 1. Adding a Scalar to an Array


arr = np.array([[1, 2, 3], [4, 5, 6]])
result = arr + 10

print(result)


# 2. Broadcasting a 1D Array to a 2D Array

arr1 = np.array([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
arr2 = np.array([10, 20, 30])           # Shape (3,)

result = arr1 + arr2
print(result)


# 3. Broadcasting Arrays of Different Shapes

arr1 = np.array([[1], [2], [3]])  # Shape (3, 1)
arr2 = np.array([10, 20, 30, 40])  # Shape (1, 4)

result = arr1 + arr2
print(result)


# 4. Incompatible Shapes

arr1 = np.array([[1, 2, 3]])  # Shape (1, 3)
arr2 = np.array([[1], [2]])   # Shape (2, 1)

result = arr1 + arr2  # This will work
print(result)
