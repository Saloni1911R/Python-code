#a.	Write a Python program to draw a line with suitable label in the x axis, y axis and a title.
import matplotlib.pyplot as plt 
# data to display on plots 
x = [1, 2, 3] 
y = [3, 2, 4] 
plt.plot(x, y)
plt.title("POST LAB EXERCISE")
# Adding the legends
plt.legend(["Line"])
plt.show()
