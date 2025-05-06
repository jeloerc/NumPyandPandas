import numpy as np  # np is the standard convention

# Create arrays
list_data = [1, 2, 3, 4, 5]
arr1d = np.array(list_data)
print(f"1D Array: {arr1d}")
print(f"Shape: {arr1d.shape}, Dimensions: {arr1d.ndim}, Type: {arr1d.dtype}")

matrix = [[1, 2, 3], [4, 5, 6]]
arr2d = np.array(matrix)
print(f"\n2D Array (Matrix):\n{arr2d}")
print(f"Shape: {arr2d.shape}, Dimensions: {arr2d.ndim}")

# Create special arrays
zeros_arr = np.zeros((2, 3))  # 2x3 array of zeros
ones_arr = np.ones(4)         # 1x4 array of ones
range_arr = np.arange(0, 10, 2)  # Like range(), but returns an array (start, stop_excluded, step)
print(f"\nArray of zeros:\n{zeros_arr}")
print(f"Array of ones: {ones_arr}")
print(f"Array with arange: {range_arr}")

# Basic element-wise operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum_result = a + b
product_result = a * 2
print(f"\nSum of a + b: {sum_result}")
print(f"Product of a * 2: {product_result}")

# Indexing and slicing
print(f"\nFirst element of arr1d: {arr1d[0]}")
print(f"Last two elements of arr1d: {arr1d[-2:]}")
print(f"Element at row 0, column 1 of arr2d: {arr2d[0, 1]}")  # or arr2d[0][1]
print(f"Entire first row of arr2d: {arr2d[0, :]}")  # or arr2d[0]
print(f"Entire second column of arr2d: {arr2d[:, 1]}")

# Math functions
print(f"\nSquare root of arr1d: {np.sqrt(arr1d)}")
print(f"Total sum of arr2d: {np.sum(arr2d)}")
print(f"Mean of the first column of arr2d: {np.mean(arr2d[:, 0])}")
