'''

EX 107 : AVOIDING DUPLICATES

In this exercise, you will create a program that reads words from the user until the
user enters a blank line. After the user enters a blank line your program should display
each word entered by the user exactly once. The words should be displayed in the same order
that they were entered. For example, if the user enters:

first
second
first
third
second

then your program should display:

first
second
third

'''

wordlist = []

word = input("Enter a word: ")

if word == '':
    print("First entry cannot be blank.")

else:

    while word != '':

        if word not in wordlist:
            wordlist.append(word)
        
        word = input("Enter a word (blank to stop): ")

print()   
for i in wordlist:
    print(i)