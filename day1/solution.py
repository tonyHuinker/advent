filename = "input.txt"

with open(filename) as f:
    content = f.readlines()

numbers = []
for line in content:
    numbers.append(int(line))

total = len(numbers)
for x in range(0, total):
    for y in range(x+1, total):
        #print("%d + %d = %d" % (numbers[x], numbers[y], numbers[x]+numbers[y]))
        if (numbers[x]+numbers[y] == 2020):
            print("Found it! %d & %d = 2020" % (numbers[x], numbers[y]))