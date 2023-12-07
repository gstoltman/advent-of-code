input_path = '../inputs/2a.txt'

with open(input_path, 'r') as file:
    aoc_input = file.read()

limit_dict = {'red': 12, 'green': 13, 'blue': 14}

game_dict = {}

games = aoc_input.splitlines()

total = 0

for game in games:
    game_set = game.split(':')
    game_number = int(game_set[0].replace('Game ', ''))
    color_sets = game_set[1].split(';')
    
    color_list = []

    for color_set in color_sets:
        color_dict = {}
        
        colors = color_set.split(',')
        for color in colors:
            parts = color.strip().split(' ')
            count = int(parts[0])
            color_name = parts[1]
            color_dict[color_name] = count
        color_list.append(color_dict)
    
    game_dict[game_number] = color_list

for game, color_sets in game_dict.items():
#    for reveal in color_sets:
#        for color, amount in reveal.items():         
#            if amount > reveal[color]:
#                reveal[color] = amount
                
print(game_dict)


        

