#To generate a random number

import random
#____MAIN PROGRAM____
lower_bound = int(input("enter a number for the lower bound:"))
upper_bound = int(input("enter a number for the upper bound "))
random_num = random.randint(lower_bound, upper_bound)
print(f"The random number between {lower_bound} and {upper_bound} is: {random_num}")
