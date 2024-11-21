def selection_sort(arr):
    """
    Perform selection sort on the given array.

    :param arr: List of elements to sort
    :return: Sorted list
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Assume the minimum is the first element of the unsorted part
        min_index = i
        # Check the rest of the array for a smaller element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
if __name__ == "__main__":
    # Input array
    arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    
    # Perform selection sort
    sorted_arr = selection_sort(arr)
    
    print("Sorted array:", sorted_arr)
