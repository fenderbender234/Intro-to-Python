#Josh Freeman

weight = float(input("Please enter the weight of your package in pounds: "))

#Based on weight's value, display calculate the given rate, format, and display to the user the cost of shipping
if weight <= 0 :

    print("Please enter a positive integer for your package's weight")

elif weight > 0 and weight <= 2 :
    
    rate = weight * 1.10

    format_rate = "{:.2f}".format(rate)

    print("Your shipping will cost: $", format_rate)

elif weight > 2 and weight <= 6 :

    rate = weight * 2.20

    format_rate = "{:.2f}".format(rate)

    print("Your shipping will cost: $", format_rate)

elif weight > 6 and weight <= 10 :

    rate = weight * 3.70

    format_rate = "{:.2f}".format(rate)

    print("Your shipping will cost: $", format_rate)

else :

    rate = weight * 3.80

    format_rate = "{:.2f}".format(rate)

    print("Your shipping will cost: $", format_rate)
