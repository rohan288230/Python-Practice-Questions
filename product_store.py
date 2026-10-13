# Product Store 
# Design & create an online store for Products(name,price).
# Track total products being created.
# Create a static method to calculate discount on each product
# based on a % parameter.
class Product:
    count = 0

    def __init__(self, name , price):
        self.name = name
        self.price = price
        Product.count += 1

    @classmethod
    def get_count(cls):
        print(f"Total products is {cls.count}")

    def get_info(self):
        print(f"Price of product {self.name} is Rs.{self.price}")

    @staticmethod
    def cal_discount(price, discount):
        final_price = price - (price * discount/100)
        print(f"The final price is {final_price}")

p1 = Product("Phone", 10_000)
p2 = Product("Laptop", 50_000)
p3 = Product("Headphone", 1_000)
p4 = Product("Speaker", 1_500)
p1.get_info()
Product.get_count()
p1.cal_discount(p1.price,15)