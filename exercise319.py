for side1 in range(1,20):
    for side2 in range(1,20):
        for hypotenuse in range(1,20):
            x1 = (side1**2)+(side2**2)
            x2 = hypotenuse**2
            if x1 == x2:
                print(f'The numbers {side1},{side2} and {hypotenuse} are a euclidean trio')