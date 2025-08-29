#d. Write a Python program to find the first and last digits of a number.
n = int(input("Enter a number: "))
last = n % 10
first = int(str(n)[0])
print("First digit:", first)
print("Last digit:", last)
