def linear_search(arr,target):
    """
    Perform a linear search on the given array.

    Args:
        arr (list): The array to search through.
        target (int): The element to search for.
    """
    
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Element {target} found at index {arr[i]}")
            return arr[i]
    
    print(f"Element {target} not found in the array.")
    return -1

linear_search([5,1,4,7,9,8,6,56,3,2], 6)