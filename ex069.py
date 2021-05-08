'''

EX 69 : APPROXIMATE PI

The value of π can be approximated by the following infinite series:

Write a program that displays 15 approximations of π. The first approximation
should make use of only the first term from the infinite series. Each additional
approximation displayed by your program should include one more term in the series, making
it a better approximation of π than any of the approximations displayed previously.

'''

approximation_term = 3

for i in range(1,16):

    n = i * 2
    term = 4 / (n * (n+1) * (n+2))
    print(f'n = {i}')
    print(f'term = {term}')

    if (i % 2) != 0:
        approximation_term += term
    
    else:
        approximation_term -= term
    
    print (f'approximation {i} of pi = {approximation_term}.')