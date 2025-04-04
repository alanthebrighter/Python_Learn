print("Weight converter")
approximatePounds = 2.205
unit = input("Which unit? ('K' for kilograms, 'P' for pounds/libras), Insert: ")
if unit in ('K','P','k','p'):
    weight = float(input('Insert the weight: '))
    if unit == 'K' or unit == 'k':
        result = weight*approximatePounds
        transform = "pounds"
    elif unit == 'P' or unit == 'p':
        result = weight/approximatePounds
        transform = "kgs"

    print(f'Result: {round(result, 2)} {transform}, approximately.')
else:
    print(f"'{unit}' is not a valid Unit!!")