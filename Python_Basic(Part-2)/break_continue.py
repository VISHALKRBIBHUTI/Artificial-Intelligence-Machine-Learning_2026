# break

print("Break illustration")
i = 1
while(i<=10):
    if(i%5 == 0):
        break
    print(i)
    i+=1


# continue
print("Continue illustration")
j = 1
while(j <= 10):
    if(j%3 == 0):
        j+=1
        continue
    print(j)
    j+=1 

# printing Odd Number using Continue Keyword
print("Printing Odd Number Using Continue Keyword")
k = 1
while(k <=10):
    if(k%2 == 0):
        k += 1
        continue
    print(k)
    k += 1
