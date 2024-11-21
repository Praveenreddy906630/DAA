def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = sum_of_digits(number)
    print(f"The sum of the digits of {number} is: {result}")
