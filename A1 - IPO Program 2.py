#Josh Freeman

#Prompt user for a temp in fahrenheit, store in variable f as a float
f = float(input("Please enter a temperature in Fahrenheit"))

#Converts user given temperature (f) to Kelvin (k) using the following equation and stores in variable k
k = (f + 459.67) * (5 / 9)

#Displays to the user what their input was, and what the conversion to Kelvin is
print("The Fahrenheit temperature you input was: ", f)
print("After conversion, your temperature value in Kelvin is: ", k)