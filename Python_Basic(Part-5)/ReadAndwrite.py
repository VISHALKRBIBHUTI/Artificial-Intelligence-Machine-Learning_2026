

f = open("sample.txt" , 'r')
data = f.read()
print(data)

f = open("sample.txt" , 'w')
f.write("I Love Learning Python")
f.close()