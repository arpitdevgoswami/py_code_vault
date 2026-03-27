#To find the sum of the natural numbers 
def sumofnaturalnum(n):
    sum = 0
    for i in range (1, n+1):
        sum += i
    return sum

#___MAIN PROGRAM____
n = int(input("Enter a number: "))
print("The sum of natural numbers up to", n, "is:", sumofnaturalnum(n))