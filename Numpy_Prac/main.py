"""
NUMPY BASICS – PRACTICE + EXPLANATION

This file contains:
1. How to create arrays
2. Array properties
3. Useful NumPy functions

Read comments carefully. Run file to see outputs.
"""

# Import NumPy library
import numpy as np


# ================================
# 1. Creating 1D Array
# ================================
arr = np.array([1, 2, 3, 4, 5])

print("1D Array:", arr)

# dtype → type of elements
print("Data Type:", arr.dtype)

# shape → structure (5 elements → (5,))
print("Shape:", arr.shape)

# ndim → number of dimensions (1D here)
print("Dimensions:", arr.ndim)

# size → total elements
print("Total Elements:", arr.size)


# ================================
# 2. Creating 2D Array (Matrix)
# ================================
arr2 = np.array([[1.33, 1.2], [4.5, 6.7]])

print("\n2D Array:\n", arr2)

print("Data Type:", arr2.dtype)
print("Shape:", arr2.shape)   # (rows, columns)
print("Dimensions:", arr2.ndim)
print("Total Elements:", arr2.size)


# ================================
# 3. Range-Based Arrays
# ================================

# arange(start, stop, step)
print("\nnp.arange(0, 10, 2):", np.arange(0, 10, 2))

# default start = 0
print("np.arange(5):", np.arange(5))

# reverse using negative step
print("np.arange(10, 0, -2):", np.arange(10, 0, -2))


# ================================
# 4. linspace()
# ================================
# linspace(start, stop, number_of_points)
print("\nnp.linspace(0, 1, 5):", np.linspace(0, 1, 5))


# ================================
# 5. Special Arrays
# ================================

# zeros → filled with 0
print("\nZeros Matrix:\n", np.zeros((2, 3)))

# ones → filled with 1
print("Ones Matrix:\n", np.ones((2, 3)))

# identity matrix
print("Identity Matrix:\n", np.eye(3))


# ================================
# 6. Random Values
# ================================

# random floats between 0 and 1
print("\nRandom Float Matrix:\n", np.random.rand(2, 3))

# random integers
print("Random Integers:\n", np.random.randint(0, 10, (2, 3)))


# ================================
# FINAL NOTE
# ================================
"""
KEY TAKEAWAYS:

- NumPy arrays are faster than Python lists
- shape = structure
- ndim = dimensions
- size = total elements
- arange → step-based range
- linspace → fixed number of values
- zeros/ones/eye → special matrices
- random → useful for ML/data work

Practice creating arrays and exploring their properties to get comfortable with NumPy basics!
"""