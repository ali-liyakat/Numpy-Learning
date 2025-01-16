import numpy as np

# Saving Arrays

# 1. np.save()

# Saving an 1D Array:

arr = np.array([1, 2, 3, 4, 5])
np.save('my_array.npy', arr)
print("Array saved")

# Saving a 2D Array:

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
np.save('my_2d_array.npy', arr_2d)
print("2D array saved to 'my_2d_array.npy'")



# 2. np.savetxt()

# Saving as a Text File:

arr = np.array([1.23, 4.56, 7.89])
np.savetxt('my_array.txt', arr)
print("Array saved to 'my_array.txt'")


# Saving with a Custom Format:

arr = np.array([1.23, 4.56, 7.89])
np.savetxt('formatted_array.txt', arr, fmt='%.2f')  # Save with 2 decimal places
print("Formatted array saved to 'formatted_array.txt'")


# Saving a 2D Array with Delimiters:

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt('my_2d_array.csv', arr_2d, delimiter=',', fmt='%d')
print("2D array saved to 'my_2d_array.csv'")



# Loading Arrays

# 1. np.load()

# Loading a Binary .npy File:

arr = np.array([1, 2, 3, 4, 5])
np.save('my_array.npy', arr)  # Save the array
loaded_arr = np.load('my_array.npy')  # Load the array
print(loaded_arr)
# Output: [1 2 3 4 5]

# Loading a .npz File:

np.savez('multi_arrays.npz', arr1=arr, arr2=arr + 5)  # Save multiple arrays
data = np.load('multi_arrays.npz')  # Load the .npz file
print(data['arr1'])  # Access 'arr1'
print(data['arr2'])  # Access 'arr2'


# 2. np.loadtxt()

# Loading a Text File:

np.savetxt('my_array.txt', arr)  # Save the array as text
loaded_arr = np.loadtxt('my_array.txt')
print(loaded_arr)
# Output: [1. 2. 3. 4. 5.]


# Loading a CSV File:

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt('my_2d_array.csv', arr_2d, delimiter=',', fmt='%d')  # Save as CSV
loaded_arr = np.loadtxt('my_2d_array.csv', delimiter=',')
print(loaded_arr)
# Output: [[1. 2. 3.]
#          [4. 5. 6.]]


# Selecting Specific Columns:

loaded_cols = np.loadtxt('my_2d_array.csv', delimiter=',', usecols=(0, 2))
print(loaded_cols)
# Output: [[1. 3.]
#          [4. 6.]]
