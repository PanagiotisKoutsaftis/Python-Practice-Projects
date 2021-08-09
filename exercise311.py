gallons = int(input("Enter gallons used (-1 to end):"))

miles_sum = 0
gallons_sum = 0

while gallons != -1:
     
    miles = int(input("Enter miles driven: "))
    performance = miles/gallons
    print("The miles/gallons for this tank was:", performance)
    miles_sum = miles_sum + miles
    gallons_sum = gallons_sum + gallons
    gallons = int(input("Enter gallons used (-1 to end): "))
    if gallons == -1:
        break
        
    
if gallons_sum != 0:
    overall_performance = miles_sum / gallons_sum
    print("The overall average miles/gallon was: ", overall_performance)
else:
    print("Goodbye")