'''

EX 72 : IS A STRING A PALINDROME?

A string is a palindrome if it is identical forward and backward. For example “anna”,
“civic”, “level” and “hannah” are all examples of palindromic words. Write a program
that reads a string from the user and uses a loop to determines whether or not it is a
palindrome. Display the result, including a meaningful output message.

'''

word = input("Enter a word: ")

is_p = True

for i in range(0, len(word) // 2):
    if word[i] != word[-i-1]:
        is_p = False

if is_p == True:
    print(f'{word} is a palindrome.')
else:
    print(f'{word} is not a palindrome.')