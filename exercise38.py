summ = 0
mul = 1

for i in range(4):
    number = int(input("Enter an integer number: "))
    summ = summ + number
    mul = mul * number
    if i == 0:
        maxi = number
        mini = number
    if number > maxi:
        maxi = number
    if number < mini:
        mini = number
    

mean = summ / 4

print("Sum =", summ)
print("Mul =", mul)
print("Mean =", mean)
print("Min =", mini)
print("Max =", maxi)