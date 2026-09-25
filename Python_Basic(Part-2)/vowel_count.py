# Count Number of Vowels in String
str1 = "flowers"
count =0
for var in str1:
    if(var == 'a' or var == 'e' or var == 'i' or var == 'o' or var =='u'):
        count +=1
print(f"{count} Vowels appear in in Given String")
