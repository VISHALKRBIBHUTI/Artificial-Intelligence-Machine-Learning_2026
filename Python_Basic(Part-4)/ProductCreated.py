

class Product:
    count = 0

    def __init__(self , name , price):
        self.name = name
        self.price = price
        Product.count += 1

    def product_info(self):
        print(f"Product Name is: {self.name} and Price is : {self.price}")
    


    @staticmethod
    def calculate_dicount(price , dicount):
        print(f"Price of the Product is : {price}")
        discount_price = (price - price*dicount/100)
        print(f"Discount on Product is {discount_price}")


    @classmethod
    def get_total_product(cls):
        print(f"Total Product in Our Store is = {cls.count}")



p1 = Product("laptop" , 40_000)
p2 = Product("Pen" , 10)
p3 = Product("Book" ,100)


Product.get_total_product()
