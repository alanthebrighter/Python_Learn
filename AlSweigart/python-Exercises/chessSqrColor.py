#!/bin/python3
'''
Write a getChessSquareColor() function that has parameters column and row. The function either returns 'black' or 'white' depending on the color at the specified column and row. Chess boards are 8 x 8 spaces in size, and the columns and rows in this program begin at 0 and end at 7 like in Figure 9-1. If the arguments for column or row are outside the 0 to 7 range, the function returns a blank string.

Note that chess boards always have a white square in the top left corner.
'''

def getChessSquareColor(column, row):
    chesstable = [[None for _ in range(8)] for _ in range(8)]
    for r in range(0, 8):
        #print("creating row", r)
        for c in range(0, 8):
            #print("creating column", r, c)
            if (r+c)%2==0:
                #print(r, c, "white")
                chesstable[r][c] = "white"
            else:
                #print(r, c, "black")
                chesstable[r][c] = "black"
    try: 
        return chesstable[row][column]
    except IndexError:
        return ""
    #print(chesstable)
#print(getChessSquareColor(1, 2))

# Test
assert getChessSquareColor(0, 0) == 'white'
assert getChessSquareColor(1, 0) == 'black'
assert getChessSquareColor(0, 1) == 'black'
assert getChessSquareColor(7, 7) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
