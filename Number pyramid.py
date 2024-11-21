def number_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces for alignment
        print(' ' * (n - i), end=' ')
        
        # Print numbers in increasing order
        for j in range(1, i + 1):
            print(j, end=' ')
        
        # Move to the next line after each row
        print()

# Example usage
if __name__ == "__main__":
    rows = int(input("Enter the number of rows for the pyramid: "))
    number_pyramid(rows)
