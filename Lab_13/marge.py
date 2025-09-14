# d. Merge file1.txt and file2.txt into merged.txt
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    data1 = f1.read()
    data2 = f2.read()

with open("merged.txt", "w") as f:
    f.write(data1 + "\n" + data2)

print("Files merged into merged.txt")
