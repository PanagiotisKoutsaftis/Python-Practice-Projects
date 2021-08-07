print("You must enter three floating point numbers")
number1 = float(input("Enter the first float number: "))
number2 = float(input("Enter the second float number: "))
number3 = float(input("Enter the third float number: "))

minimum = min(number1,number2,number3)
maximum = max(number1, number2, number3)

middle = number1

if number2 != maximum and number2 != minimum:
    middle = number2

if number3 != maximum and number3 != minimum:
    middle = number3

print("The inputed numbers in ascending order are:")
print(minimum,"\n",middle,"\n",maximum)