# Josh Freeman
# Program 2 : Pig Latin
# Write a main program that accepts a sentence as input and converts each word to "Pig Latin."
# To convert a word to Pig Latin you remove the first letter and place that letter at the end of the word
# Then you append the string "ay" to the word

def Main():

    string = input("Enter a sentence to be converted to Pig Latin: ").lower()

    string = string.split()

    for x in range(len(string)):
            
            string[x] = string[x] [1:] + string[x][0]
            string[x] += 'ay '
        
    string = "".join(string)

    print(string)

Main()