'''

EX 73 : MULTIPLE WORD PALINDROMES

There are numerous phrases that are palindromes when spacing is ignored. Examples
include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
among many others. Extend your solution to Exercise 72 so that it ignores spacing
while determining whether or not a string is a palindrome. For an additional challenge,
extend your solution so that is also ignores punctuation marks and treats uppercase
and lowercase letters as equivalent.

'''

phrase = input("Enter a word: ")
phrase2 = phrase.replace(" ", "").lower()

is_p = True

for i in range(0, len(phrase2) // 2):
    if phrase2[i] != phrase2[-i-1]:
        is_p = False

if is_p == True:
    print(f'"{phrase}" is a palindrome.')
else:
    print(f'"{phrase}" is not a palindrome.')