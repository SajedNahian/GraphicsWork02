"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

# print the matrix such that it looks like
# the template in the top comment


def print_matrix(matrix):
    rowCount = get_row_count(matrix)
    colCount = get_col_count(matrix)
    for y in range(rowCount):
        line = ''
        for x in range(colCount):
            line += str(matrix[x][y]) + ' '
        print(line[:-1])

# turn the paramter matrix into an identity matrix
# you may assume matrix is square


def ident(matrix):
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            if (x == y):
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0

# multiply m1 by m2, modifying m2 to be the product
# m1 * m2 -> m2


def matrix_mult(m1, m2):
    nm = new_matrix(len(m1[0]), len(m2))
    for rowNum in range(get_row_count(m1)):
        for colNum in range(get_col_count(m2)):
            row = get_row(m1, rowNum)
            col = get_col(m2, colNum)
            value = multiply_add_two_arrays(row, col)
            set_value(nm, rowNum, colNum, value)
    # print_matrix(nm)
    m2[:] = nm


def multiply_add_two_arrays(arr1, arr2):
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * arr2[i]
    return sum


def get_value(matrix, row, col):
    return matrix[col][row]


def set_value(matrix, row, col, value):
    matrix[col][row] = value


def get_row_count(matrix):
    if (len(matrix) == 0):
        return 0
    return len(matrix[0])


def get_col_count(matrix):
    return len(matrix)


def get_row(matrix, row):
    arr = []
    for i in range(get_col_count(matrix)):
        arr.append(get_value(matrix, row, i))
    return arr


def get_col(matrix, col):
    return matrix[col]


def new_matrix(rows=4, cols=4):
    m = []
    for c in range(cols):
        m.append([])
        for r in range(rows):
            m[c].append(0)
    return m
