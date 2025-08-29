#b.	Write a Python program to find the sum of all natural numbers between 1 to n.
n = int(input("Enter a number: "))
total = n * (n + 1) // 2 
print("Sum of natural numbers from 1 to", n, "is:", total)