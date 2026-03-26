#fuction for swapping the variable 
def swap_variable(a,b):
    a,b = b,a
    return a,b

#____MAIN PROGRAM____
x = input("Enter the value of x ")
y = input ("Enter the value of y ")
print(f"Before swapping: x = {x}, y = {y}")
x,y = swap_variable(x,y)
print(f"After swapping: x = {x}, y = {y}")