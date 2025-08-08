def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Inserted {key} at position {j + 1}: {arr}")

arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)

print("Sorted array:", arr)