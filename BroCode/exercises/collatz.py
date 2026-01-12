c = int(input("Number: "))
counter = 0

while c >= 0:
    if c == 1:
        break
    elif c % 2 == 0:
        c = c // 2
        print(c)
        
    else:
        c = 3 * c + 1
        print(c)
    counter += 1

print("step =", counter)
        
    
