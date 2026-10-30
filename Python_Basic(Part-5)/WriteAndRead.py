

f = open("sample.txt" , 'w+')

f.write("Learning Python is Fun")

f.seek(0) # Move Cursor to Position 0(beginning)

data = f.read()

print(data)

f.close()