
def linear_search_first(arr, target):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1

        if arr[i] == target:
            print("Element found at index:", i)
            print("Number of comparisons:", comparisons)
            return i

    print("Element not found")
    print("Number of comparisons:", comparisons)
    return -1


arr = [10, 20, 30, 40, 20, 50]
target = 20

linear_search_first(arr, target)


def linear_search_all(arr, target):
    positions = []
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1

        if arr[i] == target:
            positions.append(i)

    if positions:
        print("Element found at indices:", positions)
    else:
        print("Element not found")

    print("Number of comparisons:", comparisons)


arr = [10, 20, 30, 20, 40, 20, 50]
target = 20
linear_search_all(arr, target)


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            print("Element found at index:", mid)
            print("Number of comparisons:", comparisons)
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    print("Element not found")
    print("Number of comparisons:", comparisons)
    return -1


arr = [10, 20, 30, 40, 50, 60, 70]
target = 50

binary_search(arr, target)















