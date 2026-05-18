import math
n = int(input("Enter number: "))
if 0 <= n <= 9:
    print("Square =", n ** 2)
elif 10 <= n <= 99:
    print("Square root =", math.sqrt(n))
elif 100 <= n <= 999:
    print("Cube root =", n ** (1/3))
else:
    print("Invalid input")