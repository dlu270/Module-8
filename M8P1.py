# Daniel Lu
# 9/12/20

# This functions determines whether two inputs are equal.

x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))

if ((x ^ y) !=0):
    print ("These numbers are not equal")
else:
    print ("These numbers are equal")