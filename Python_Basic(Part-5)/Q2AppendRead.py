

with open("log.txt" , "a+") as f:
    f.write("Hi Python People\n")
    f.write("Program Run Successfully\n")
    f.write("Python Program End")

    f.seek(0) # move cursor to the beginning
    data = f.read()
    print(data)