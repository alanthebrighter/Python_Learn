#! /bin/python3
def isSudoku(data):
    correctLine = '123456789'
    lineTrue = 0
    colTrue = 0
    gridTrue = 0

    ogdata = data.split("\n")
    newdata = [line for line in ogdata if line]
    def lineCheck(newdata):       
        for ix in range(len(newdata)):
            data = newdata
            data = sorted(data[ix])
            lineTrue = 1 if ''.join(data) == correctLine else 0 
            if lineTrue == 0:
                break

        return lineTrue

    def columnCheck(newdata):
        columnData = []
        
        for ix in range(9):
            colLine = []
            for item in newdata:
                colLine.append(item[ix])
            columnData.append(''.join(colLine))
        
        colTrue = lineCheck(columnData)
        return colTrue

    def gridCheck(data):
        gridData = []
        for item in data:
            piece1 = item[0:3]
            piece2 = item[3:6]
            piece3 = item[6:9]

            gridData.append([piece1, piece2, piece3])
        #print(gridData)
        gridResult = []
        for i in range(0, len(gridData), 3):
            block = gridData[i:i+3]
            for ix in range(3):
                aux = block[0][ix], block[1][ix], block[2][ix]
                gridResult.append(''.join(aux))

        gridTrue = lineCheck(gridResult)
        return gridTrue
 
    if (lineCheck(newdata) == 1 and columnCheck(newdata) == 1 and gridCheck(newdata) == 1):
        print("Yes")
    else:
        print("No")

    


        

data1 = """
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
"""
data2 = """
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
"""

isSudoku(data1)
isSudoku(data2)
