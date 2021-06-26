'''

EX 89 : CAPITALIZE IT

Many people do not use capital letters correctly, especially when typing on small
devices like smart phones. In this exercise, you will write a function that capitalizes
the appropriate characters in a string. A lowercase “i” should be replaced with an
uppercase “I” if it is both preceded and followed by a space. The first character in
the string should also be capitalized, as well as the first non-space character after a
“.”, “!” or “?”. For example, if the function is provided with the string “what time
do i have to be there? what’s the address?” then it should return the string “What
time do I have to be there? What’s the address?”. Include a main program that reads
a string from the user, capitalizes it using your function, and displays the result.

'''

def capitalize(s):
    punc = [",", ".", "!", "?"]
    s = s.replace(" i ", " I ")

    if len(s) > 0:
        s = s[0].upper() + s[1:]
    
    index = 0

    while index < len(s):
        if s[index] in punc:
            index += 1

            while index < len(s) and s[index] == " ":
                index += 1
            
            if index < len(s):
                s = s[:index] + s[index].upper() + s[index + 1:]
        
        index += 1
    
    return s

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"capitalized string: {capitalize(s)}")