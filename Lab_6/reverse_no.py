#g. Write a Python program to enter a number and print its reverse
n = int(input("Enter a number: "))
reverse = int(str(abs(n))[::-1])

if n < 0:  # handle negative numbers
    reverse = -reverse

print("Reverse of number:", reverse)
