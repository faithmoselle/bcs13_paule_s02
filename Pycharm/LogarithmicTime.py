def log(arr, num):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < num:
            low = mid + 1

        elif arr[mid] > num:
            high = mid - 1

        else:
            return mid
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 2

index = log(arr, num)

if index != -1:
    print(f"{num} is at index {index}")
else:
    print(f"Element {num} could not be found.")
