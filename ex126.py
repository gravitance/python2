'''

EX 126 : GENERATE ALL SUBLISTS OF A LIST

Using the definition of a sublist from Exercise 125, write a function that returns a list
containing every possible sublist of a list. For example, the sublists of [1, 2, 3]
are [], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3]. Note that your function will always
return a list containing at least the empty list because the empty list
is a sublist of every list. Include a main program that demonstrate your function by
displaying all of the sublists of several different lists.

'''

def generate_sublists(mainlist):
    masterlist = [[]]

    for i in range(len(mainlist)+1):
        for k in range(i):
            sublist = mainlist[k:i]
            masterlist.append(sublist)
    
    return sorted(masterlist)


def main():

    mainlists = [[4,5,6], [2,3,4], [1,4,5,7], [1, 2, 3, 4, 5], [5,3,2]]

    for mainlist in mainlists:
        print(f"main list: {mainlist}")
        print(f"all sublists of the above are: {generate_sublists(mainlist)}.")
        print()

if __name__ == "__main__":
    main()