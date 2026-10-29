

class Laptop:
    storage_type = "SSD" #class attribute


    def __init__(self , RAM , storage): #parameterized Constructor
        self.RAM = RAM #instance attribute
        self.storage = storage #instance attribute

    def get_info(self): #instance method
        print(f"Laptop has {self.RAM} RAM and storage {self.storage} {self.storage_type}")

    @classmethod
    def get_storage_type(cls): #class method
        print(f"storage_type = {cls.storage_type}")
        



l1 = Laptop("16gb" , "512gb")
l1.get_info()
l1.get_storage_type()
