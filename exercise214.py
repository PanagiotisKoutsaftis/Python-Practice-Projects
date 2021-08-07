age = int(input("Enter your age: "))
maximumHR = 220 - age
print("The maximum heart rate according to your age is", maximumHR)
goalHR1 = 0.5*maximumHR
goalHR2 = 0.85*maximumHR
print("You should aim for a Heart rate somewhere between", goalHR1, "and",
      goalHR2)

