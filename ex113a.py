'''

EX 113 : FORMATTING A LIST (USE RANGE)

When writing out a list of items in English, one normally separates the items with
commas. In addition, the word “and” is normally included before the last item, unless
the list only contains one item. Consider the following four lists:

apples
apples and oranges
apples, oranges and bananas
apples, oranges, bananas and lemons

Write a function that takes a list of strings as its only parameter. Your function
should return a string that contains all of the items in the list formatted in the manner
described previously as its only result. While the examples shown previously only
include lists containing four elements or less, your function should behave correctly
for lists of any length. Include a main program that reads several items from the user,
formats them by calling your function, and then displays the result returned by the
function.

'''

def formatting(itemlist):
    itemstring = ""
    
    if len(itemlist) == 1:
        return str(itemlist[0])

    for i in range(len(itemlist) - 2):
        itemstring += str(itemlist[i]) + ", "
    
    itemstring += str(itemlist[len(itemlist) - 2]) + " and "
    itemstring += str(itemlist[len(itemlist) - 1])

    return itemstring

def main():
    #itemlist = [ "apple", "banana", "grapes", "orange", "watermelon" ]
    #itemlist = [ "apple", "banana", "grapes" ]
    #itemlist = [ "apple", "banana" ]
    #itemlist = [ "apple" ]

    itemlist = []
    item = input("Enter an item to put into list: ")

    if item == "":
        print("List should not be empty.")
    
    else:

        while item != "":
            itemlist.append(item)
            item = input("Enter an item to put into list (blank to stop): ")

        itemstring = formatting(itemlist)

        print(itemstring)

if __name__ == "__main__":
    main()