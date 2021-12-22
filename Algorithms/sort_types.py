import random
from copy import copy


# https://pythonru.com/osnovy/top-5-algoritmov-sortirovki-na-python#:~:text=Топ-5%20алгоритмов%20сортировки%20на%20Python


def bubble_sort(lst):
    n = 1
    lst = copy(lst)
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


# ----------------------------------------------------------------


def selection_sort(lst):
    lst = copy(lst)
    for i in range(len(lst)):
        min_ind = i
        for j in range(i + 1, len(lst)):
            if lst[min_ind] > lst[j]:
                min_ind = j
        lst[i], lst[min_ind] = lst[min_ind], lst[i]
    return lst


# ----------------------------------------------------------------

def insertion_sort(lst):
    lst = copy(lst)
    for i in range(1, len(lst)):
        spam = lst[i]
        j = i
        while lst[j - 1] > spam and j > 0:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = spam
        print(lst)
    return lst


# ----------------------------------------------------------------


def shell_sort(lst):
    assert len(lst) < 4000, 'Массив слишком большой. Используйте другую сортировку.'
    lst = copy(lst)

    def new_increment(lst):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(lst) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(lst):
        for i in range(increment, len(lst)):
            for j in range(i, increment - 1, -increment):
                if lst[j - increment] <= lst[j]:
                    break
                lst[j], lst[j - increment] = lst[j - increment], lst[j]
    return lst


# -----------------------------------------------------------------
def merge_sort(array, start, end):
    """Sorts the list from indexes start to end - 1 inclusive."""
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge_list(array, start, mid, end)


def merge_list(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            array[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            array[k] = right[j]
            j = j + 1
            k = k + 1


# ----------------------------------------------------------------
def quick_sort(lst):  # изменяет переданный массив.
    if len(lst) <= 1:
        return lst
    pivot = random.choice(lst)
    s_ar = []
    m_ar = []
    l_ar = []
    for item in lst:
        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception('unknown error')
    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)


# ----------------------------------------------------------------
def quick_sort_no_memory(array, fst, lst):
    if fst >= lst:
        return lst
    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quick_sort_no_memory(array, fst, j)
    quick_sort_no_memory(array, i, lst)


# ----------------------------------------------------------------

def revers(lst):  # аналог array.reverse()
    lst = copy(lst)
    for i in range(len(lst) // 2):
        lst[i], lst[len(arr) - i - 1] = lst[len(arr) - i - 1], lst[i]
    return lst


# ----------------------------------------------------------------

# timsort Сложность: O(n log n), Устойчивость: устойчивая,
# Тип: гибридная(вставками + слиянием), Потребление памяти: O(n)

arr = [i for i in range(20)]
random.shuffle(arr)
print(arr)
print(insertion_sort(arr))
# quick_sort_no_memory(arr, 0, len(arr) - 1)
# print(arr)
"""
array.sort(reverse=True) позволяет развернуть и отсортировать
tuple(sorted(t)) где t - кортеж. Это позволяет сортировать кортеж.
У sorted также есть атрибут reverse.
"""
