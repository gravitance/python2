'''

EX 116 : PIG LATIN IMPROVED

Extend your solution to Exercise 115 so that it correctly handles uppercase letters and
punctuation marks such as commas, periods, question marks and exclamation marks.
If an English word begins with an uppercase letter then its Pig Latin representation
should also begin with an uppercase letter and the uppercase letter moved to the end of
the word should be changed to lowercase. For example, Computer should become
Omputercay. If a word ends in a punctuation mark then the punctuation mark
should remain at the end of the word after the transformation has been performed.
For example, Science! should become Iencescay!.

'''

firstvowels = ["a", "i", "u", "e", "o", "y"]
vowels = ["a", "i", "u", "e", "o"]
punc = [",", ".", "?", "!"]


text = input("Enter a line of text: ")

textlist = text.split()
newtextlist = []

for word in textlist:

    p = ""

    if word[-1] in punc:
        p = word[-1]
        word = word.replace(word[-1], "")

    if word[0].lower() in vowels:
        new = word + "way" + p

    else:
        tail = ""
        i = 0
        while i < len(word) and word[i] not in vowels:
            tail += word[i]
            i += 1
        new = word[i:] + tail + "ay" + p
    
    if word[0].isupper():
        new = new.lower().replace(new[0], new[0].upper())
    
    newtextlist.append(new)

print("translated into pig latin:", end=" ")
for word in newtextlist:
    print(word, end=" ")
print()
