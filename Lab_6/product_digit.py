#f. Write a Python program to calculate the product of digits of a number.
n = int(input("Enter a number: "))
product = 1

for digit in str(abs(n)):
    product *= int(digit)

print("Product of digits:", product)
