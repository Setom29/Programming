def binary_search(arr, el):  # lst - sorted list
    start, mid, end = 0, (len(arr) - 1) // 2, len(arr) - 1
    while start <= end:
        if arr[mid] == el:
            return mid
        elif arr[mid] > el:
            end = mid - 1
            mid = (start + end) // 2
        else:
            start = mid + 1
            mid = (start + end) // 2
    return None


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 14, 15, 15, 16, 16, 17, 19, 23]
print(binary_search(lst, 20))
