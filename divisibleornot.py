#To find numbers divisible by another number
def is_divisible(num, divisor):
    if divisor == 0:
        return False  # Cannot divide by zero
    return num % divisor == 0

# Main program
if __name__ == "__main__":
    try:
        num = int(input("Enter the number: "))
        divisor = int(input("Enter the divisor: "))
        if is_divisible(num, divisor):
            print(f"{num} is divisible by {divisor}")
        else:
            print(f"{num} is not divisible by {divisor}")
    except ValueError:
        print("Please enter valid integers.") 