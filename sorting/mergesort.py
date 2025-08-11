def mergesort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    print("Dividing:", arr)
    
    left = arr[:mid]
    print("Left:", left)
    
    right = arr[mid:]
    print("Right:", right)
    
    print("Recursively sorting left and right halves")
    left = mergesort(left)
    right = mergesort(right)
    
    merged = merge(left, right)
    print("Merging:", merged)
    return merged

def merge(left, right):
    merged = []
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            print("Merging left:", merged)
            i += 1
        else:
            merged.append(right[j])
            print("Merging right:", merged)
            j += 1
        k += 1
    
    while i < len(left):
        merged.append(left[i])
        print("Appending remaining left:", merged)
        i += 1
        k += 1
    
    while j < len(right):
        merged.append(right[j])
        print("Appending remaining right:", merged)
        j += 1
        k += 1
    return merged

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = mergesort(arr)
print(f"Sorted array: {sorted_arr}")