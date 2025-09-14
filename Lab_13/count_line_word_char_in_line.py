# a. Count lines, words, and characters in example.txt
with open("example.txt", "r") as f:
    text = f.read()

lines = text.splitlines()
words = text.split()
chars = len(text)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", chars)
