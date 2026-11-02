import json

population = {
    "Delhi": 11034555,
    "Mumbai": 12442373,
    "Bengaluru": 8443675
}

# Step 1: Save initial data
with open("cities.json" , "w") as f:
    json.dump(population , f , indent=4)


# Step 2: Read existing data
with open("cities.json", "r") as f:
    data = json.load(f)
    print("Existing Data:", data)


# Step 3: Take new data from user
asking_user = True
new_dict = {}


while asking_user:

    asking_user = input("Want to Enter New Data Y/N: ").upper()

    if asking_user == "Y":

        cities_name = input("Enter City Name: ")

        population_of_cities = int(input("Enter Population: "))

        new_dict[cities_name] = population_of_cities

    elif asking_user == "N":
        asking_user = False

    else:
        print("Invalid choice! Enter Y or N.")



# Step 4: Combine old and new dictionaries
population.update(new_dict)


# Step 5: Save updated dictionary
with open("cities.json", "w") as f:
    json.dump(population, f, indent=4)



# Step 6: Read updated data
with open("cities.json", "r") as f:
    data = json.load(f)
    print("Updated Data:", data)
