#! /bin/python3
def isSudoku(data):
    correctLine = '123456789'

    ogdata = data.split("\n")
    newdata = [line for line in ogdata if line]
    #print(newdata)

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
