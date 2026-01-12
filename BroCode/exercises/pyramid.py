blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = 0
usedBlocks = 0
while True:
    nextBlocks = height + 1
    if (usedBlocks + nextBlocks) <= blocks:
        height = height + 1
        usedBlocks += nextBlocks
    else:
        break
    
print("The height of the pyramid:", height)


