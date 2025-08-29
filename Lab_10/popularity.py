#c.	Write a Python programming to display a bar chart of the popularity of programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
import matplotlib.pyplot as plt 
# data to display on plots 
language = ['Java','Python', 'PHP', 'JavaScript', 'C#', 'C++'] 
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7] 


# This will plot a simple bar chart
plt.bar(language, popularity)
# Title to the plot
plt.title("popularity of programming Languages")
# Adding the legends
plt.legend(["bar"])
plt.show()