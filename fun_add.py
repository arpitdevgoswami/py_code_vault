# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Get user input
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Call the function and display the result
result = add(number1, number2)
print("The sum of", number1, "and", number2, "is", result)