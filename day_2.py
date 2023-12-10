puzzle_input = '''Game 1: 4 red, 5 blue, 9 green; 7 green, 7 blue, 3 red; 16 red, 7 blue, 3 green; 11 green, 11 blue, 6 red; 12 red, 14 blue
Game 2: 12 blue, 11 green, 3 red; 6 blue, 5 green, 7 red; 5 red, 11 blue; 2 blue, 8 green
Game 3: 8 blue, 5 green, 2 red; 5 blue, 5 green, 7 red; 7 blue, 1 green, 7 red; 8 green, 14 blue, 7 red; 8 green, 14 blue; 8 blue, 2 green, 8 red
'''

# Initialize an empty dictionary to store game outcomes
games_dict = {}

# I'd say this is our goal data structure. This is probably way more complex than it needs to be lol 
example_data_structure = {
    1: [{'r': 1, 'g': 2, 'b': 3}, {'r': 1, 'g': 1}],
    2: [{'r': 10, 'g': 2, 'b': 3}, {'r': 1, 'g': 1, 'b': 10}],
    3: [{'r': 4, 'g': 2, 'b': 3}, {'r': 1, 'g': 3}]
}

# Split the input into a list of games
list_of_games = puzzle_input.split("\n")[:-1]  # This is now a list of strings

# Iterate through each game and process the data
for game in list_of_games:
    # For every game in our list of games, we're going to process that data and add each one to our dict
    game_info = game.split(": ")
    game_numbers = int(game_info[0].split(" ")[1])  # Get game number out
    outcomes = game_info[1].split("; ")  # Store outcomes as a list of strings, something like ['red = 1, blue = 2', 'red = 1, blue = 5, green = 10'] etc
    games_dict[game_numbers] = outcomes  # Build our dict

    # So now we go back into our list of strings, where each string is the result of one game:

    game_outcomes_list = []  # List that stores outcomes of the game we're currently looking at in our loop

    for outcome in outcomes:
        count, *colour = outcome.split(" ")  # Splits each element (outcome) into a list with two elements,
        # where the first element of each is assigned the variable count and the second assigned to colour
        # So now it'll be like [[red, 1], [blue, 2]], [[red, 5], [blue, 10], [green, 12]], etc.
        count = int(count)  # Currently the count is a string not an int so we want to make it an int

        # Initialize our goal data structure to represent each bag draw that makes up a game
        outcome_dict = {'r': 0, 'g': 0, 'b': 0}
        outcome_dict[colour] = count  # Set the value of each key to our count

        game_outcomes_list.append(outcome_dict)  # Now we have our list of dictionaries

    games_dict[game_numbers] = game_outcomes_list  # Setting each value of our dictionary (where the keys are the game IDs) to the list of dicts, where each element (each dict) is a bag draw

# Now let's define our limits, as provided in the question, and loop thru to see which games exceed these

total_of_game_IDs = 0

limits = {'r': 12, 'g': 13, 'b': 14}

# Let's loop through every game in our big dict of games
for game_number, outcomes_list in games_dict.items():
    # Default is to set to true
    possible = True

    for outcome_dict in outcomes_list:  # Outcomes_list is the list of dicts for each game, where each dict is each bag draw
        for colour, count in outcome_dict.items():
            limits[colour] -= count  # So for each bag draw we take away the quantity of each colour from our limit,
            # and if we end up with a negative number at the end, we've exceeded our limit
            if limits[colour] < 0:
                possible = False
                break
            if not possible:
                break

        if possible:  # If it's possible then we'll add that to our running total of possible game IDs
            total_of_game_IDs += game_number

# Print the final running total of possible games
print(f"Total of game IDs for possible games: {total_of_game_IDs}")
