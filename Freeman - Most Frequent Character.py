# Josh Freeman
# Program 1 : Most Frequent Character
# Write a main program that lets the user enter a string and displays the character that appears most frequently in the string
# Define a function that takes the string as a parameter and returns the character.  Then call the function in Main()

def Main():

    string = input("Enter any number of words: ")

    print("The most frequent character is", mostFrequentCharacter(string))


def mostFrequentCharacter(string):

    strings = {}

    for i in string:

        if i in strings:

            strings[i] += 1
        
        else:
            
            strings[i] = 1

    mostFrequentCharacter = max(strings, key = strings.get)

    return mostFrequentCharacter

Main()
