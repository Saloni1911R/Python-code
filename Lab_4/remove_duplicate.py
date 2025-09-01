#c.	Write a Python program to remove duplicates from a list.
List = [1,2,2,5,6,4,5,4,7,8,9]
List = list(dict.fromkeys(List))
print(List)
