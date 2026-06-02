#Create a Diccioneary
print("Diccionarios")
cities = dict()
#Add values to the dictionary
cities = {1 :"New York", 2 : "Madrid", 3 : "Paris", 4 : "Berlin"}
# Get the value associated with a key
print(cities.get(2)) # Madrid 
print(cities.get(8)) # None
# Iterate over each key and value using items()

print("keys - values")
for key, value in cities.items():
    print("Key: "+ str(key)+ " Value: "+ value)
print("keys")
for values in cities.keys():
    print(values)
print("values")
for key in cities.values():
    print(key)

#We can add new element to the dictionary
cities.setdefault(5, "Rome")
#And we cannot have duplicated keys, but we can have duplicated values
cities.setdefault(6, "Madrid")
print(cities)#{1: 'New York', 2: 'Madrid', 3: 'Paris', 4: 'Berlin', 5: 'Rome', 6: 'Madrid'}

# We can remove an element by its key
cities.pop(1)
print(cities) #{2: 'Madrid', 3: 'Paris', 4: 'Berlin', 5: 'Rome', 6: 'Madrid'}
#or we can delete all the elements
cities.clear()
print(cities) #{}


print("*****************************************")
#Example
# Create a program should ask the user for 5 names of your friends and sort them by friendship.
# These names will be displayed at the end, after they have all been entered.
# If the user enters a repeated name, they must be asked to enter another one, meaning I want 5 unique names with no duplicates.
print("the 5 best friends list")
def get_5_friends():
    names = {}
    while len(names) < 5:
        name = input("Enter a name: ")
        if name in names:
            print("This name is already in the list. Please enter another one.")
        else:
            names[name] = True
    return names.keys()

friends = get_5_friends()
print("Your 5 best friends are: ")
for friend in friends:
    print(friend)
