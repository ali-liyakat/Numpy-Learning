import numpy as np

# >>>>>  Linear Algebra: Dot Product in NumPy

# 1. Using np.dot()

# 1D Arrays (Vector Dot Product)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)
print(dot_product)  # Output: 32 (1*4 + 2*5 + 3*6)

# 2D Arrays (Matrix Multiplication)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

matrix_product = np.dot(A, B)
print(matrix_product)
# Output:
# [[19 22]
#  [43 50]]

# 2. Using @ Operator

# For vectors
vector_product = a @ b
print(vector_product)  # Output: 32

# For matrices
matrix_product = A @ B
print(matrix_product)
# Output:
# [[19 22]
#  [43 50]]



# >>>>>  Matrix Multiplication in NumPy: np.matmul()

# 1. Matrix Multiplication (2D Arrays)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = np.matmul(A, B)
print(result)
# Output:
# [[19 22]
#  [43 50]]

# 2. Vector and Matrix Multiplication

vector = np.array([1, 2])
result = np.matmul(A, vector)
print(result)
# Output: [ 5 11 ]


# 3. Broadcasting (3D Arrays)

A = np.random.rand(2, 3, 4)  # 3D array: 2 matrices of size (3x4)
B = np.random.rand(2, 4, 5)  # 3D array: 2 matrices of size (4x5)

result = np.matmul(A, B)
print(result.shape)
# Output: (2, 3, 5)


# 4. Higher Dimensions with Broadcasting

A = np.random.rand(3, 4)     # Single matrix of size (3x4)
B = np.random.rand(2, 4, 5)  # 3D array: 2 matrices of size (4x5)

result = np.matmul(A, B)
print(result.shape)
# Output: (2, 3, 5)
