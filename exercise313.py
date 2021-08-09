number = int(input("Give me a non negative integer number: "))
factorial = 1
if number >= 0:
    for i in range(number):
        factorial = factorial*(number - i)
    print("The factorial of number", number, "is", factorial)
else:
    print("I said a non negative number you sussy baka!")
    


