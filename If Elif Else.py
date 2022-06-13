#Josh Freeman

#Prompt user for desired grade
gradeDesired = float(input("Please enter the grade you would like to achieve for the class as a decimal (0.0 - 4.0): "))

#Prompt user for current grade
currentGrade = float(input("Please enter your current grade for the class as a percentage (0.0 - 100.0): "))

#Convert percentage grade to decimal grade
grade = currentGrade / 10 - 5.5

#Display to user current grade as a decimal
print("Your current grade as a decimal is: ", grade)

if gradeDesired >= grade:
    print("Congrats! You are on track to make your target grade")

else:
    print("Oops.  You need to work harder to make your target grade")