#To check the number is armstrong or not 
def armstrong(num):
    sum = 0
    temp = num
    while temp > 0 :
        dight = temp % 10
        sum += dight ** 3
        temp //= 10
    return sum == num

#____MAIN PROGRAM____
number = int(input("Enter a number to check if it is an Armstrong number: "))
if armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")