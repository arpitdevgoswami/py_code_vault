#To display the multiplication table of a number
def multiplication_table(n):
    table = []
    for i in range(1, 11):
        table.append(f"{n} x {i} = {n * i}")
    return table

#____MAIN PROGRAM____
num = int(input("Enter a number to display its multiplication table: "))
table = multiplication_table(num)
print(f"Multiplication Table of {num}:")

for line in table:
    print(line)