#Program to check the number is odd or even 
def oddeven(num):
    if num % 2 == 0:
        print(f"The {num} is Even ")
    else:
        print(f"The {num} is Odd ")

#____MAIN PROGRAM____
num = int(input("Enter a number: " ))
oddeven(num)