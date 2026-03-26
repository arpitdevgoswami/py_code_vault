#Funtion to find the area if the triangle 
def AOT(b,h):
    formula = 1/2 * b * h
    return formula
     

#____MAIN PROGRAM____
b = float(input("Enter the base of the triangle: "))
h = float(input("Enter the length of the triangle: "))
area = AOT(b,h)
print(f"The area of the triangle is {area}")
