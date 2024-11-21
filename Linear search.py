def linear_search(arr, target):
    """
    Perform a linear search for the target in the array.

    :param arr: List of elements to search
    :param target: Element to find
    :return: Index of the target if found, otherwise -1
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Return the index of the found element
    return -1  # Return -1 if the target is not found

# Example usage
if __name__ == "__main__":
    # Input array
    arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    target = int(input("Enter the element to search for: "))
    
    # Perform linear search
    result = linear_search(arr, target)
    
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.")
