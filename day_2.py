import re

test_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

def main(input):
    # Initialize dictionary to store the resulting data structure
    cube_data = {}

    # Split the input into a list of games
    list_of_games = input.split("\n")[:-1]

    # Iterate through each game and process the data
    for game in list_of_games:
        # Get game number from the game information
        game_info = game.split(": ")
        game_number = int(game_info[0].split(" ")[1])

        # Get subsets of cubes from the game information
        outcomes = [re.findall(r'(\d+) (\w+)|(\d+) (\w+)|(\d+) (\w+)', subset)[0] for subset in game_info[1].split("; ")]

        game_data = []
        for outcome in outcomes:
            # Initialize a dictionary for each subset
            outcome_dict = {'green': 0, 'blue': 0, 'red': 0}
            for i in range(0, len(outcome), 2):
                count = int(outcome[i])
                color = outcome[i + 1].lower()
                outcome_dict[color] = count
            # Add this dictionary to the game_data list
            game_data.append(outcome_dict)

        # Add the game_data list to the right game number in the example_array dictionary
        cube_data[game_number] = game_data

    # Now we have our accessible data structure, time to access it and check against the numbers

    # We are allowed 12 red cubes, 13 green cubes, and 14 blue cubes

    game_number = 1  # Could use the enumerate function, but our game numbers start at 1

    running_total = 0  # Initialize the starting value for our final answer

    for game in cube_data.values():
        # Now each 'game' iteration should be a list of dicts

        # We're going to initialize our counters here, they should reset when our loop moves onto the next game
        number_of_green_cubes = 13
        number_of_blue_cubes = 14
        number_of_red_cubes = 12

        # Now loop through each dict in our list of dicts
        for draw in game:
            # Now each 'draw' should be a dict, so we simply access the values in that dict
            number_of_blue_cubes -= draw['blue']
            number_of_green_cubes -= draw['green']
            number_of_red_cubes -= draw['red']

        # Once we're out of this loop, we should have the number of remaining cubes of each color, in the bag

        # So let's check if this game is allowed and if so, add it to our running total. if there is a negative number of cubes in the bag, this is clearly not possible.
        if number_of_blue_cubes >= 0 and number_of_green_cubes >= 0 and number_of_red_cubes >= 0:
            running_total += game_number 

        game_number += 1

    return running_total  # Our final answer

print(main(test_input))
