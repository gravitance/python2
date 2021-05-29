'''

EX 124 : EVALUATE POSTFIX

Evaluating a postfix expression is easier than evaluating an infix expression because it
does not contain any brackets and there are no operator precedence rules to consider.
A postfix expression can be evaluated using the following algorithm:

    Create a new empty list, values

    For each token in the postfix expression

        If the token is a number then
            Convert it to an integer and add it to the end of values

        Else
            Remove an item from the end of values and call it right
            Remove an item from the end of values and call it left
            Apply the operator to left and right
            Append the result to the end of values

    Return the first item in values as the value of the expression

Write a program that reads a mathematical expression in infix form from the user,
evaluates it, and displays its value. Uses your solutions to Exercises 122 and 123
along with the algorithm shown above to solve this problem.

'''

from ex122 import tokenize
from ex123 import to_postfix

def evaluate_postfix(postlist):
    values = []

    for token in postlist:

        if token.lstrip("+-").isdigit():
            values.append(int(token))
        
        else:
            right = values.pop()
            left = values.pop()
            
            if token == "+":
                result = left + right
            
            elif token == "-":
                result = left - right
            
            elif token == "*":
                result = left * right
            
            elif token == "^":
                result = left ** right
            
            else:
                result = left / right
            
            values.append(result)
        
    return values[0]

def main():
    thestring = input("Enter a mathematical expression: ")
    tokenlist = tokenize(thestring)
    postlist = to_postfix(tokenlist)
    evaluated = evaluate_postfix(postlist)
    print(f"evaluated postfix: {evaluated}")

if __name__ == "__main__":
    main()