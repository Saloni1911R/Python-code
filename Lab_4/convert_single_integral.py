#f.	Convert a list of multiple integers into a single integer
numbers = [1, 2, 3, 4]
combined = int(''.join(map(str, numbers)))
print("Combined integer:", combined)