
# Python Code to find the sum of squares of numbers in a list

def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of squares
result = sum_of_squares(numbers)
print(f"Sum of squares: {result}")
