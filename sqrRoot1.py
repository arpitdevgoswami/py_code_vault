#Find and calculate square root of a number
def square_root(num):
    if num < 0:
        return "Cannot calculate square root of a negative number."
    elif num == 0:
        return 0
    else:
        guess = num / 2.0
        for i in range(10):
            guess = (guess + num/guess)/2.0
        return guess

#____MAIN PROGRAM____
number = float(input("enter a number to find the square root "))
result = square_root(number)
print(f"The square root of {number} is {result}.")