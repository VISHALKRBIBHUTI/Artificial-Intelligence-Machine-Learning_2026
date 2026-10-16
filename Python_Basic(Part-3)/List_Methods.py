

lst = [1 , 2 , 3]
# 1. lst.append(val)
lst.append(4)
# print(lst)

# 2. lst.insert(idx , val)
lst.insert(1 , 5)
# print(lst)

# 3. lst.sort()
lst1 = [5 , 4 , 2 , 3 , 1 , 6]
lst1.sort()
# print(lst1)
# print(lst1)


# 4. lst.reverse()
lst2 = [1 , 2 , 3 , 4]
lst2.reverse()
# print(lst2)


# 5. lst.sort(reverse = True)
lst3 = [1 , 3 , 2 , 4 , 5]
lst3.sort(reverse= True)
# print(lst3)


# Loops in List
# nums = [1 , 2 ,3]
# for val in nums:
#     print(val , end = " ")

# find value 10 at which index it is present
# LINEAR SEARCH
nums1 = [1 , 2 ,10 , 3 , 5 , 4] 
key = 4
for idx in range(len(nums1)):
    if(nums1[idx] == key):
        print(f"Key {key} Found At Index : {idx}")
        break


