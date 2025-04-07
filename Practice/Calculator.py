print('Calculator of Two Numbers.')
operator = input('+ for Addition, - for Subtraction, * for Multiplication, / for Division. Insert: ')
if operator in ('+','-','*','/'):
    n1 = float(input('Insert the 1st Number: '))
    n2 = float(input('Insert the 2nd Number: '))
    if operator == '+':
        result = n1+n2
    elif operator == '-':
        result = n1-n2
    elif operator == '*':
        result = n1*n2
    elif operator == '/':
        result = n1/n2

    print(f'Result: {round(result, 3)}')
else:
    print(f'"{operator}" is not a valid operator!!')

