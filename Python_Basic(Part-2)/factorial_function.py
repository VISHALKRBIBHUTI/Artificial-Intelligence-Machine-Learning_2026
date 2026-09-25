
# factorial definition

def factorial(num1):
    fact = 1
    for i in range(1,num1+1):
        fact = fact *i
    return fact


print(f"factorial of 6 is : {factorial(6)}") # 120

