# from copy import deepcopy
from MatrixClass import Matrix


def transposition(matrix):
    transpose_matrix = []
    for i in range(len(matrix)):
        transpose_matrix.append([])
        for j in range(len(matrix[0])):
            transpose_matrix[i].append(matrix[j][i])
    return Matrix(transpose_matrix, None)


def matrix_op(a, b, op):
    if op == '*' and (type(b) != float and type(b) != int):
        if len(a[0]) == len(b):
            c = []
            for i in range(len(a[0])):
                c.append([])
                res = 0
                for j in range(len(b)):
                    for k in range(len(a)):
                        res += a[i][k] * b[k][j]
                    c[i].append(res)
            return Matrix(c, None)
        else:
            print('Index Error (matrix multiplication)')
    elif op == '*':
        return Matrix([[a[i][j] * b for j in range(len(a[0]))] for i in range(len(a))], None)
    elif op == '+':
        if len(a) == len(b) and len(a[0]) == len(b[0]):
            return Matrix([[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))], None)
        else:
            print('Index Error (matrix summation)')
    elif op == '-':
        if len(a) == len(b) and len(a[0]) == len(b[0]):
            return Matrix([[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))], None)
        else:
            print('Index Error (matrix subtraction)')


A = [[1, 2], [1, 2]]
B = [[3, 4], [3, 4]]

print(matrix_op(A, B, '-'))
