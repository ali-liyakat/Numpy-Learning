import numpy as np

# >>>>>>> Working with Random Numbers in NumPy

# 1. np.random.rand()

# Single Random Number:

random_number = np.random.rand()
print(random_number)
# Output: A random number, e.g., 0.5488135039273248

# Random Array with Given Shape:

random_array = np.random.rand(3, 2)
print(random_array)
# Output: A 3x2 array of random numbers between 0 and 1


# 2. np.random.randn()

# Single Random Number:

random_number = np.random.randn()
print(random_number)
# Output: A random number, e.g., -0.9787379841057392

# Random Array with Given Shape:

random_array = np.random.randn(2, 3)
print(random_array)
# Output: A 2x3 array of random numbers from the standard normal distribution


# 3. np.random.randint()

# Single Random Integer:

random_integer = np.random.randint(1, 10)
print(random_integer)
# Output: A random integer between 1 (inclusive) and 10 (exclusive), e.g., 7

# Random Array of Integers:

random_array = np.random.randint(1, 10, size=(3, 3))
print(random_array)
# Output: A 3x3 array of random integers between 1 and 10


# >>>>>>  Setting Random Seeds: np.random.seed()

# Setting a Seed for Reproducibility:


np.random.seed(42)
print(np.random.rand(3))
# Output: [0.37454012 0.95071431 0.73199394]

np.random.seed(42)
print(np.random.rand(3))
# Output (same as above): [0.37454012 0.95071431 0.73199394]

# Different Results Without a Seed:

np.random.seed()
print(np.random.rand(3))
# Output: Random numbers (varies with each execution)

# Setting a Seed for Repeated Experiments:

np.random.seed(123)
array1 = np.random.rand(3)
np.random.seed(123)
array2 = np.random.rand(3)

print(np.array_equal(array1, array2))  # Output: True

# Using Random Functions After Setting a Seed:

np.random.seed(7)
print(np.random.randint(0, 10, size=5))
# Output: [4 9 6 3 3]
