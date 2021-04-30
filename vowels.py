# This is a python program that removes the vowels from a given string.

print("Enter x for exit.")
string = input("Enter a string: ")
if string.lower() == "x": #Using the lower() function just in case someone use upper case character X
    exit()
else:
    print("Removing vowels...")
    newString = string #copying the string so the changes dont affect the for-loop
    vowels = ["a" , "e" , "i" , "o" , "u" , "A" , "E" , "I" , "O" , "U"]  #defining a list with all the vowels, upper and lower case
    for c in string:  #looping through all characters of the given string
        if c in vowels:
            newString = newString.replace(c,"") #the replace() function changes the c character with blank if c is in the vowels list
    print(f"The new string is {newString}")
    input("Press Enter to finish the program... ")


# I know I'm using a lot of comments, but it's something I must really learn as well.

