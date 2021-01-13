filename = "input.txt"

with open(filename) as f:
    content = f.readlines()

valid = 0
for line in content:
    thisline = line.split()
    positions = thisline[0].split("-")
    positions[0] = int(positions[0])
    positions[1] = int(positions[1])

    #remove colon
    thisline[1] = thisline[1].replace(":", "")
    if (bool(thisline[2][positions[0]-1] == thisline[1]) ^ bool(thisline[2][positions[1]-1] == thisline[1])):
        print("%s is valid" % (line))
        valid = valid + 1
    else:
        print("%s is NOT valid" % (line))
        #print("%d < %d < %d is NOT TRUE" % (positions[0], thisline[2].count(thisline[1]),  positions[1]))
        #print("%s character\n%s" % (thisline[1], thisline[2]))

print(valid)