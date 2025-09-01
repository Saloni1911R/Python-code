#e.	Write a Python program to find the length of the last word in a sentence.
def length_of_last_word(sentence):
    words = sentence.strip().split()  
    if not words:
        return 0
    return len(words[-1])
text = input("Enter a sentence: ")
length = length_of_last_word(text)
print("Length of the last word is:", length)
