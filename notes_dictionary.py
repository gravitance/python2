# example of a dictionary

phonebook = {"alice": 91234567, "bob": 81112222, "charlie": 95557777, "david": 82239944}
fruits = {"apple": "red", "banana": "yellow", "grape": "purple", "cherry": "red", "mango": "yellow"}

for fruit in fruits:
    if fruits[fruit] == "red":
        print(fruit)

# create an empty dictionary

my_dict = {}
my_dict2 = dict()

# iterating through a dictionary

for i in phonebook:
    print(i) # only prints keys
    print(phonebook[i]) # only prints values


for key, value in phonebook.items():
    print(phonebook[key]) # prints the value of key. returns KeyError if key does not exist.
    print(phonebook.get(key)) # also prints the value of key. returns "None" when key does not exist in dictionary. remaining code runs as per usual.

# adding items into dictionary

new_dict = {}
print(new_dict)

new_dict["mykey"] = 0
print(new_dict)

new_dict["mykey"] = 3 # items in dictionary are unique. only values for identical keys will be updated / replaced
print(new_dict)

new_dict["mykey"] += 1
print(new_dict)