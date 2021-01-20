import math
filename = "input.txt"

with open(filename) as f:
    content = f.readlines()

positionX = 0
positionY = 0

slope = (3, 1)
numTrees = 0

while (positionY < len(content)):
    positionX =  positionX % (len(content[0])-1)
    print("line %d out of %d" % (positionY, len(content)))
    if(content[positionY][positionX] == "#"):
        numTrees += 1


    positionX += slope[0]
    positionY += slope[1]

for line in content:
    print(line)
print(numTrees)


