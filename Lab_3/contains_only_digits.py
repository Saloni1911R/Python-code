#c.	Write a Python program to check if a string contains only digits.
def contains_only_digits(s):
    return s.isdigit()
text = input("Enter a string: ")
if contains_only_digits(text):
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")