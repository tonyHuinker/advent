filename = "input.txt"

with open(filename) as f:
    content = f.readlines()

valid = 0
for line in content:
    thisline = line.split()
    minmax = thisline[0].split("-")
    minmax[0] = int(minmax[0])
    minmax[1] = int(minmax[1])

    #remove colon
    thisline[1] = thisline[1].replace(":", "")
    if (minmax[0] <= thisline[2].count(thisline[1]) <= minmax[1]):
        print("%s is valid" % (line))
        valid = valid + 1
    else:
        print("%s is NOT valid" % (line))
        #print("%d < %d < %d is NOT TRUE" % (minmax[0], thisline[2].count(thisline[1]),  minmax[1]))
        #print("%s character\n%s" % (thisline[1], thisline[2]))

print(valid)