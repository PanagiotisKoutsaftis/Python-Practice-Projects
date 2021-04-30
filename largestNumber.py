#This python program takes three numbers as an input and then prints the largest number.

counter = 1 # If someone enters three equal numbers I will use the counter variable in an if-statement that will output if the numbers are equal or not
print("Enter x if you wish to exit the program.")
print("Enter three numbers.")
num1 = input("Enter the first number: ")
if num1.lower() == "x":  #Using the lower() function in case someone enters the upper case character X
    exit()
else:
    num1 = float(num1) #I'm using float and not int in case someone enters a floating number and not an integer
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    maximum = num1 #assuming that the first number is the largest
    if maximum < num2 and num2 > num3:
        maximum = num2
    elif maximum < num3 and num3 > num2:
        maximum = num3
    else:
        maximum = num1
    if num1 == num2 and num2 == num3:
        counter = 0
    if counter == 0:
        print("The three numbers are equal to one another")
    else:
        print(f"The largest number is {maximum}")
    input("Press Enter to continue...")


#Probably there is a better solution that is using lists and also applies to larger amount of inputed numbers. I still don't know lots about lists.
#I will solve the problem again when I'll know more about lists and list manipulation.