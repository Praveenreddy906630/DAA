def is_subset_sum(numbers, target_sum, n):
    # Base Cases
    if target_sum == 0:
        return True
    if n == 0:
        return False

    # If the last element is greater than the target sum, ignore it
    if numbers[n-1] > target_sum:
        return is_subset_sum(numbers, target_sum, n-1)

    # Check if the target sum can be obtained by including or excluding the last element
    return (is_subset_sum(numbers, target_sum, n-1) or
            is_subset_sum(numbers, target_sum - numbers[n-1], n-1))

# Example usage
if __name__ == "__main__":
    numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
    target_sum = int(input("Enter the target sum: "))
    
    n = len(numbers)
    if is_subset_sum(numbers, target_sum, n):
        print(f"A subset with the target sum {target_sum} exists.")
    else:
        print(f"No subset with the target sum {target_sum} exists.")
