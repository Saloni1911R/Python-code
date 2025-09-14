# b. Read file line by line into a list
lines_list = []
with open("example.txt", "r") as f:
    for line in f:
        lines_list.append(line.strip())

print(lines_list)
