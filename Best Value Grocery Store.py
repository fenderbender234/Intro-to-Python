#Josh Freeman

#Prompt user for values and store within variables
smallSize = float(input("Please enter the size of the small item in ounces: "))
smallPrice = float(input("Please enter the price of the small item: "))
largeSize = float(input("Please enter the size of the large item in ounces: "))
largePrice = float(input("Please enter the price of the large item: "))

#Calculate price per ounce for each item
smallCost = smallPrice / smallSize
largeCost = largePrice / largeSize

#Output which unit has the better price
if smallCost == largeCost :
    print("The two prices are the same, ounce for ounce")

elif smallCost > largeCost :
    print("The small item has the better price")

else :
    print("The large item has the better price")