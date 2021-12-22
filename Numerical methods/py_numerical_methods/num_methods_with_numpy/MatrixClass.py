import numpy as np

from copy import deepcopy


class Matrix:
    def __init__(self, eps_ind=7, name='matr_file_1.txt'):
        try:
            with open(name, 'r', encoding='utf-8') as f:
                temp = f.readlines()
                self.B = np.array([float(el.replace('\n', '').split()[-1]) for el in temp])
                self.matrix = np.array([list(map(float, (el.replace('\n', '').strip().split())))[:-1] for el in temp])
                self.eps = 10 ** ((-1) * eps_ind)
                self.eps_ind = eps_ind
        except IOError:
            print(f"{name} doesn't exist!")
        except Exception as err:
            print(str(err))

    def __str__(self):
        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[0]):
                if abs(self.matrix[i, j]) < self.eps:
                    self.matrix[i, j] = 0.0
                else:
                    self.matrix[i, j] = round(self.matrix[i, j], self.eps_ind)
        temp = "\n".join(['      '.join(list(map(str, el))) for el in self.matrix])
        return temp

    @staticmethod
    def row_change(matrix, ind1, ind2):
        matrix[[ind1, ind2]] = matrix[[ind2, ind1]]
        return matrix

    @staticmethod
    def is_less_eps(lst, eps):
        for el in lst:
            if el > eps:
                return False
        return True

    @staticmethod
    def rg(main_matrix, eps):
        matrix, main_n, main_m = deepcopy(main_matrix), *main_matrix.shape  # copy matrix
        n, m = main_n, main_m
        while True:
            for i in range(min(n, m)):
                if Matrix.is_less_eps(matrix[:, i], eps):
                    continue
                if abs(matrix[i, i]) < eps:  # if matrix[i, i] < eps, change rows
                    for z in range(i + 1, m):
                        if not matrix[z, i] < eps:
                            matrix = Matrix.row_change(matrix, i, z)
                            break
                else:  # else divide the current row of the matrix by matrix[i, i]
                    matrix[i] = [0.0 if p < i else matrix[i, p] / matrix[i, i] for p in range(m)]

                for j in range(i + 1, n):
                    div = matrix[j, i]  # save divisor for each row
                    for k in range(i, m):
                        matrix[j, k] -= div * matrix[i, k]
            ind = 0
            for i in range(n):  # search for zero columns
                flag = True
                for j in range(m):
                    if matrix[j, i] != 0.0:
                        flag = False
                        break
                if flag:
                    ind += 1
                else:
                    break
            if ind == 0:
                break
            else:  # start deleting zero columns
                for i in range(n):
                    matrix[i] = matrix[i, ind:m]  # end deleting zero columns
                n, m = len(matrix), len(matrix[0])

        if len(matrix[0]) != main_m:  # restoring the dimension of the matrix
            dif = main_m - len(matrix[0])
            for i in range(main_n):
                matrix[i] = [0.0] * dif + matrix[i]

        # start counting zero rows
        ind = main_n
        for i in range(main_n - 1, -1, -1):
            flag = False
            for j in range(main_m):
                if abs(matrix[i, j]) > eps:
                    flag = True
                    ind = i + 1
                    break
                else:
                    continue
            if flag:
                break
        # end counting zero rows
        return ind

    @staticmethod
    def inverse_matrix(main_matrix, eps, eps_ind):
        if Matrix.rg(main_matrix, eps) != main_matrix.shape[0]:
            return
        matrix, n = deepcopy(main_matrix), main_matrix.shape[0]  # copy matrix
        matrix = np.concatenate((matrix, np.eye(n)), axis=1)
        m = matrix.shape[1]
        for i in range(n):
            if abs(matrix[i, i]) < eps:  # if matrix[i, i] < eps, change rows
                for z in range(i + 1, m):
                    if not matrix[z, i] < eps:
                        matrix = Matrix.row_change(matrix, i, z)
                        break
            else:  # else divide the current row of the matrix by matrix[i, i]
                temp = matrix[i, i]
                matrix[i] = [0.0 if p < i else round(matrix[i, p] / temp, eps_ind) for p in range(m)]
            for j in range(i + 1, n):
                div = matrix[j, i]  # save divisor for each row
                for k in range(i, m):
                    matrix[j, k] -= div * matrix[i, k]
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                div = matrix[j, i]
                for k in range(i, m):
                    matrix[j, k] -= div * matrix[i, k]
        return matrix[:, m // 2: m]


A = Matrix()
print(Matrix.rg(A.matrix, A.eps))
print(Matrix.inverse_matrix(A.matrix, A.eps, A.eps_ind))
# Matrix.row_change(A.matrix, 0, 1)
# print(A)
