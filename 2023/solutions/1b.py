input_path = '../inputs/1a.txt'

with open(input_path, 'r') as file:
    aoc_input = file.read()

x = aoc_input.splitlines()

total = 0

y = "one two three four five six seven eight nine".split()

for i in x:
    for r in y:
        i = i.replace(r, r + str(y.index(r) + 1) + r)
    a = ""
    for ii in i:
        if ii.isdigit(): a += ii
    total += int(a[0] + a[-1])
 

print(total) 