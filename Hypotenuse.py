import math

sideA = float(input('Insert the length of the First side: '))
sideB = float(input('Insert the length of the Second side: '))
hypotenuse = math.sqrt(pow(sideA, 2)+pow(sideB, 2))
print(f'The value of the hypotenuse is {round(hypotenuse, 2)}cm')