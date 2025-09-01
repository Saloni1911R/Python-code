#b.	Write a Python program to check if a string is a palindrome.
def is_palindrome(string):
    cleaned = string.replace(" ", "").lower()
    if cleaned == cleaned[::-1]:
        return True
    else:
        return False
text = input("Enter a string: ")
if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

