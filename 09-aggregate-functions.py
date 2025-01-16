import numpy as np

# >>>>>   Aggregate Functions in NumPy

# 1: np.sum()

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(np.sum(arr))  # Sum of all elements: 21
print(np.sum(arr, axis=0))  # Column-wise sum: [5 7 9]
print(np.sum(arr, axis=1))  # Row-wise sum: [6 15]

# 2: np.mean()

print(np.mean(arr))  # Overall mean: 3.5
print(np.mean(arr, axis=0))  # Column-wise mean: [2.5 3.5 4.5]
print(np.mean(arr, axis=1))  # Row-wise mean: [2. 5.]

# 3: np.std()

print(np.std(arr))  # Overall standard deviation: 1.7078
print(np.std(arr, axis=0))  # Column-wise standard deviation: [1.5 1.5 1.5]
print(np.std(arr, axis=1))  # Row-wise standard deviation: [0.8165 0.8165]

# 4: np.min() and np.max()

print(np.min(arr))  # Overall minimum: 1
print(np.max(arr))  # Overall maximum: 6
print(np.min(arr, axis=0))  # Column-wise minimum: [1 2 3]
print(np.max(arr, axis=1))  # Row-wise maximum: [3 6]

# 5: np.prod()

print(np.prod(arr))  # Product of all elements: 720
print(np.prod(arr, axis=0))  # Column-wise product: [4 10 18]

# 6: np.var()

print(np.var(arr))  # Overall variance: 2.9167
print(np.var(arr, axis=0))  # Column-wise variance: [2.25 2.25 2.25]

# 7: np.cumsum()

print(np.cumsum(arr))  # Cumulative sum of all elements: [1 3 6 10 15 21]
print(np.cumsum(arr, axis=0))  # Column-wise cumulative sum:
# [[1 2 3]
#  [5 7 9]]

# 8: np.cumprod()

print(np.cumprod(arr))  # Cumulative product: [1 2 6 24 120 720]


# 9: np.median()

print(np.median(arr))  # Median of all elements: 3.5


# 10: np.argmax() and np.argmin()

print(np.argmax(arr))  # Index of the maximum value (flattened): 5
print(np.argmin(arr))  # Index of the minimum value (flattened): 0
print(np.argmax(arr, axis=0))  # Column-wise indices of max: [1 1 1]
