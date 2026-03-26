#To find the armstrong number ina given interval
def armstrong_interval(start, end):
    armstrongnumbers = []
    for num in range(start, end + 1):
        sum = 0
        temp = num 
       
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
        
        if sum == num:
            armstrongnumbers.append(num)
    return armstrongnumbers

#____MAIN PROGRAM____
start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))
armstrong_numbers = armstrong_interval(start, end)
print(f"Armstrong numbers in the interval [{start}, {end}]: {armstrong_numbers}")