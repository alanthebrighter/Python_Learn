#! /bin/python3

#digitalnumbers = {1:"#\n#\n#\n#\n#", 2:"###\n  #\n###\n#\n###", 3:"###\n  #\n###\n  #\n###", 4:"# #\n# #\n###\n  #\n  #", 5:"###\n#\n###\n  #\n###", 6:"###\n#\n###\n# #\n###", 7:"###\n  #\n  #\n  #\n  #", 8:"###\n# #\n###\n# #\n###", 9:"###\n# #\n###\n  #\n###"}

#digits = {
#    1: " # \n # \n # \n # \n # ",
#    2: "###\n  #\n###\n#  \n###",
#    3: "###\n  #\n###\n  #\n###",
#    4: "# #\n# #\n###\n  #\n  #",
#    5: "###\n#  \n###\n  #\n###",
#    6: "###\n#  \n###\n# #\n###",
#    7: "###\n  #\n  #\n  #\n  #",
#    8: "###\n# #\n###\n# #\n###",
#    9: "###\n# #\n###\n  #\n###",
#    0: "###\n# #\n# #\n# #\n###",
#}

digits = {
    1: [" # ", " # ", " # ", " # ", " # "],
    2: ["###", "  #", "###", "#  ", "###"],
    3: ["###", "  #", "###", "  #", "###"],
    4: ["# #", "# #", "###", "  #", "  #"],
    5: ["###", "#  ", "###", "  #", "###"],
    6: ["###", "#  ", "###", "# #", "###"],
    7: ["###", "  #", "  #", "  #", "  #"],
    8: ["###", "# #", "###", "# #", "###"],
    9: ["###", "# #", "###", "  #", "###"],
    0: ["###", "# #", "# #", "# #", "###"],
}
def display(ns):
    num = str(ns)
    blocks = []

    #blocks = [digits[int(d)] for d in num]

    for d in num:
        digitslist = digits[int(d)]
        blocks.append(digitslist) 

    for i in range(5):
        #line = " ".join(block[i] for block in blocks)

        linestorage = []
        for block in blocks:
            linestorage.append(block[i])
        
        line = " ".join(linestorage)

        print(line)
    
display(9081726354)

