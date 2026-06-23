def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Example
arr = [1, 3, 5, 7, 9]
x = 7

ans = binary_search(arr, x)

if ans != -1:
    print("Found at index", ans)
else:
    print("Not found")