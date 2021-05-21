'''

EX 106 : REMOVE OUTLIERS

When analysing data collected as part of a science experiment it may be desirable
to remove the most extreme values before performing other calculations. Write a
function that takes a list of values and an non-negative integer, n, as its parameters.
The function should create a new copy of the list with the n largest elements and the
n smallest elements removed. Then it should return the new copy of the list as the
function’s only result. The order of the elements in the returned list does not have to
match the order of the elements in the original list.

Write a main program that demonstrates your function. Your function should read
a list of numbers from the user and remove the two largest and two smallest values
from it. Display the list with the outliers removed, followed by the original list. Your
program should generate an appropriate error message if the user enters less than 4
values.

'''

def removeOutliers(original_list, n):
    newlist = sorted(original_list)
    for i in range(n):
        newlist.pop()
        # print (newlist)
    for i in range(n):
        newlist.pop(0)
        # print (newlist)
    return newlist

original_list = []

element = input("Enter the data for the list: ")

if element == '':
    print("List must have at least 4 values.")

else:
    while element != '':

        original_list.append(float(element))
        element = input("Enter the data for the list (blank to stop): ")
    
    if len(original_list) < 4:
        print("List must have at least 4 values.")

    else:

        newlist = removeOutliers(original_list,2)
        print(f'original data: {original_list}')
        print(f'processed data: {newlist}')