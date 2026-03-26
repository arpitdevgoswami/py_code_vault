#TO display the Fibonacci sequence up to a given number
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a , b = b , a + b
    return sequence

#____MAIN PROGRAM____
num = int(input("Enter a number to display its Fibonacci sequence: "))
fib_seq = fibonacci(num)
print(f"Fibonacci Sequence up to {num}: {fib_seq}")