# Daniel Lu
# 9/12/20

# This function determines whether the sum of two inputs is greater than, less than, or equal to 10.

x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))
sum1 = (x + y)

if sum1 < 10:
    print (sum1, "is less than 10")
elif sum1 == 10:
    print (sum1, "is equal to 10")
else:
    print (sum1, "is greater than 10")