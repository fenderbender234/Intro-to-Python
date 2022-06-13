#Josh Freeman

#Opening statement for the user
print("This program will add together all the whole numbers between a start and end value")

#Get start/end inputs from user, instantiate sum
start = int(input("Please enter a starting point: "))
end = int(input("Please enter an ending point: "))
sum = 0

#If statement puts lower number first
#For loops take each number within given range and adds to sum, then prints sum for user
#If 2 values are the same, states that case and gives the sum
if start < end :

    for num in range(start, end + 1) :

        sum += num

    print("The sum of all integers between {} and {} is {}".format(start, end, sum))

elif start > end :

    for num in range(end, start + 1) :

        sum += num

    print("The sum of all integers between {} and {} is {}".format(end, start, sum))

else :

    print("The two values were the same, the sum is:", start)
