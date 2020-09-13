# Daniel Lu
# 9/12/20

# This function determines if the year entered is a leap year.

year = int(input("Please enter a year: "))
      
if (year % 400 == 0):
    print (year, "is a leap year")
elif (year % 100 == 0):
    print (year, "is not a leap year")
elif (year % 4 == 0):
    print (year, "is a leap year")
else:
    print (year, "is not a leap year")