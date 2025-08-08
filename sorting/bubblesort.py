def bubblesort(arr):
    swapped = False
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"Swapped {arr[j]} and {arr[j + 1]}: {arr}")
        if not swapped:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
bubblesort(arr)

print("Sorted array:", arr)