# Numpy Begineer Tutorial as mentioned in Readme.md

import numpy as np

# Creating a 1D array
a = np.array([1, 2, 3])
print(a)

# Creating a 2D array
b = np.array([[1, 2], [3, 4]])
print(b)

# Creating a 3D array
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c)

# Creating an array of all zeros
d = np.zeros((2, 2))
print(d)

# Creating an array of all ones
e = np.ones((2, 2))
print(e)

# Creating a constant array
f = np.full((2, 2), 7)
print(f)

# Creating an identity matrix
g = np.eye(2)
print(g)

# Creating an array filled with random values
h = np.random.random((2, 2))
print(h)

# Creating an array of evenly spaced values
i = np.arange(10)
print(i)

# Creating an array of evenly spaced values
j = np.arange(1, 9, 2)
print(j)

# Creating an array of evenly spaced values
k = np.linspace(0, 1, 5)
print(k)

# Creating a 3x3 array of normally distributed random values
l = np.random.normal(0, 1, (3, 3))
print(l)

# Creating a 3x3 array of random integers in the interval [0, 10)
m = np.random.randint(0, 10, (3, 3))
print(m)

# Creating a 3x3 identity matrix
n = np.eye(3)
print(n)

# Creating an uninitialized array of three integers
o = np.empty(3)
print(o)

# Creating an array of ones
p = np.ones(10)
print(p)

# Creating an array of zeros
q = np.zeros(10)
print(q)


# Creating an array of 10 fives
r = np.ones(10) * 5
print(r)

# Basic Operations
a = np.array([1, 2, 3, 4])
b = np.ones(4) + 1

# Adding two arrays
print(a + b)

# Subtracting two arrays
print(a - b)

# Multiplying two arrays
print(a * b)

# Dividing two arrays
print(a / b)

# Squaring an array
print(a ** 2)

# Taking the sin of an array
print(np.sin(a))

# Taking the cos of an array
print(np.cos(a))

# Taking the log of an array
print(np.log(a))

# Dot product of two arrays
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.ones((3, 2))

print(a.dot(b))

# Summing all the elements of an array
x = np.array([1, 2, 3, 4])
print(np.sum(x))

# Summing the rows or columns of an array
x = np.array([[1, 1], [2, 2]])
print(x.sum(axis=0))
print(x.sum(axis=1))

# Transposing an array
x = np.array([[1, 2], [3, 4]])
print(x)
print(x.T)

# Creating a view of an array
x = np.array([1, 2, 3])
y = x.view()
y[0] = 100
print(x)

# Creating a copy of an array
x = np.array([1, 2, 3])
y = x.copy()
y[0] = 100
print(x)

# Reshaping an array
grid = np.arange(1, 10).reshape((3, 3))
print(grid)

# Concatenating arrays
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = np.concatenate([x, y])
print(z)

# Universal Functions
# Creating an array of angles
theta = np.linspace(0, np.pi, 3)

# Taking the sin of the angles
print(np.sin(theta))

# Taking the cos of the angles
print(np.cos(theta))

# Taking the tan of the angles
print(np.tan(theta))

# Taking the inverse sin of the angles
x = [-1, 0, 1]
print(np.arcsin(x))

# Taking the inverse cos of the angles
x = [-1, 0, 1]
print(np.arccos(x))

# Taking the inverse tan of the angles
x = [-1, 0, 1]
print(np.arctan(x))

# Taking the exponential of the angles
x = [1, 2, 3]
print(np.exp(x))

# Taking the natural log of the angles
x = [1, 2, 3]
print(np.log(x))

# Taking the base 2 log of the angles
x = [1, 2, 3]
print(np.log2(x))

# Taking the base 10 log of the angles
x = [1, 2, 3]
print(np.log10(x))

# Indexing, Slicing and Iterating
# One-dimensional arrays
a = np.arange(10) ** 3
print(a)

# Accessing the 6th element of the array
print(a[5])

# Accessing the 6th element through the end of the array
print(a[5:])
print(a[5:10])

# Accessing every other element of the array
print(a[::2])

# Accessing every other element of the array, starting at index 1
print(a[1::2])

# Accessing the values of the array at the specified indices
print(a[[1, 2, 3]])

# Reversing the array
print(a[::-1])

# Multidimensional arrays
def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int)
print(b)

# Accessing the element at row 2, column 3
print(b[2, 3])

# Accessing the element at row 0, column 0
print(b[0, 0])

# Accessing the first row of the array
print(b[0, :])

# Accessing the first column of the array
print(b[:, 0])

# Accessing the last row of the array
print(b[-1, :])

# Accessing the last column of the array
print(b[:, -1])

# Shape Manipulation
# Flattening an array
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ravel())

# Reshaping an array
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.reshape((3, 2)))

# Transposing an array
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.T)

# Stacking arrays vertically
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
print(np.vstack((a, b)))

# Stacking arrays horizontally
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
print(np.hstack((a, b)))

# Splitting arrays vertically
a = np.arange(16).reshape((4, 4))
upper, lower = np.vsplit(a, [2])
print(upper)
print(lower)

# Splitting arrays horizontally
a = np.arange(16).reshape((4, 4))
left, right = np.hsplit(a, [2])
print(left)
print(right)

# Copies and Views
# No Copy at All
a = np.arange(12)
b = a
print(b is a)

# View or Shallow Copy
a = np.arange(12)
b = a.view()
print(b is a)
print(b.base is a)
print(b.flags.owndata)

# Deep Copy
a = np.arange(12)
b = a.copy()
print(b is a)
print(b.base is a)
print(b.flags.owndata)

# Broadcasting rules
# Adding a scalar to an array
a = np.ones((3, 3))
b = a + 3
print(b)

# Adding a one-dimensional array to a two-dimensional array
a = np.arange(3)
b = np.arange(3).reshape((3, 1))
print(a)
print(b)
print(a + b)

# Comparisons, Masks, and Boolean Logic
# Comparing arrays
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print(a == b)
print(a > b)

# Comparing array to scalar
a = np.array([1, 2, 3, 4])
b = 2
print(a == b)
print(a > b)

# Using logical operators
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print(np.logical_or(a > b, a < b))
print(np.logical_and(a > b, a < b))

# Advanced indexing
# Using Boolean masks
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[a > 2])

# Using integer masks
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[[0, 1, 2], [0, 1, 0]])

