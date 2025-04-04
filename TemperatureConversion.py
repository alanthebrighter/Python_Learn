print("Weight converter")
# C/F = (32°F − 32) × 5/9 = 0°C
# C/K = 0K − 273.15 = -273.1°C
# F/K = (32°F − 32) × 5/9 + 273.15 = 273.15K
tempTypes=('K','k','C','c','F','f')
tempType = input('What is temperature measurement?("F": Fahrenheit, "C": Celsius, "K": Kelvin). Insert: ')
transformType = input('What is temperature transformation?("F": Fahrenheit, "C": Celsius, "K": Kelvin). Insert: ')
if tempType in tempTypes and transformType in tempTypes and transformType!=tempType:
    # Celsius to Fahrenheit
    if((tempType=='C' or tempType=='c') and (transformType=='F' or transformType=='f')):
        celsius = float(input("Type Celsius temperature: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is iqual to {fahrenheit:.2f}°F.")
    # Fahrenheit to Celsius
    elif (tempType == 'F' or tempType == 'f') and (transformType == 'C' or transformType == 'c'):
        fahrenheit = float(input("Type Fahrenheit temperature: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is iqual to {celsius:.2f}°C.")
    # Celsius to Fahrenheit
    elif tempType == 'c' and transformType == 'f':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F.")

    # Fahrenheit to Celsius
    elif tempType == 'f' and transformType == 'c':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F é igual a {celsius:.2f}°C.")

    # Celsius to Kelvin
    elif tempType == 'c' and transformType == 'k':
        celsius = float(input("Digite a temperatura em Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C é igual a {kelvin:.2f}K.")

    # Kelvin to Celsius
    elif tempType == 'k' and transformType == 'c':
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin}K é igual a {celsius:.2f}°C.")

    # Fahrenheit to Kelvin
    elif tempType == 'f' and transformType == 'k':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print(f"{fahrenheit}°F é igual a {kelvin:.2f}K.")

    # Kelvin to Fahrenheit
    elif tempType == 'k' and transformType == 'f':
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        print(f"{kelvin}K é igual a {fahrenheit:.2f}°F.")
else:
    if tempType not in tempTypes:
        print(f'"{tempType}" is not a valid temperature measurement!!')
    elif transformType not in tempTypes:
        print(f'"{transformType}" is not a valid temperature measurement!!')
    elif tempType == transformType:
        print(f"The temperature measurements can't be equal")
    else:
        print(f'"{tempType}" and ""{transformType}" are not valid temperature measurements!!')
