def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = helper(arr,target,left,right)
    return result

def helper(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        # If the target is greater than the middle element, ignore the left half
        return helper(arr, target, mid + 1, right)
    else:
        # If the target is less than the middle element, ignore the right half
        return helper(arr, target, left, mid - 1)

print("Element found at index:", binary_search([1, 2, 3, 4, 5], 3))