def pascal_triangle(n):
    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)  # Start with a row of 1s
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  # Fill in the values
        triangle.append(row)
    
    return triangle

# Example usage
if __name__ == "__main__":
    rows = int(input("Enter the number of rows for Pascal's Triangle: "))
    triangle = pascal_triangle(rows)
    
    for row in triangle:
        print(' '.join(map(str, row)).center(rows * 2))  # Center the rows for better formatting
