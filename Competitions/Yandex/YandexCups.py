import numpy as np
"""Полное решение будет оценено в 2 балла.

Сравните два числа в двоичной системе счисления. Числа представлены последовательностью слов без пробелов,
обозначающих цифры (0 — zero, 1 — one).

Формат ввода
Первая строка содержит запись первого числа

Вторая строка содержит запись второго числа

Числа не содержат лидирующих нулей.

Формат вывода
Выведите символ > (ASCII 62), если первое число больше второго, символ < (ASCII 60), если второе число больше первого,
иначе выведите символ = (ASCII 61) ."""
def first_ex():
    first = input()
    second = input()
    first = int(first.replace('one', '1').replace('zero', '0'))
    second = int(second.replace('one', '1').replace('zero', '0'))
    if first > second:
        print('>')
    elif first < second:
        print('<')
    else:
        print('=')


"""Решение, корректно работающее в ограничениях 
1≤nm≤24, будет оценено в 2 балла.

Полное решение будет оценено в 4 балла (включая 2 балла за подзадачу выше).

Дана матрица 
n×m (n, m — степени двойки), заполненная целыми числами от 1 до nm
 (числа по возрастанию по строкам).
 За один шаг мы «складываем» матрицу пополам, как лист бумаги, поперек большей стороны 
 (по горизонтали или по вертикали) и суммируем числа, которые накладываются друг на друга, до тех пор, 
 пока не останется один элемент. Квадрат складываем по горизонтальной линии.
Элементы всех полученных матриц (в том числе и исходной) выписываем в одну последовательность.
Найдите количество различных выписанных чисел.
 """
n, m = list(map(int, input().split()))
ind = 1
matrix = np.zeros((n, m), dtype=np.int32)
lst = []
for i in range(0, n):
    for j in range(0, m):
        matrix[i, j] = ind
        ind += 1
while True:
    for row in matrix:
        for el in row:
            if el not in lst:
                lst.append(el)
    if matrix.shape == (1, 1):
        print(len(lst))
        break
    elif matrix.shape[0] < matrix.shape[1]:
        for i in range(matrix.shape[1] // 2):
            matrix[:, i] = matrix[:, i] + matrix[:, matrix.shape[1] - 1 - i]
        if matrix.shape[1] % 2 != 0:
            matrix = matrix[:, 0:matrix.shape[1] // 2 + 1]
        else:
            matrix = matrix[:, 0:matrix.shape[1] // 2]
    else:
        for i in range(matrix.shape[0] // 2):
            matrix[i, :] = matrix[i, :] + matrix[matrix.shape[0] - 1 - i, :]
        if matrix.shape[0] % 2 != 0:
            matrix = matrix[0:matrix.shape[0] // 2 + 1, :]
        else:
            matrix = matrix[0:matrix.shape[0] // 2, :]


