'''Calculating the value of pi'''



n = 0
summ = 0
i = 1
steps = int(input("Enter the order of the summ: "))
while i <= steps:
    summ = summ + ((-1)**n)*(1/i)
    
    n = n + 1
    i = i + 2
    
pi = 4 * summ
print("The value of pi after using",steps,"order of the summ is", pi)
    