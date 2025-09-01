#d.	Write a Python program to get the frequency of elements in a list.
from collections import Counter

items = ['a', 'b', 'a', 'c', 'b', 'a']
frequency = Counter(items)

print("Frequency of elements:", dict(frequency))
