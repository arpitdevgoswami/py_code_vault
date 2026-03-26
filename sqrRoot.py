#Find and calculate square root of a number
def square_root(num):
    if num < 0:
        return "Cannot calculate square root of a negative number."
    elif num == 0:
        return 0
    else:
       sqrt = num ** 0.5
       print(f"Square root of {num} is {sqrt}")

#____MAIN PROGRAM____
number = float(input("enter a number to find the square root "))
result = square_root(number)

    
