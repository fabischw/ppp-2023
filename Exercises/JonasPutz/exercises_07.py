# to solve todays exercise you will need a fully functional int-computer
# a fully functional int-computer has some additional features compared to the 
# last one you implemented.
# you can either use my implementation of an int-computer (see AtrejuTauschinsky/int_computer.py)
# or you can extend your own int-computer with the necessary features. If you want to extend your own
# the features you need to implement will be described at the bottom.
#
#
# We will run 'breakout' -- the arcade game -- on our simulated computer. 
# (https://en.wikipedia.org/wiki/Breakout_(video_game))
# The code for the computer will be provided under data/breakout_commands.txt
# the code will produce outputs in triplets. every triplet that is output
# specifies (x-position, y-position, tile_type).
# tiles can be of the following types:
# 0: empty tile
# 1: wall. walls are indestructible
# 2: block. blocks can be destroyed by the ball
# 3: paddle. the paddle is indestructible
# 4: ball. the ball moves diagonally and bounces off objects
# 
# EXAMPLE:
# a sequence of output values like 1, 2, 3, 6, 5, 4 would
#  - draw a paddle (type 3) at x=1, y=2
#  - draw the ball (type 4) at x=6, y=5
#
#
# PART 1:
# run the game until it exits. Analyse the output produced during the run, and create
# a visual representation (matplotlib or ascii-art are possibilities here...) of the screen display.
# mark the different tile types as different colors or symbols. Upload the picture with your PR.
#
# PART 2:
# The game didn't actually run in part 1, it just drew a single static screen.
# Change the first instruction of the commands from 1 to 2. Now the game will actually run.
# when the game actually runs you need to provide inputs to steer the paddle. whenever the computer
# requests you to provide an input, you can chose to provide
# -  0: the paddle remains in position
# - -1: move the paddle to the left
# - +1: move the paddle to the right
#
# the game also outputs a score. when an output triplet is in position (-1, 0) the third value of
# the triplet is not a tile type, but your current score.
# You need to beat the game by breaking all tiles without ever letting the ball cross the bottom 
# edge of the screen. What is your high-score at the end of the game? provide the score as part of your PR.
#
# BONUS: (no extra points, just for fun)
# make a movie of playing the game :)
#
#
# COMPLETE INT COMPUTER
# This is only relevant if you decide to extend your own implementation with the necessary features.
# If you decide to use my implementation you can ignore this part.
#
#
# - The computer needs to implement memory much /larger/ than the set of initial commands.
#   Any memory address not part of the initial commands can be assumed to be initialized to 0.
#   (only positive addresses are valid).
# - You need to support a new parameter mode, 'relative mode', denoted as mode 2 in the 'mode' part
#   of the instructions.
#   Relative mode is similar to position mode (the first access mode you implemented). However, 
#   parameters in relative mode count not from 0, but from a value called 'relative offset'. 
#   When the computer is initialized, the relative offset is initialized to 0, and as long as it remains
#   0 relative mode and position mode are identical.
#   In general though parameters in relative mode address the memory location at 'relative offset + parameter value'.
#   EXAMPLE: if the relative offset is 50, the mode is 2, and the value you read from memory is 7 you should 
#     retrieve data from the memory address 57.
#     Equally, if you read -7, you should retrieve data from the memory address 43.
#   This applies to both read- and write operations.
# - You need to implement a new opcode, opcode 9. opcode 9 adjusts the relative offset by the value of its only parameter.
#   the offset increases by the value of the parameter (or decreases if that value is negative).
from exercises_07_computer import IntComputer
from exercises_07_breakoutgui import BreakoutGUI
from pathlib import Path

def get_breakout_commands() -> list[int]:
    """ Gets the commands from breakout_commands.txt

        Returns them as a List of ints"""
    
    commands = []
    with (Path(__file__).parent.parent.parent / 'data' / 'breakout_commands.txt').open("r") as ifile:
        commands = [int(val.strip()) for val in ifile]

    return commands

def user_input() -> int:
    """ Gets a console input by the user
    
        This will only accept the controls sepcified below"""
    print(breakout_gui)

    while (answer := input("Input: ")) not in _CONTROLS:
        print(_control_str)

    return _CONTROLS[answer]

_CONTROLS = { #The possible user inputs and their interpretation
    '0': 0,
    '1': 1,
    '-1': -1,
    '2' : -1,

    'a': -1,
    's': 0,
    'd': 1,
}
_control_str = f"Controls: {[key + ': ' + ('left' if val == -1 else 'wait' if val == 0 else 'right') for key, val in _CONTROLS.items()]}"

def auto_input() -> int:
    """ Will automaticly send a input to the computer, keeping the paddle under the ball at all time"""
    print(breakout_gui)
    relative_pos = breakout_gui.get_ball_relative()
    if relative_pos < 0:
        return -1
    elif relative_pos == 0:
        return 0
    else:
        return 1

breakout_gui = BreakoutGUI(symbol_air = " ", symbol_wall = "#", symbol_block = "=", symbol_paddle = "-", symbol_ball = "o")

def run_game():
    commands = get_breakout_commands()
    commands[0] = 2 #switches to game mode

    print("Choose input mode: Auto [0], Manual [1]")
    while (mode := input("")) not in ['0', '1']: 
        pass

    input_method = None
    if mode == '0':
        input_method = auto_input
    else:
        input_method = user_input
        print(_control_str)


    running = True
    while running:
        IntComputer(input_method, breakout_gui.add_output).run(commands)

        print("\n\nFinal Board:")
        print(breakout_gui)

        while ((answer := input("Try again? [y] [n]\n")) not in ['y', 'n']): 
            pass
        
        running = answer == 'y'

run_game()