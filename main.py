import numpy as np

def add_matrices(a, b):
    return a + b

def subtract_matrices(a, b):
    return a - b

def multiply_matrices(a, b):
    return np.dot(a, b)

def transpose_matrix(a):
    return a.T

def determinant_matrix(a):
    return np.linalg.det(a)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Addition:\n", add_matrices(a, b))
print("Subtraction:\n", subtract_matrices(a, b))
print("Multiplication:\n", multiply_matrices(a, b))
print("Transpose of A:\n", transpose_matrix(a))
print("Determinant of A:\n", determinant_matrix(a))
