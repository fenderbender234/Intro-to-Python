#Josh Freeman

num = 0
sum = 0

while num >= 0 :

    num = int(input("Enter a positive number: "))

    if num >= 0 :

        sum += num

    else :

        print("\n")
        print("The sum of positive numbers is: ", sum)
