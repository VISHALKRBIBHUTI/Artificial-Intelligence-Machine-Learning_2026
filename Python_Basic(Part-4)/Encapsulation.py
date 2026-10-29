

class BankAccount:

    def __init__(self , name , balance):
        self.name = name
        self.__balance = balance

    def set_balance(self , newBalance):
        self.__balance = newBalance

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("vishal" , 200_000)
print(acc1.name , acc1.get_balance())

print()

acc1.set_balance(300_000)
print(acc1.name , acc1._BankAccount__balance)