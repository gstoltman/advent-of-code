input_path = '../inputs/1a.txt'

with open(input_path, 'r') as file:
    aoc_input = file.read()

def convert_to_list(data):
    input_list = []
    lines = data.strip().split('\n')
    input_list = [value for value in lines]
    return input_list

aoc_list = convert_to_list(aoc_input)

total = 0

for item in aoc_list:
    for i in item:
        if i.isdigit():
            first = i
            break
    for j in reversed(item):
        if j.isdigit():
            last = j
            break
    line_sum = int(first + last)
    total += line_sum
    print(total)