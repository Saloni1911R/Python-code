#c. Write a Python function program to count a number of digits in a number.
def count_digits(num):
    return len(str(abs(num)))
n = int(input("Enter a number: "))
print("Number of digits:", count_digits(n))
