

salary = float(input("Enter Your salary To Know How Much Tax You Have To Pay : "))
tax_amnt = None

# if salary less than 30,000 -> 5%
# if salary is between 30,000 - 70,000 -> 15%
# if salary greater than 70,000 -> 25%

if(salary < 30_000):
    tax_amnt = salary * 0.05
  
elif(salary<= 70_000):
    tax_amnt = salary *0.15
  
else:
    tax_amnt = salary *0.25
  

print(f"Final Tax Amount You Have To Pay is: {tax_amnt}")



