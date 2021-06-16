import random


def bubble_sort(array):  # заканчивает итерацию, если no_swap остается True, т.е. не было перестановок элементов.
    n = 1
    span = 0
    while n < len(array):
        no_swap = True
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                no_swap = False
        if no_swap:
            break
        n += 1
        span += 1
    print(array)
    print(f'Количество проходов по списку: {span}.')


lst = [random.randint(-100, 99) for i in range(30)]
print(lst)
bubble_sort(lst)
