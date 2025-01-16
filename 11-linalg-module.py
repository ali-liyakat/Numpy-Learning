import numpy as np

# >>>>>  Linear Algebra Operations with np.linalg

# 1. Determinants: np.linalg.det()


A = np.array([[4, 7], [2, 6]])
det_A = np.linalg.det(A)
print(det_A)  # Output: 10.0

# 2. Eigenvalues and Eigenvectors: np.linalg.eig()

A = np.array([[4, -2], [1, 1]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
# Output: Eigenvalues: [3. 2.]

print("Eigenvectors:")
print(eigenvectors)
# Output:
# [[ 0.89442719  0.70710678]
#  [ 0.4472136  -0.70710678]]


# 3. Inverse of a Matrix: np.linalg.inv()

A = np.array([[1, 2], [3, 4]])
inv_A = np.linalg.inv(A)
print(inv_A)
# Output:
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# 4. Solving Linear Systems: np.linalg.solve()

A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])

x = np.linalg.solve(A, B)
print(x)
# Output: [2. 3.]


# 5. Singular Value Decomposition (SVD): np.linalg.svd()

A = np.array([[1, 2], [3, 4], [5, 6]])
U, S, Vt = np.linalg.svd(A)

print("U:", U)
print("Singular Values:", S)
print("V^T:", Vt)


# 6. Norms of a Matrix: np.linalg.norm()

A = np.array([3, 4])
norm_A = np.linalg.norm(A)
print(norm_A)  # Output: 5.0 (Euclidean norm)


# 7. QR Decomposition: np.linalg.qr()

A = np.array([[1, 2], [3, 4]])
Q, R = np.linalg.qr(A)

print("Q:", Q)
print("R:", R)
