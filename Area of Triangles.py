#Josh Freeman

#Prompts user for base/height of the 2 triangles and stores them within the following variables
baseOne = float(input("Please enter the base length of triangle one: "))
heightOne = float(input("Please enter the height of triangle one: "))
baseTwo = float(input("Please enter the base length of triangle two: "))
heightTwo = float(input("Please enter the height of triangle two: "))

#Calculate the area of the 2 triangles and store within the following variables
areaOne = (baseOne * heightOne) / 2
areaTwo = (baseTwo * heightTwo) / 2

#Display to the user the triangle with the largest area, or if they are the same
if areaOne == areaTwo :
    print("The area of the two triangles is the same, the area is: ", areaOne)

elif areaOne > areaTwo :
    print("The area of triangle one is greater than triangle two.  The area of triangle one is: ", areaOne)

else :
    print("The area of triangle two is greater than triangle one.  The area of triangle two is: ", areaTwo)