#Josh Freeman

#Prompt user for the various values of the prism, and store them within the associated variables as a float
l = float(input("Please enter the length of the prism"))
h = float(input("Please enter the height of the prism"))
p = float(input("Please enter the base width of the prism"))
q = float(input("Please enter the top width of the prism"))

#Calculate the volume of the prism with the values the user gave and store within the variable v
v = l * h * ((p + q) / 2)

#Output all measurements and the volume
print("The length given is: ", l)
print("The height given is: ", h)
print("The base width given is: ", p)
print("The top width given is: ", q)
print("The volume calculated is: ", v)

#Reduce all measurements by 25%
newL = l * .75
newH = h * .75
newP = p * .75
newQ = q * .75

#Calculate reduced volume
newV = newL * newH * ((newP + newQ) / 2)

#Output reduced measurements and volume
print("The reduced length is: ", newL)
print("The reduced height is: ", newH)
print("The reduced base width is: ", newP)
print("The reduced top width is: ", newQ)
print("The reduced volume calculated is: ", newV)