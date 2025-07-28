# File: operations.py
# This file contains functions to perform operations on arrays.

def access_element(arr, index):
    """
    Accesses an element in the array at the specified index.

    Args:
        arr (list): Sample array to access.
        index (int): Index of the element to access.
    """
    
    if index < 0 and index >= len(arr):
        raise IndexError("Index out of bounds")
    return arr[index]

def update_element(arr, index, value):
    """
    _summary_

    Args:
        arr (list): Sample array to update.
        index (int): Index of the element to update.
        value (int): New value to set.
    """
    
    if index < 0 and index <= len(arr):
        raise IndexError("Index out of bounds")
    
    arr[index] = value
    return arr

def traverse_array(arr):
    """
    Traverses the array and returns a list of elements.

    Args:
        arr (list): Sample array to traverse.
    """
    
    return [element for element in arr]

def copy_array(arr):
    """
    Copies the array and returns a new array.

    Args:
        arr (list): Sample array to copy.
    """
    
    return arr.copy()

def insert_element(arr, index, value):
    """
    Inserts an element at the specified index in the array.

    Args:
        arr (list): Sample array to insert into.
        index (int): Index at which to insert the new element.
        value (int): Value to insert.
    """
    
    if index < 0 or index > len(arr):
        raise IndexError("Index out of bounds")
    
    arr.insert(index, value)
    return arr

def delete_element(arr, index):
    """
    Deletes an element at the specified index in the array.
    Args:
        arr (list): Sample array to delete from.
        index (int): Index of the element to delete.
    """
    
    if index < 0 or index >= len(arr):
        raise IndexError("Index out of bounds")
    
    del arr[index]
    return arr

arr = [1,2,3,4,5]

print("Accessing element at index 2:", access_element(arr, 2))  # Output: 3

print("Updating element at index 2:", update_element(arr, 2, 10))  # Output: [1, 2, 10, 4, 5]

print("Accessing element at index 2 again:", access_element(arr, 2))  # Output: 10

print("Traversing the array:", traverse_array(arr))  # Output: [1, 2, 10, 4, 5]

print("Copying the array:", copy_array(arr))  # Output: [1, 2, 10, 4, 5]

insert_element(arr, 2, 20)
print("Array after inserting element at index 2:", arr)  # Output: [1, 2, 20, 10, 4, 5]

delete_element(arr, 2)
print("Array after deleting element at index 2:", arr)  # Output: [1, 2, 10, 4, 5]