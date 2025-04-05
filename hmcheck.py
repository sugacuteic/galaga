import string
file = "check.txt"
word = {}
l = []
totallines = 0

def readfile():
    global l, totallines
    f = open("check.txt")
    for i in f:
        l.append(i)
        totallines += 1
    print(l)
    print(totallines)

readfile()
    

# def checkfile():
#     global word
#     if "you" in "check.txt":
#         word += 1
#         print("yes")
        
        



