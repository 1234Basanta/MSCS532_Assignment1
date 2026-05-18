def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Sort in decreasing order
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Example array
numbers = [12, 5, 8, 19, 1, 25]

print("Original Array:", numbers)

sorted_numbers = insertion_sort_desc(numbers)

print("Sorted Array in Decreasing Order:", sorted_numbers)