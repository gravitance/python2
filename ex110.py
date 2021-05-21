'''

EX 110 : PERFECT NUMBERS

An integer, n, is said to be perfect when the sum of all of the proper divisors of n is
equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.

Write a function that determines whether or not a positive integer is perfect. Your
function will take one parameter. If that parameter is a perfect number then your function will return true.
Otherwise it will return false. In addition, write a main program
that uses your function to identify and display all of the perfect numbers between 1
and 10,000. Import your solution to Exercise 109 when completing this task.

'''

from ex109 import proper_divisor

def is_perfect(n):
    divisor_list = proper_divisor(n)
    total = sum(divisor_list)
    
    if total == n:
        return True
    else:
        return False

def main():
    maximum = 10000
    perfect = []

    for p in range(1, maximum+1):
        if is_perfect(p) == True:
            perfect.append(p)

    print(f'All perfect numbers between 1 and {maximum} are: {perfect}.')

if __name__ == "__main__":
    main()