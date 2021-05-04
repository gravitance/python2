'''

EX 8 : WIDGETS AND GIZMOS

An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.

'''

widgets = int(input("Enter number of widgets: "))
gizmos = int(input("Enter number of gizmos: "))
weight = (widgets * 75) + (gizmos * 112)

print(f'Total weight of order: {weight} grams')