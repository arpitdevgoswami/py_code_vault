#To check the number is Positive Negative or zero
def positvenegativezero(num):
    if num > 0:
        print("The number is Positive")
    elif num < 0:
        print("The number is Negative")
    else:
        print("The number is Zero")

#____MAIN PROGRAM____
number = float(input("Enter a number: "))
positvenegativezero(number)