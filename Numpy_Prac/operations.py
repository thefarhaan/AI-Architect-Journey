"""
Purpose:
    Demonstrates a wide range of NumPy operations including indexing, arithmetic,
    broadcasting, aggregation, matrix multiplication, and random number generation.

Key Concepts:
    - Array indexing and slicing
    - Element-wise operations
    - Boolean comparisons
    - Mathematical functions
    - Broadcasting
    - Reshaping and flattening
    - Aggregation functions (sum, mean, min, max)
    - Matrix multiplication
    - Random number generation

Libraries Used:
    - NumPy → used for efficient numerical array operations
"""

# ============================
# IMPORTS
# ============================

import numpy as np  # NumPy → core numerical computing library


# ============================
# ARRAY CREATION & INDEXING
# ============================

a = np.array([[1,2,3],[4,5,6]])

print(a)

# Access element at row 1, column 2 → 6
print(a[1,2])

# Access element at row 0, column 1 → 2
print(a[0,1])

# First row
print(a[0,:])

# Second row
print(a[1,:])


# ============================
# ELEMENT-WISE OPERATIONS
# ============================

b = np.array([1,2,3])
c = np.array([4,5,6])

# Element-wise addition
print(b+c)

# Element-wise subtraction
print(b-c)

# Element-wise multiplication
print(b*c)

# Element-wise division
print(b/c)

# Powers
print(b**2)
print(b**3)


# ============================
# BOOLEAN OPERATIONS
# ============================

d =np.array([1,2,3])

# Greater than comparison
print(d>1)

# Equality check
print(d==1)

# Not equal check
print(d!=1)


# ============================
# MATHEMATICAL FUNCTIONS
# ============================

# Square root
print(np.sqrt([1,4,9]))

# Exponential (e^x)
print(np.exp([1,4,9]))

# Sine function (uses radians)
print(np.sin([0,np.pi/2]))


# ============================
# BROADCASTING
# ============================

# Column vector
e = np.array([[1],[2],[3]])

# Row vector
f = np.array([4,5,6])

# Broadcasting expands to (3x3) for addition
print(e+f)


# ============================
# RESHAPING & FLATTENING
# ============================

g = np.array([[1,2],[3,4],[5,6]])

print(g)

# Reshape to 2x3
print(g.reshape(2,3))

# Flatten to 1D array
print(g.flatten())


# ============================
# AGGREGATION OPERATIONS
# ============================

h = np.array([[1,2,3],[4,5,6]])

# Sum of all elements → 21
print(h.sum())

i = np.array([1,2,3,4,5])

# Mean value → 3.0
print(np.mean(i))

# Sum → 15
print(np.sum(i))

# Minimum → 1
print(np.min(i))

# Maximum → 5
print(np.max(i))



# ============================
# MATRIX MULTIPLICATION
# ============================

# Define first matrix (2x2)
j = np.array([[1,2],[3,4]])

# Define second matrix (2x2)
k = np.array([[5,6],[7,8]])

# Matrix multiplication (dot product)
# Rule:
# Each element = (row from j) • (column from k)

# Step-by-step manual calculation:

# First row of j → [1, 2]
# First column of k → [5, 7]
# (1×5) + (2×7) = 5 + 14 = 19

# First row of j → [1, 2]
# Second column of k → [6, 8]
# (1×6) + (2×8) = 6 + 16 = 22

# Second row of j → [3, 4]
# First column of k → [5, 7]
# (3×5) + (4×7) = 15 + 28 = 43

# Second row of j → [3, 4]
# Second column of k → [6, 8]
# (3×6) + (4×8) = 18 + 32 = 50

# Final result matrix:
# [[19, 22],
#  [43, 50]]

print(j.dot(k))  # Performs matrix multiplication using NumPy


# ============================
# RANDOM NUMBER GENERATION
# ============================

# Set seed for reproducibility (ensures same random results each run)
print(np.random.seed(0))

# Random values in range [0, 1), shape (2x2)
print(np.random.rand(2,2))

# Random values in range [0, 1), shape (3x4)
print(np.random.rand(3,4))

# Random integers between 1 and 99 (10 values)
print(np.random.randint(1,100, size= 10))

# Random integers between 1 and 99999 (5 values)
print(np.random.randint(1,100000, size= 5))