class Laptop:

    storage_type = "SSD"

    def __init__(self , RAM , storage):
        self.RAM = RAM
        self.storage = storage

    # instance method
    def get_info(self):
        print(f"Laptop RAM is {self.RAM} and storage is {self.storage} {self.storage_type}")

    @classmethod
    def get_storage_type(cls):
        print(f"storage_type = {cls.storage_type}")

    @staticmethod
    def calculate_price(price , dicount):
        total_price = price - (price *dicount/100)
        print(f"Total Price = {total_price}")


l1 = Laptop("16gb" , "512")
l1.get_info()
l1.get_storage_type()
l1.calculate_price(40_000 , 20) #32,000