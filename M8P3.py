# Daniel Lu
# 9/12/20

# This function determines whether a list contains the value 5.

list1 = (int(x) for x in input("Enter a list of numbers, separated by spaces: ").split())

if 5 in list1:
    print ("The number 5 is in that list.")
else:
    print ("The number 5 is not in that list.")