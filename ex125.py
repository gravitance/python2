'''

EX 125 : DOES A LIST CONTAIN A SUBLIST?

A sublist is a list that makes up part of a larger list. A sublist may be a list containing
a single element, multiple elements, or even no elements at all. For example, [1],
[2], [3] and [4] are all sublists of [1, 2, 3, 4]. The list [2, 3] is also a
sublist of [1, 2, 3, 4], but [2, 4] is not a sublist [1, 2, 3, 4] because
the elements 2 and 4 are not adjacent in the longer list. The empty list is a sublist of
any list. As a result, [] is a sublist of [1, 2, 3, 4]. A list is a sublist of itself,
meaning that [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4].

In this exercise you will create a function, isSublist, that determines whether
or not one list is a sublist of another. Your function should take two lists, larger
and smaller, as its only parameters. It should return True if and only if smaller
is a sublist of larger. Write a main program that demonstrates your function.

'''

def isSublist(larger, smaller):

    is_subset = False

    if smaller == []:
        is_subset = True
    
    elif smaller == larger:
        is_subset = True
    
    elif len(smaller) > len(larger):
        is_subset = False
    
    else:
        count = 0
        for i in range(len(larger)):
            if larger[i] == smaller[0]:
                count += 1
                while (count < len(smaller)) and (larger[i+count] == smaller[count]):
                    count += 1
                
                if count == len(smaller):
                    is_subset = True
    
    return is_subset

def main():

    larger = [1, 2, 3, 4]
    smaller = [1, 2]
    print(isSublist(larger, smaller))

if __name__ == "__main__":
    main()