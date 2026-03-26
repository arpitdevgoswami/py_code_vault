#To check the following year is a leap year or not 
def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")

    else:
        print(f"{year} is not a leap year.")

#____MAIN PROGRAM____
year = int(input("Enter a year"))
leapyear(year)