
def sortColors(arr):
    first, mid, last = 0, 0, len(arr) - 1

    while mid <= last:
        if arr[mid] == 'B':
            arr[first], arr[mid] = arr[mid], arr[first]
            first += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        else:  
            arr[mid], arr[last] = arr[last], arr[mid]
            last -= 1
    
    return arr


arr = ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
print(sortColors(arr))
