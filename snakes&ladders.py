import random
import time

# Constants representing the starting and ending squares on the board
START_SQUARE = 0
END_SQUARE = 100

#Ladder randomisation variables
l1 = random.randint(3, 6)
l2 = random.randint(15, 19)
l3 = random.randint(21, 24)
l4 = random.randint(29, 30)
l5 = random.randint(38, 41)
l6 = random.randint(44, 48)
l7 = random.randint(56, 60)
l8 = random.randint(75, 77)
l9 = random.randint(82, 84)

# ladder1 = random.choice(13, 43)
# ladder2 = random.choice(14, 27)
win1 = random.choice([13, 14, 26, 27, 43])  
win2 = random.choice([26, 27, 31])
win3 = random.choice([36, 43, 49])
win4 = random.choice([38, 42]) 
win5 = random.randint(65, 67)
win6 = random.choice([85, 86, 88, 89, 90])
win7 = random.choice([78, 86])
win8 = random.choice([88, 89, 90])
win9 = random.choice ([94, 95, 96, 97])


s1 = random.randint(10, 12)
s2 = random.randint(32, 35)
s3 = random.randint(51, 54)
s4 = random.randint(61, 63)
s5 = random.choice([69, 70, 71, 87])
s6 = random.randint(72, 74)
s7 = random.randint(79, 81)
s8 = random.randint(91, 93)
s9 = random.randint(98, 99)
if s9 == 98:
    s10 = 99
else:
    s10 = 98

lose1 = random.choice([0,1,2,7])
lose2 = random.choice([13, 14])
lose3 = random.choice([25, 43])
lose4 = random.choice([42, 55])
lose5 = random.choice([20, 36])
lose6 = random.randint(65, 67) 
lose7 = random.choice([50, 54])
lose8 = random.choice([13, 43]) 
lose9 = random.choice([0, 2, 2, 25, 25, 50])
lose10 = 50

# Dictionary mapping square numbers to the number of squares to move forward or backward
# For example, if the player lands on square 97, they will move 3 squares backward

TROPHY = {
    100: 100,
}

die1 = random.choice([7, 8, 9])
die2 = random.choice([25, 26, 27, 28, 43])
die3 = random.choice([64, 68])
die4 = random.choice([78, 86])

ROLL_AGAIN = {
    die1: die1,
    die2: die2,
    die3: die3,
    die4: die4
}

SNAKES = {
    s1: lose1,
    s2: lose2,
    s3: lose3,
    s4: lose4,
    s5: lose5,
    s6: lose6,
    s7: lose7,
    s8: lose8,
    s9: lose9,
    s10: lose10
}

LADDERS = {
    l1: win1,
    l2: win2,
    l3: win3,
    l4: win4,
    l5: win5,
    l6: win6,
    l7: win7,
    l8: win8,
    l9: win9
}



# Dictionary mapping numbers to ASCII art images of dice
DICE_IMAGES = {
    1: """
---------
|       |
|   O   |
|       |
---------
""",
    2: """
---------
|       |
| O   O |
|       |
---------
""",
    3: """
---------
|   O   |
|   O   |
|   O   |
---------
""",
    4: """
---------
| O   O |
|       |
| O   O |
---------
""",
    5: """
---------
| O   O |
|   O   |
| O   O |
---------
""",
    6: """
---------
| O   O |
| O   O |
| O   O |
---------
"""
}

# Emoji for snake squares
SNAKE_EMOJI = "🐍"

# Emoji for ladder squares
LADDER_EMOJI = "🪜"

# Emoji for roll again squares 
DICE_EMOJI = "🎲"

#Emoji for 100th square
TROPHY_EMOJI = "🏆"

roll = 0
spaces_back = 0
player_number = 0



# Function to move the player's position on the board
def move(position, player_number):
    # Wait for the user to press the return button
    print()
    input("Roll the 🎲: ")

    # Roll the dice
    if position <= 94:
        roll = random.randint(1, 6)
    elif position == 95:
        roll = random.randint(1, 5)
    elif position == 96:
        roll = random.randint(1, 4)
    elif position == 97:
        roll = random.randint(1, 3)
    elif position == 98:
        roll = random.randint(1, 2)
    else:
        roll = random.randint(1, 2)

    # Display the dice image
    print(DICE_IMAGES[roll])

    # Update the player's position
    position += roll

    # Check if the player has advanced past square 100
    if position > END_SQUARE:
        # Calculate the number of spaces to move backwards
        spaces_back = position - END_SQUARE
        # Move the player backwards
        position -= spaces_back

    if position in SNAKES:
        # Move the player to the new position dictated by the snake
        position = SNAKES[position]
        print("Oh no! You were bitten by a snake and tumbled to square {}.".format(position))
        time.sleep(0.5)
    elif position in LADDERS:
        # Move the player to the new position dictated by the ladder
        position = LADDERS[position]
        print("Yay! You climbed up a ladder and moved to square {}.".format(position))
        time.sleep(0.5)
    elif position in ROLL_AGAIN:
        # Move the player to the new position dictated by the die
        position = ROLL_AGAIN[position]
        print()
        print("Player {}: Landed on Roll Again! (moved to square {})".format(player_number + 1, position))
        time.sleep(2)  

        print ()
        for i in range(1, 7):
         # Calculate the square number
            square_number = position + i
            # Check if the square is a snake or ladder square
            if square_number in SNAKES:
                print("{}: {} - {}".format(square_number, SNAKE_EMOJI, (square_number - position)))
            elif square_number in LADDERS:
                print("{}: {}  - {}".format(square_number, LADDER_EMOJI, (square_number - position)))
            elif square_number in ROLL_AGAIN:
                print("{}: {} - {}".format(square_number, DICE_EMOJI, (square_number - position)))
            elif square_number in TROPHY:
                print("{}: {} - {}".format(square_number, TROPHY_EMOJI, (square_number - position)))
            else:
                print("{}: ".format(square_number))

        print()

        input("Roll the 🎲: ")
        roll = random.randint(1, 6)
        print(DICE_IMAGES[roll])
        # Update the player's position
        position += roll
        # Check if the player has advanced past square 100
        if position > 100:
            # Calculate the number of spaces to move backwards
            spaces_back = position - 100
            # Move the player backwards
            position -= spaces_back 
           
        if position in SNAKES:
                # Move the player to the new position dictated by the snake
                position = SNAKES[position]
                print("Oh no! You were bitten by a snake and tumbled to square {}.".format(position))
                time.sleep(0.5)
        elif position in LADDERS:
                # Move the player to the new position dictated by the ladder
                position = LADDERS[position]
                print("Yay! You climbed up a ladder and moved to square {}.".format(position))
                time.sleep(0.5)
        else:
                print("You have moved to square {}.".format(position))
        # Print the outcome of the roll and the new position of the player
    elif position in TROPHY:
        position = TROPHY[position]
        print("Congratulations! You landed on Square 100 and have won the game! 🎉 🏆 🎉")
        time.sleep(5)
        exit()
    else:
        print("You have moved to square {}.".format(position))
        # Print the outcome of the roll and the new position of the player

    # Check if the player has reached the end square
    # if position == END_SQUARE:
    #     print("Player {} wins!".format(player_number + 1))
    #     exit()
    # else:
    return position


# Function to play a game of Snakes and Ladders
def play_game(num_players, position):
    # List to store the positions of all the players
    positions = [START_SQUARE] * num_players

    # Loop until one of the players has reached the end square
    while END_SQUARE not in positions:
        # Loop through the players in turn
        for i in range(num_players):
            # Print the current player's position
            print()
            print("...")
            print()
            while END_SQUARE not in positions:
                # Loop through the players in turn
                for player_number, position in enumerate(positions):
                    # Print the current player's position
                    print()
                    print()
                    print("Player {}: You are currently on square {}.".format(player_number + 1, position))
                    print()
                    # Display the board game
                    for i in range(1, 7):
                        # Calculate the square number
                        square_number = position + i
                        # Check if the square is a snake or ladder square
                        if square_number in SNAKES and square_number < 101:
                            print("{}: {} - {}".format(square_number, SNAKE_EMOJI, (square_number - position)))
                        elif square_number in LADDERS and square_number < 101:
                            print("{}: {}  - {}".format(square_number, LADDER_EMOJI, (square_number - position)))
                        elif square_number in ROLL_AGAIN and square_number < 101:
                            print("{}: {} - {}".format(square_number, DICE_EMOJI, (square_number - position)))
                        elif square_number in TROPHY:
                            print("{}: {} - {}".format(square_number, TROPHY_EMOJI, (square_number - position)))
                        else:
                            if square_number < 101:
                             print("{}: ".format(square_number))
                    # display_board_game(position, roll, player_number+1)

                    # Move the player
                    # positions[player_number] = move(position, player_number+1)
                    positions[player_number] = move(position, player_number)
                    time.sleep(2.5)
    return

def rules():
    print()
    print("...")
    print()
    print("Instructions: The goal of the game is to be the first player to reach square 100. Each player's turn consists of rolling a six sided die once.\n\n")
    print("Every single game the positions of snake and ladder (including inputs and outcome locations) squares are randomised!")
    print()
    print("Ladder square: \n🪜  = you can climb up to the top of the ladder.\n")
    print("Snake square: \n🐍 = you stumble away downwards from the head of the snake.\n")
    print("Roll Again square: \n🎲 = you can climb up to the top of the ladder.\n")
    print("Switch square: \n❓ = you switch positions with the nearest player! (can be enabled in settings)\n")
    print("Teleporter square: \n🟡 = teleports you to the other teleporter of it's kind! (can be enabled in settings)\n")
    print()
    time.sleep(2)
    options()
    return

def settings():
    print()
    time.sleep(0.5)
    print("Settings are coming soon...")
    time.sleep(0.5)
    options()
    return

def boardOverview():
    print()
    print("This is the current board layout!")
    print()
    time.sleep(0.5)
    print("...")
    print()
    time.sleep(1)
    for i in range(1, 101):
        # Calculate the square number
        position = 0
        square_number = position + i
        # Check if the square is a snake or ladder square
        if square_number in SNAKES and square_number < 101:
            print("{}: {} - {}".format(square_number, SNAKE_EMOJI, (square_number - position)))
            time.sleep(0.1)
        elif square_number in LADDERS and square_number < 101:
            print("{}: {}  - {}".format(square_number, LADDER_EMOJI, (square_number - position)))
            time.sleep(0.1)
        elif square_number in ROLL_AGAIN and square_number < 101:
            print("{}: {} - {}".format(square_number, DICE_EMOJI, (square_number - position)))
            time.sleep(0.1)
        elif square_number in TROPHY:
            print("{}: {} - {}".format(square_number, TROPHY_EMOJI, (square_number - position)))
            time.sleep(0.1)
        else:
            if square_number < 101:
                print("{}: ".format(square_number))
                time.sleep(0.1)
    time.sleep(4)
    print()
    options()
    # newBoard = str(input("What you like a new board? (y/n) "))
    # time.sleep(0.2)

    # if newBoard == "y" or newBoard == "yes":
    #     print()
    #     time.sleep(0.5)
    #     print("generating... (1/3)")
    #     print()

    #     # this function generates a new board layout
    #     generateNewBoard()

    #     time.sleep(0.9)
    #     print("generating... (2/3)")
    #     print()
    #     time.sleep(0.9)
    #     print("generating... (3/3)")
    #     print()
    #     time.sleep(0.33)
    #     print("New board has successfully generated!")
    #     time.sleep(1)
    #     print()
    #     print("...")
    #     time.sleep(3)

    #     # shows the updated board layout
    #     boardOverview()
    #     return
    # elif newBoard == "n" or newBoard == "no":
    #     print()
    #     time.sleep(0.5)
    #     print("no problem! Current board has been saved :)")
    #     time.sleep(0.5)
    #     options()
    #     return
    # else:
    #     options()
    #     return 

def generateNewBoard():
#Ladder randomisation variables
    l1 = random.randint(3, 6)
    l2 = random.randint(15, 19)
    l3 = random.randint(21, 24)
    l4 = random.randint(29, 30)
    l5 = random.randint(38, 41)
    l6 = random.randint(44, 48)
    l7 = random.randint(56, 60)
    l8 = random.randint(75, 77)
    l9 = random.randint(82, 84)

    # ladder1 = random.choice(13, 43)
    # ladder2 = random.choice(14, 27)
    win1 = random.choice([13, 14, 26, 27, 43])  
    win2 = random.choice([26, 27, 31])
    win3 = random.choice([36, 43, 49])
    win4 = random.choice([38, 42]) 
    win5 = random.randint(65, 67)
    win6 = random.choice([85, 86, 88, 89, 90])
    win7 = random.choice([78, 86])
    win8 = random.choice([88, 89, 90])
    win9 = random.choice ([94, 95, 96, 97])


    s1 = random.randint(10, 12)
    s2 = random.randint(32, 35)
    s3 = random.randint(51, 54)
    s4 = random.randint(61, 63)
    s5 = random.choice([69, 70, 71, 87])
    s6 = random.randint(72, 74)
    s7 = random.randint(79, 81)
    s8 = random.randint(91, 93)
    s9 = random.randint(98, 99)
    if s9 == 98:
        s10 = 99
    else:
        s10 = 98

    lose1 = random.choice([0,1,2,7])
    lose2 = random.choice([13, 14])
    lose3 = random.choice([25, 43])
    lose4 = random.choice([42, 55])
    lose5 = random.choice([20, 36])
    lose6 = random.randint(65, 67) 
    lose7 = random.choice([50, 54])
    lose8 = random.choice([13, 43]) 
    lose9 = random.choice([0, 2, 2, 25, 25, 50])
    lose10 = 50

    # Dictionary mapping square numbers to the number of squares to move forward or backward
    # For example, if the player lands on square 97, they will move 3 squares backward

    die1 = random.choice([7, 8, 9])
    die2 = random.choice([25, 26, 27, 28, 43])
    die3 = random.choice([64, 68])
    die4 = random.choice([78, 86])

    ROLL_AGAIN = {
        die1: die1,
        die2: die2,
        die3: die3,
        die4: die4
    }

    SNAKES = {
        s1: lose1,
        s2: lose2,
        s3: lose3,
        s4: lose4,
        s5: lose5,
        s6: lose6,
        s7: lose7,
        s8: lose8,
        s9: lose9,
        s10: lose10
    }

    LADDERS = {
        l1: win1,
        l2: win2,
        l3: win3,
        l4: win4,
        l5: win5,
        l6: win6,
        l7: win7,
        l8: win8,
        l9: win9
    }
    return die1, die2, die3, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, lose1, lose2, lose3, lose4, lose5, lose6, lose7, lose8, lose9, lose10, l1, l2, l3, l4, l5, l6, l7, l8, l9, win1, win2, win3, win4, win5, win6, win7, win8, win9

def options():
    print()
    time.sleep(0.5)
    print ("...")
    print()
    time.sleep(0.9)
    print("(r) - rules")
    time.sleep(0.9)
    print("(s) - settings")
    time.sleep(0.9)
    print("(b) - board overview")
    time.sleep(0.9)
    print("(sg) - start game")
    print()
    time.sleep(0.9)
    print ("...")
    print()
    options = str(input("What would you like to do? (r/s/b/sg) "))

    if options == "r" or options == "rules":
        rules()
        return
    elif options == "s" or options == "settings":
        settings()
        return
    elif options == "b" or options == "board overview":
        boardOverview() 
    elif options == "sg" or options == "start game":
        main()
    else:
        main()
        return 
    return

print()
time.sleep(0.33)
print("Welcome to 🐍 Snakes & 🪜  Ladders!")

# Main function
def main():
    position = 0
    startGame = 0
    print()
    time.sleep(0.5)
    print ("...")
    print()
    time.sleep(0.5)
    startGame = str(input("Would you like to start the game? (y/n) "))
    time.sleep(0.2)

    if startGame == "y" or startGame == "yes":
         print()
         num_players = int(input("Enter the number of players (2 - 8): "))

           # Validate the number of players
         if num_players  < 2 or num_players > 8:
            print("Error: invalid number of players. Please try again.")
            main()
         else:
            print("Player count set to {}!".format(num_players))
            time.sleep(1)
            print()
            print("starting game...")
            time.sleep(1)
            play_game(num_players, position)
         return
    elif startGame == "n" or startGame == "no":
        options()
        return
    else:
        main()
        return

   
# Run the main function
main()
