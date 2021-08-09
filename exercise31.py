student_count = 0
passes = 0
fails = 0
wrong_inputs = 0

while student_count != 10:
    result = int(input("Enter result. Pass=1,Fail=2: "))
    if result == 1:
        passes = passes +1
        student_count = student_count +1
    elif result == 2:
        fails = fails +1
        student_count = student_count +1
    else:
        print("You entered a wrong input. Please enter 1 for Pass and 2 for fail")
        wrong_inputs = wrong_inputs + 1

print("Passed:",passes)
print("Failed:",fails)
print("Wrong inputs:",wrong_inputs)

if passes > 8:
    print("Bonus for instructor")