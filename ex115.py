'''

EX 115 : PIG LATIN

Pig Latin is a language constructed by transforming English words. While the origins of the
language are unknown, it is mentioned in at least two documents from
the nineteenth century, suggesting that it has existed for more than 100 years. The
following rules are used to translate English into Pig Latin:

• If the word begins with a consonant (including y), then all letters at the beginning of
the word, up to the first vowel (excluding y), are removed and then added to the end
of the word, followed by ay. For example, computer becomes omputercay
and think becomes inkthay.

• If the word begins with a vowel (not including y), then way is added to the end
of the word. For example, algorithm becomes algorithmway and office
becomes officeway.

Write a program that reads a line of text from the user. Then your program should
translate the line into Pig Latin and display the result. You may assume that the string
entered by the user only contains lowercase letters and spaces.

'''

firstvowels = ["a", "i", "u", "e", "o", "y"]
vowels = ["a", "i", "u", "e", "o"]


text = input("Enter a line of text: ")

textlist = text.split()
newtextlist = []

for word in textlist:

    if word[0] in vowels:
        new = word + "way"

    else:
        tail = ""
        i = 0
        while i < len(word) and word[i] not in vowels:
            tail += word[i]
            i += 1
        new = word[i:] + tail + "ay"
    
    newtextlist.append(new)

print("translated into pig latin:", end=" ")
for word in newtextlist:
    print(word, end=" ")
print()
