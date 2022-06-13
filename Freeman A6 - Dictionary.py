# Josh Freeman
# Create a dictionary weeklyTemps and initialize it with data, where the keys are the days of the week and the values are set to 0
# Request the temperature values for each day of the week Monday through Sunday and add the values to the dictionary defined above
# Must use a for loop

from statistics import mean

def Main():

    weeklyTemps = {'Monday' : 0, 'Tuesday' : 0, 'Wednesday' : 0, 'Thursday' : 0, 'Friday' : 0, 'Saturday' : 0, 'Sunday' : 0}

    for day in weeklyTemps:

        weeklyTemps[day] = int(input("Enter the temperature for " + day + ": "))


    days = list(weeklyTemps.keys())

    minTemp = min(weeklyTemps.values())
    maxTemp = max(weeklyTemps.values())
    average = sum(weeklyTemps.values()) / 7

    minIndex = list(weeklyTemps.values()).index(minTemp)
    day = days[minIndex]
    print(day + " was the coldest day with a temperature value of", minTemp)

    maxIndex = list(weeklyTemps.values()).index(maxTemp)
    day = days[maxIndex]
    print(day, " was the warmest day with a temperature value of", maxTemp)

    print("The average temperature was", round(average, 2))

    for day in weeklyTemps:

        if weeklyTemps.get(day) > average:

            print(day, "had a temperature that was higher than the weekly average")

Main()
