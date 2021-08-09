number = int(input("Enter an integer with five digits: "))
digits = [0,0,0,0,0]

for i in range(5):
    digits[i] = int((number//(10000/(10**i)))%10)

print(digits)

if digits[0] == digits[4] and digits[1] == digits[3]:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

    

    
