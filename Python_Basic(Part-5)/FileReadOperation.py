

f = open("sample.txt" , 'r')
# data = f.read()

# print(type(data))

data = f.readline()
print(data)

data = f.readline()
print(data)


f.close()

