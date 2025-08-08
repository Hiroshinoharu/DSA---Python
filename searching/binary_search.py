def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # If the target is greater than the middle element,
            # ignore the left half
            left = mid + 1
        else:
            # If the target is less than the middle element,
            # ignore the right half
            right = mid - 1
    return -1


print("Element found at index:", binary_search([1, 2, 3, 4, 5], 3))