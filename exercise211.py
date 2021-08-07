number = input("Enter an integer with 5 digits: ")
if len(number) == 5:
    number = int(number)
    d1 = number // 10000
    print(d1)
    d2 = (number//1000)%10
    print(d2)
    d3 = (number//100)%10
    print(d3)
    d4 = (number//10)%10
    print(d4)
    d5 = number%10
    print(d5)
    
else:
    print("Wrong number of digits")

