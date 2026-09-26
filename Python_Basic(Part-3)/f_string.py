

num1 = 4
num2 = 5
sum = num1 + num2

# normal formatting
print("The sum of {} and {} is {}".format(num1 , num2 , sum))


# index based formatting
print("Index Based Formatting")
print("The sum of {1} and {0} is : {2}".format(num1 , num2 , sum))


# value based formatting
print("value based formatting")
print("values of var is {num1} and {num2}".format(num1 = 2 , num2 = 3))


print()

print("f-string")
a = 6
b = 10
print(f"the sum of {a} and {b} is: {a + b}")

