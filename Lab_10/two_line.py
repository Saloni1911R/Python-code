#b.	Write a Python program to plot two or more lines on same plot with suitable legends of each line.
import matplotlib.pyplot as plt 
# data to display on plots 
x = [10, 20, 30] 
y = [3, 2, 4] 
plt.plot(x, y)
plt.title("POST LAB EXERCISE")
# Adding the legends
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["Line"])
plt.show()