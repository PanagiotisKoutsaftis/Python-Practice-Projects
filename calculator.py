#We are going to create a simple calculator
import math as mth

print("1 = addition")
print("2 = subtraction")
print("3 = Multiplication")
print("4 = division")
print("5 = Square root")
print("6 = power")
print("7 = exit program")

def addition(number1, number2):
    result = number1 + number2
    print(f"The result is equal to {result}")

def subtraction(number1, number2):
    result = number1 - number2
    print(f"The result is equal to {result}")

def multiplication(number1 , number2):
    result = number1 * number2
    print(f"The result is equal to {result}")

def division(number1 , number2):
    result = number1 / number2
    print(f"The result is equal to {result}")


while True:
    choice = int(input("Enter your choice: "))
    if choice >= 1 and choice <= 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == 1:
            addition(num1 , num2)
        elif choice == 2:
            subtraction(num1 , num2)
        elif choice == 3:
            multiplication(num1 , num2)
        elif choice == 4:
            division(num1 , num2)
    elif choice == 5:
        num = float(input("Enter the number:"))
        square = mth.sqrt(num)
        print(f"The square root is equal to {square}")
    elif choice == 6:
        num = float(input("Enter the number: "))
        power = float(input("Enter the power: "))
        result = num ** power
        print(f"The result is {result}")
    elif choice == 7:
        break
    else:
        print("You enter a non valid choice.Please enter your choice again.")

