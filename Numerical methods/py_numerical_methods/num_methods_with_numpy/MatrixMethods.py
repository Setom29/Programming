import numpy as np
from math import sqrt
from MatrixClass import Matrix
# import MatrixOperations
from copy import deepcopy, copy


def is_valid(matrix):
    """
    Check if the rank of the matrix is equal to it's dimension
    """
    rg = Matrix.rg(matrix.matrix, matrix.eps)
    if rg == len(A.matrix) and len(A.matrix[0]) == len(A.matrix):
        return True
    return False


def gauss(matrix):
    """
    Returns list of solutions to the given system of linear equations using the Gauss method,
    if  is_valid(matrix) returns True.
    """
    if not is_valid(matrix):
        return
    matrix, b, eps, eps_ind, n = deepcopy(matrix.matrix), matrix.B[:], matrix.eps, matrix.eps_ind, len(matrix.matrix)
    for i in range(n):
        is_zero_col = False
        if abs(matrix[i, i]) < eps:  # if matrix[i, i] < eps, change rows
            for z in range(i + 1, n):
                if not matrix[z, i] < eps:
                    matrix = Matrix.row_change(matrix, i, z)
                    b[i], b[z] = b[z], b[i]
                    break
                if z == n - 1:
                    is_zero_col = True
            if is_zero_col:
                continue
        else:  # else divide the current row of the matrix by matrix[i, i]
            temp = matrix[i, i]
            matrix[i] = [0.0 if p < i else round(matrix[i, p] / temp, eps_ind) for p in range(n)]
            b[i] = round(b[i] / temp, eps_ind)
        for j in range(i + 1, n):
            div = matrix[j, i]  # save divisor for each row
            for k in range(i, n):
                matrix[j, k] -= div * matrix[i, k]
            b[j] -= div * b[i]
        # reverse
    x = [0.0] * n
    x[n - 1] = b[n - 1] / matrix[n - 1, n - 1]
    for i in range(n - 1, -1, -1):
        temp = 0
        for j in range(n - 1, i, -1):
            temp += x[j] * matrix[i, j]
        x[i] = (b[i] - temp) / matrix[i, i]
    return [round(el, eps_ind) for el in x]


def gauss_with_selection(matrix):
    """
    Returns list of solutions to the given system of linear equations using the Gauss method
    with the selection of the main element, if is_valid(matrix) returns True.
    """
    if not is_valid(matrix):
        return
    matrix, b, eps, eps_ind, n = deepcopy(matrix.matrix), matrix.B[:], matrix.eps, matrix.eps_ind, len(matrix.matrix)
    for i in range(n):
        max_el = i
        is_zero_col = 0
        for z in range(i, n):
            is_zero_col += 1
        if is_zero_col == 0:
            continue
        else:  # else divide the current row of the matrix by matrix[i, i]
            for z in range(i + 1, n):
                if abs(matrix[z, i]) > abs(matrix[max_el, i]):
                    max_el = z
            matrix = Matrix.row_change(matrix, i, max_el)
            b[i], b[max_el] = b[max_el], b[i]
            temp = matrix[i, i]
            matrix[i] = [0.0 if p < i else round(matrix[i, p] / temp, eps_ind) for p in range(n)]
            b[i] = round(b[i] / temp, eps_ind)
        for j in range(i + 1, n):
            div = matrix[j, i]  # save divisor for each row
            for k in range(i, n):
                matrix[j, k] -= div * matrix[i, k]
            b[j] -= div * b[i]
        # reverse
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / matrix[n - 1, n - 1]
    for i in range(n - 1, -1, -1):
        temp = 0
        for j in range(n - 1, i, -1):
            temp += x[j] * matrix[i, j]
        x[i] = (b[i] - temp) / matrix[i, i]
    return [round(el, eps_ind) for el in x]


def qr_Givens(main_matrix):
    matrix, b = deepcopy(main_matrix.matrix), copy(main_matrix.B)
    n = matrix.shape[0]
    c = np.zeros((n, n))
    s = np.zeros((n, n))
    # Прямой ход
    if Matrix.rg(matrix, main_matrix.eps) != n:
        return
    for k in range(0, n - 1):  # "Большой" шаг (исключение переменных)
        for t in range(k + 1, n):  # "Малый" шаг
            c[k][t] = matrix[k][k] / (sqrt(matrix[k][k] * matrix[k][k] + matrix[t][k] * matrix[t][k]))
            s[k][t] = matrix[t][k] / (sqrt(matrix[k][k] * matrix[k][k] + matrix[t][k] * matrix[t][k]))

            #  Умножение матрицы matrix[][] на T[k][t]
            a_kk = matrix[k][k]
            a_tk = matrix[t][k]
            a_kt = matrix[k][t]
            a_tt = matrix[t][t]
            matrix[k][k] = a_kk * c[k][t] + a_tk * s[k][t]
            matrix[k][t] = a_kt * c[k][t] + a_tt * s[k][t]
            matrix[t][k] = -a_kk * s[k][t] + a_tk * c[k][t]
            matrix[t][t] = -a_kt * s[k][t] + a_tt * c[k][t]

            # Вектор свободных членов умножается на T[k][t]
            bk = b[k]
            bt = b[t]
            b[k] = bk * c[k][t] + bt * s[k][t]
            b[t] = -bk * s[k][t] + bt * c[k][t]
    # Теперь матрица matrix[][] -- верхняя диагональная.

    # Обратный ход
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / matrix[n - 1, n - 1]
    for i in range(n - 1, -1, -1):
        temp = 0
        for j in range(n - 1, i, -1):
            temp += x[j] * matrix[i, j]
        x[i] = (b[i] - temp) / matrix[i, i]
    # x[n - 1] = b[n - 1] / matrix[n - 1, n - 1]
    # for t in range(n - 1, -1, -1):
    #     temp = b[t - 1]
    #     for k in range(t + 1, n):
    #         temp -= x[k - 1] * matrix[t - 1, k - 1]
    #         x[t - 1] = temp / matrix[t - 1, t - 1]
    return matrix, b, x


A = Matrix()
print(qr_Givens(A))

# g_ans = gauss(A)
# if g_ans is None:
#     print('Indefinite system of linear equations')
# else:
#     print(g_ans)
#
# g_ans = gauss_with_selection(A)
# if g_ans is None:
#     print('Indefinite system of linear equations')
# else:
#     print(g_ans)
