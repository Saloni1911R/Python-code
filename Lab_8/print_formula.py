#	Make a simplest possible Python program that calculates and prints the value of the formula
#   y=6x^2+4sin(x)
import math

x = float(input("Enter value of x: "))
y = 6 * (x ** 2) + 4 * math.sin(x)
print("y =", y)
