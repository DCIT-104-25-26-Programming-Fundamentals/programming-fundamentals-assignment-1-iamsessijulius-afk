# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
def read_matrix(rows, cols):
  matrix = []
  for i in range(rows):
    row = [int(x)for x in input(f"enter row {i + 1}: ").split()]
    matrix.append(row)
  return matrix

def print_matrix(matrix):
  for row in matrix:
    print(*row)

def transpose_matrix(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  result = [[0] * rows for _ in range(cols)]
  for i in range(rows):
    for j in range(cols):
      result[j][i] = matrix[i][j]
  return result

def add_matrices(A, B):
  rows = len(A)
  cols = len(A[0])
  result = [[0] * cols for _ in range(rows)]
  for i in range(rows):
    for j  in range(cols):
      result[i][j] = A[i][j] + B[i][j]

  return result

def multiply_matrices(A, B):
  rows_A = len(A)
  cols_A = len(A[0])
  cols_B = len(B[0])
  result = [[0] * cols_B for _ in range(rows_A)]
  for i in range(rows_A):
    for j in range(cols_B):
      for k in range(cols_A):
        result[i][j] += A[i][k] * B[k][j]
  return result

r = int(input("Enter number of rows: "))
c = int(input("Enter numbber of columns: "))
A = read_matrix(r, c)
print_matrix(transpose_matrix(A))

r = int(input("Enter number of rows: "))
c = int(input("Enter numbber of columns: "))
A = read_matrix(r, c)
B = read_matrix(r, c)
print_matrix(add_matrices(A, B))

r_A = int(input("Enter rows for Matrix A: "))
c_A = int(input("Enter cols for A / rows for B: "))
c_B = int(input("Enter cols for Matrix B: "))
A = read_matrix(r_A, c_A)
B = read_matrix(c_A, c_B)
print_matrix(multiply_matrices(A, B))

