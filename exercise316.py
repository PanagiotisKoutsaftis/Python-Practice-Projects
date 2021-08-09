print("Give me 10 numbers")
max1 = 0
max2 = 0
for i in range(10):
   
    number = int(input("Enter a number: "))
    
    if number > max1:
        max1 = number
    elif number > max2:
        max2 = number
        
    
    
            
print("The biggest number is:", max1)
print("The second biggest number is:",max2)
    