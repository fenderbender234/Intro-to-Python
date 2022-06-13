#Josh Freeman

years = int(input("Enter the number of years: "))

rainTotal = 0
monthCount = 1
yearCount = 1

while years <= 0 :
    
    years = int(input("Invalid: Enter a positive number: "))


for yearLoop in range(0, years) :

    print("*********************************")



    for months in range(0, 12) :
        
        rainfall = float(input("Enter the rainfall for year " + str(yearCount) + " month " + str(monthCount) + ": "))

        rainTotal += rainfall

        monthCount += 1


    print("*********************************")

    yearCount += 1


totalMonths = years * 12
rainAverage = rainTotal / totalMonths
rainAverageFormat = round(rainAverage, 2)

print("Number of months: " + str(totalMonths) + " , Total rainfall in inches: " + str(rainTotal) + " , Average rainfall: " + str(rainAverageFormat))
