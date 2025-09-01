#d.	Write a Python program to find the longest word in a sentence.

def find_longest_word(sentence):
    words = sentence.split()  # Split sentence into words
    longest = max(words, key=len)  # Find the word with the maximum length
    return longest
text = input("Enter a sentence: ")

longest_word = find_longest_word(text)
print("The longest word is:", longest_word)
