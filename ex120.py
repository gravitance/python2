'''

EX 120 : IS A LIST ALREADY IN SORTED ORDER?

Write a function that determines whether or not a list of values is in sorted order
(either ascending or descending). The function should return True if the list is
already sorted. Otherwise it should return False. Write a main program that reads
a list of numbers from the user and then uses your function to report whether or not
the list is sorted.

Make sure you consider these questions when completing this exercise: Is a
list that is empty in sorted order? What about a list containing one element?

'''

def is_sorted(l):

    if len(l) < 2:
        return True
    
    elif l == sorted(l):
        return True
    
    elif l == sorted(l, reverse=True):
        return True
    
    else:
        return False

def main():

    x = input("Enter a list of numbers (separate with comma): ")
    x = x.replace(" ", "").split(",")

    if is_sorted(x) == True:
        print("the list is sorted.")
    else:
        print("the list is not sorted.")

if __name__ == "__main__":
    main()
