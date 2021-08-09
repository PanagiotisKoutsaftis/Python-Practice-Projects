number = int(input("Enter an integer with five digits: "))

for i in range(5):
    int_div = number // (10000/(10**i))
    digit = int_div % 10
    
    print(int(digit))