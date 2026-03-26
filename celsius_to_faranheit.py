#To convert celsius to farenheit and vice versa 
#Celsius to Farenheit
def ctf(cel):
    far = (cel * 9/5) + 32
    return far

#Farenheit to Celsius
def ftc(far):
    cel = (far - 32) * 5/9
    return cel

#____MAIN PROGRAM____
cel = float(input("Enter temperature in Celsius: "))
far = ctf(cel)
print(f"{cel} degrees Celsius is equal to {far} degrees Farenheit.")

far = float(input("Enter temperature in Farenheit: "))
cel = ftc(far)
print(f"{far} degrees Farenheit is equal to {cel} degrees Celsius.")
