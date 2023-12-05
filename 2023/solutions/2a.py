input_path = '../inputs/2a.txt'

with open(input_path, 'r') as file:
    aoc_input = file.read()

limit_dict = {'red': 12, 'green': 13, 'blue': 14}

game_dict = {}

games = aoc_input.splitlines()

for game in games:
    game_info = game.split(':')
    game_number = int(game_info[0].replace('Game ', ''))
    color_sets = game_info[1].split(';')

    game_dict[game_number] = {}

    for color_set in color_sets:
        colors = color_set.split(',')
        for color in colors:
            parts = color.strip().split(' ')
            count = int(parts[0])
            color_name = parts[1]
            game_dict[game_number][color_name] = count

print(game_dict)
    #        else:
    #            game_dict[game_number][color_name] = count

#total = 0
#
#for game, colors in game_dict.items():
#    counter = 0
#    for color, amount in colors.items():
#        if amount <= limit_dict[color]:
#            counter += 1
#            if counter == 3:
#                print(f"{game} is eligible")
#                total += game
                

# print(total)


        

