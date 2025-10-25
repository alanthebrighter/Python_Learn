import math

radius = float(input('What is the radius in cm of the circle?: '))
circumference = 2*math.pi*radius
circumference = round(circumference, 2)
print(f'The Circumference is {circumference}cm')
