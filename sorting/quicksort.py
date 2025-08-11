# 1 solution
def quicksort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    # Partitioning the array
    pivot = arr[len(arr) // 2]
    print(f"Pivot chosen: {pivot}")
    # Dividing the array into three parts
    left = [x for x in arr if x < pivot]
    print(f"Left partition: {left}")
    # Elements equal to the pivot
    middle = [x for x in arr if x == pivot]
    print(f"Middle partition: {middle}")
    # Elements greater than the pivot
    right = [x for x in arr if x > pivot]
    print(f"Right partition: {right}") 
    # Recursively apply quicksort to the partitions
    return quicksort(left) + middle + quicksort(right)

# 2nd solution
def qs(arr):
    qshelper(arr,0,len(arr)-1)
    return arr

def qshelper(arr, start, end):
    # Base case for recursion 
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] <= arr[pivot]:
            left += 1
        if arr[right] >= arr[pivot]:
            right -= 1
    arr[pivot], arr[right] = arr[right], arr[pivot]
    qshelper(arr, start, right - 1)
    qshelper(arr, right + 1, end)

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = qs(arr)
print("Sorted array:", sorted_arr)