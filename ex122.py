'''

EX 122 : TOKENIZING A STRING

Tokenizing is the process of converting a string into a list of substrings, known as
tokens. In many circumstances, a list of tokens is far easier to work with than the
original string because the original string may have irregular spacing. In some cases
substantial work is also required to determine where one token ends and the next one
begins.

In a mathematical expression, tokens are items such as operators, numbers and
parentheses. Some tokens, such as *, /, ˆ, ( and ) are easy to identify because the
token is a single character, and the character is never part of another token. The + and
- symbols are a little bit more challenging to handle because they might represent
the addition or subtraction operator, or they might be part of a number token.

Hint: A + or - is an operator if the non-whitespace character immediately
before it is part of a number, or if the non-whitespace character immediately
before it is a close parenthesis. Otherwise it is part of a number.

Write a function that takes a string containing a mathematical expression as its
only parameter and breaks it into a list of tokens. Each token should be a parenthesis,
an operator, or a number with an optional leading + or - (for simplicity we will
only work with integers in this problem). Return the list of tokens as the function’s
result.

You may assume that the string passed to your function always contains a valid
mathematical expression consisting of parentheses, operators and integers. However, your
function must handle variable amounts of whitespace between these
elements. Include a main program that demonstrates your tokenizing function by
reading an expression from the user and printing the list of tokens. Ensure that the
main program will not run when the file containing your solution is imported into
another program.

'''

def tokenize(s):
    s = s.replace(" ", "")
    ops = ["*", "/", "^", "(", ")"]
    tokenlist = []

    i = 0

    while i < len(s):

        if s[i] in ops:
            tokenlist.append(s[i])
            i += 1
        
        elif s[i] == "+" or s[i] == "-":

            if i > 0 and ((s[i-1] >= "0" and s[i-1] <= "9") or s[i-1] == ")"):
                tokenlist.append(s[i])
                i += 1
            
            else:
                number = s[i]
                i += 1

                while i < len(s) and (s[i] >= "0" and s[i] <= "9"):
                    number += s[i]
                    i += 1
                
                tokenlist.append(number)
        
        elif s[i] >= "0" and s[i] <= "9":
            number = ""

            while i < len(s) and (s[i] >= "0" and s[i] <= "9"):
                number += s[i]
                i += 1
            
            tokenlist.append(number)
        
        else:
            return []
        
    return tokenlist

def main():
    thestring = input("Enter a mathematical expression: ")
    tokenlist = tokenize(thestring)
    print(f"the list of tokens: {tokenlist}")

if __name__ == "__main__":
    main()