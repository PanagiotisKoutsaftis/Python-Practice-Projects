print("This program finds if an integer number is even or odd")
number = int(input("Enter an integer number: "))
mod = number % 2
if mod == 0:
    print("The number", number, "is even")
    
if mod != 0:
    print("The number", number, "is odd")