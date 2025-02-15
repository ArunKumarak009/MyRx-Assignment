def sortedSquares(arr):
    n = len(arr)
    result = [0] * n  # Output array
    print(result)
    left, right = 0, n - 1
    index = n - 1  # Start filling from the last position

    while left <= right:
        left_val, right_val = abs(arr[left]), abs(arr[right])

        if left_val > right_val:
            result[index] = left_val ** 2
            left += 1
        else:
            result[index] = right_val ** 2
            right -= 1
        
        index -= 1  # Move backwards in result array

    return result

# Example Usage:
arr = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
print(sortedSquares(arr))
