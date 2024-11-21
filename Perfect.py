def is_perfect_number(num):
    if num < 1:
        return False  # Perfect numbers are positive integers

    # Calculate the sum of proper divisors
    sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
    
    return sum_of_divisors == num  # Check if the sum equals the original number

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")
