def binary_search(lst, value):

    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == value:
            return True
        elif lst[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False
