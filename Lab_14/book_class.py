class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")
        print("\n")

    def apply_discount(self, percent):
        discount_amount = (percent / 100) * self.price
        self.price -= discount_amount


# Example usage
b1 = Book("The Alchemist", "Paulo Coelho", 500)
b2 = Book("Python Crash Course", "Eric Matthes", 800)

print("Book Details Before Discount:")
b1.display()
b2.display()

# Apply discount
b1.apply_discount(10)   # 10% discount
b2.apply_discount(20)   # 20% discount

print("Book Details After Discount:")
b1.display()
b2.display()
