from copy import deepcopy


class Matrix:

    def __init__(self, matrix, name='matr_file_1.txt'):
        if name is not None:
            try:
                with open(name, 'r', encoding='utf-8') as matr_file:
                    temp = matr_file.readlines()
                    self.B = [el[-1] for el in temp]
                    self.matrix = [list(map(float, (el.replace('\n', '').strip().split())))[:-1] for el in temp]
                    self.eps = 10 ** (-7)
            except IOError:
                print(f"{name} doesn't exist!")
        else:
            self.matrix = matrix
            self.eps = 10 ** (-7)

    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if abs(self.matrix[i][j]) < self.eps:
                    self.matrix[i][j] = 0
                else:
                    self.matrix[i][j] = round(self.matrix[i][j], 7)
        temp = "\n".join(['      '.join(list(map(str, el))) for el in self.matrix])
        return temp

    @staticmethod
    def row_change(matrix, ind1, ind2):
        matrix[ind1], matrix[ind2] = matrix[ind2], matrix[ind1]
        return matrix

    def rg(self):
        matrix = deepcopy(self.matrix)
        for i in range(len(matrix)):
            flag = True
            if abs(matrix[i][i]) < self.eps:
                flag = False
                for ind in range(i + 1, len(matrix)):
                    if abs(matrix[ind][i]) > self.eps:
                        matrix = Matrix.row_change(matrix, i, ind)
                        flag = True
                        break
            if flag:
                temp = matrix[i][i]
                for m in range(len(matrix)):
                    matrix[i][m] = matrix[i][m] / temp
                for j in range(i + 1, len(matrix)):
                    temp = matrix[j][i]
                    for k in range(i, len(matrix)):
                        matrix[j][k] -= matrix[i][k] * temp
            else:
                temp = matrix[i][i]
                for m in range(len(matrix)):
                    matrix[i][m] = matrix[i][m] / temp
                for j in range(i + 1, len(matrix)):
                    temp = matrix[j][i]
                    for k in range(i, len(matrix)):
                        matrix[j][k] -= matrix[i][k] * temp
        return Matrix(matrix, None)


matr = Matrix(None)
print(matr.rg())
