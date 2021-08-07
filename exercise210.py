print("This program takes 3 integers as an input and outputs",
      "the sum, the smaller, the bigger, the multiplication and the",
      "mean value of these numbers")

number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))
number3 = int(input("Enter the third integer: "))

summ = number1 + number2 + number3
print("The sum of these numbers is equal to", summ)

mean = (summ) / 3
print("The mean value of these numbers is equal to", mean)

mul = number1 * number2 * number3
print("The multiplication of these numbers is equal to",mul)

minimum = min(number1,number2,number3)
print("The smaller of these numbers is", minimum)

maximum = max(number1,number2,number3)
print("The maximum of these numbers is", maximum)


