'''

EX 128 : REVERSE LOOKUP

Write a function named reverseLookup that finds all of the keys in a dictionary
that map to a specific value. The function will take the dictionary and the value to
search for as its only parameters. It will return a (possibly empty) list of keys from
the dictionary that map to the provided value.

Include a main program that demonstrates the reverseLookup function as part
of your solution to this exercise. Your program should create a dictionary and then
show that the reverseLookup function works correctly when it returns multiple
keys, a single key, and no keys. Ensure that your main program only runs when
the file containing your solution to this exercise has not been imported into another
program.

'''

def reverse(dict, value):
    keys = []

    for key in dict:
        if dict[key] == value:
            keys.append(key)

    return keys

def main():
    fruits = {"apple": "red", "banana": "yellow", "grape": "purple", "tomato": "red"}
    print(f'red fruits: {reverse(fruits, "red")}')
    print(f'purple fruits: {reverse(fruits, "purple")}')
    print(f'blue fruits: {reverse(fruits, "blue")}')

if __name__ == "__main__":
    main()