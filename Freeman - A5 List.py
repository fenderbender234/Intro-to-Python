# Josh Freeman
# A5 - List

from matplotlib import pyplot as plt
from statistics import mean

def Main():
    
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    temp = []

    for n in range(len(day)):

        x = int(input("Enter the temperature for " + day[n] + ": "))

        temp.append(x)

    # Variables to hold the minimum / maximum values of temps given by user
    minTemp = min(temp)
    maxTemp = max(temp)

    # Variables to hold (and later find) the index position of the day with the lowest and highest temps
    minDay = (temp.index(minTemp))
    maxDay = (temp.index(maxTemp))
    average = Average(temp)

    print(day[minDay] + " was the coldest day with a temperature value of " + minTemp)
    print(day[maxDay] + " was the warmest day with a temperature value of " + maxTemp)
    print("The average temperature this week is: ", round(average, 2))

    plt.plot(day, temp)
    plt.title('Weekly Temperature Data')
    plt.xlabel('Days of the Week')
    plt.ylabel('Temperature Values')
    plt.show()


def Average(temp):

    return mean(temp)


Main()