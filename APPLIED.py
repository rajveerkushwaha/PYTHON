import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print("Size:", a.size)
print("Shape:", a.shape)
print("Data type:", a.dtype)
print("Item size:", a.itemsize, 6)
print("NumPy version:", np.__version__)

b = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
print("Shape:", b.shape)
print("Size:", b.size)
print("Data type:", b.dtype)
print("Item size:", b.itemsize, "bytes")
print("Max value:", b.max())
print("Min value:", b.min())
print("Index of max value:", b.argmax())
print("Index of min value:", b.argmin())
print("Sum of all elements:", b.sum())
print("Sum along axis 1:", b.sum(axis=1))
print("Sum along axis 0:", b.sum(axis=0))

arr = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
print(arr[1, 1:3])

arr1 = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
c_copy = arr1.copy()
print(arr1)
print(c_copy)

c_view = arr1.view()
print(arr1)
print(c_view)

np.random.seed(2)
random_array = np.random.randint(1, 100, (3, 3))
print(random_array)

zeros_array = np.zeros((3, 3))
print(zeros_array)

ones_array = np.ones((3, 3))
print(ones_array)

identity_matrix = np.eye(5)
print(identity_matrix)

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = np.multiply(array1, array2)
print(result)


