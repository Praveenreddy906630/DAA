def bubble_sort(arr):
    """
    Perform bubble sort on the given array.

    :param arr: List of elements to sort
    :return: Sorted list
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
if __name__ == "__main__":
    # Input array
    arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    
    # Perform bubble sort
    sorted_arr = bubble_sort(arr)
    
    print("Sorted array:", sorted_arr)
