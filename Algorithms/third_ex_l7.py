import random
from copy import copy


def find_middle(array):
    # данная функция проходит по массиву и ищет максимальный и минимальный элементы и удаляет их методом .pop()
    array = copy(array)
    while len(array) > 1:
        min_ind = 0
        max_ind = 0
        for j in range(len(array)):
            if array[j] >= array[max_ind]:
                max_ind = j
            if array[j] <= array[min_ind]:
                min_ind = j
        if max_ind > min_ind:
            array.pop(max_ind)
            array.pop(min_ind)
        if max_ind < min_ind:
            array.pop(min_ind)
            array.pop(max_ind)

    else:
        print(array[0])


m = 3
lst = [random.randint(-100, 100) for i in range(2 * m + 1)]
print(lst)
find_middle(lst)
