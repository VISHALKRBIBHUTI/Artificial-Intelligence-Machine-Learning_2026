
with open("names.txt", "w+") as f:

    for i in range(5):
        names = input("Enter name: ")
        f.write(names + "\n")

    f.seek(0)  # Move cursor to beginning

    data = f.read()

    print("\nAll names:")
    print(data)