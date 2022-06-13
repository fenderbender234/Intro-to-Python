# Josh Freeman
# 5/20/2022
# A4 Functions
# Designing and Implementing functions
# Takes Fahrenheit temperature as a parameter and converts the value into Reaumur

def FR_converter(Tf):

    Tr = (Tf -32) * (4/9)

    return Tr

def main():

    Tf = float(input("Enter a temperature in Fahrenheit: "))
    print("The value you have input is: ", Tf)
    print(FR_converter(Tf))

main()
