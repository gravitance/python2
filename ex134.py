'''

EX 134 : UNIQUE CHARACTERS

Create a program that determines and displays the number of unique characters in a
string entered by the user. For example, "Hello, World!" has 10 unique characters
while "zzz" has only one unique character. Use a dictionary or set to solve this problem.

'''

s = input("Enter a string: ")
unique = {}

for char in s:
    unique[char] = 1

print(f'the string "{s}" has {len(unique)} unique characters.')