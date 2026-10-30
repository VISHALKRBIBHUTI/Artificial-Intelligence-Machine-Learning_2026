

f = open("sample.txt" , 'r+')
data = f.read()
print(data)

data = data.replace("I " , "I Really ")

f.seek(0)

f.write(data)
f.close()