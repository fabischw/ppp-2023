# Write a function that takes as input a list of integers and returns a single integer number.
# the numbers passed as argument form the working memory of a simulated computer.
# this computer will start by looking at the first value in the list passed to the function.
# this value will contain an `opcode`. Valid opcodes are 1, 2 or 99.
# Encountering any other value when you expect an opcode indicates an error in your coding.
# Meaning of opcodes:
#  1 indicates addition. If you encounter the opcode 1 you should read values from two positions 
#    of your working memory, add them, and store the result in a third position of your working memory.
#    The three numbers immediately after your opcode indicate the memory locations to read (first two values)
#    and write (third value) respectively. 
#    After executing the addition you should move to the next opcode by stepping forward 4 positions.
#  2 indicates multiplication. Otherwise the same rules apply as for opcode 1.
# 99 indicates halt. the program should stop after encountering the opcode 99.
# After the program stops, the function should return the value in the first location (address 0) 
# of your working memory.

# As an example, if the list of integers passed to your function is 
# [1, 0, 0, 0, 99] the 1 in the first position indicates you should read the values
# at position given by the second and third entries. Both of these indicate position 0, so you should read the value
# at position 0 twice. That value is 1. Adding 1 and 1 gives you two. You then look at the value in the fourth
# position, which is again 0, so you write the result to position 0. You then step forward by 4 steps, arriving at 99
# and ending the program. The final memory looks like [2, 0, 0, 0, 99]. Your function should return 2.

# Here's another testcase:
# [1, 1, 1, 4, 99, 5, 6, 0, 99] should become [30, 1, 1, 4, 2, 5, 6, 0, 99]
# Your function should return 30.


# print out which value is returned by your function for the following list:
def command_add(current_index, memory_stream):
    """Computer will add.

        This function adds two numbers and saves the result in the memory_stream
        
        The position of these Values in the memory Stream is determined by the values following the current index:
        memory_stream[current_index + 1] := The ID of the first value being added
        memory_stream[current_index + 2] := The ID of the second value being added
        memory_stream[current_index + 3] := The ID of the cell storing the result of the addition
        
        Parameters
        ----------
        current_index (int)
            the index in the memory_stream, that indicates the start of the add command
        memory_stream (int[])
            the memory_stream used by the mini computer. This will be modified in the function!
        
        Return Values
        -------------
        current_index
            the index where the computer should continue execution
    """

    id_val_1 = memory_stream[current_index + 1]
    id_val_2 = memory_stream[current_index + 2]
    id_result = memory_stream[current_index + 3]
    memory_stream[id_result] = memory_stream[id_val_1] + memory_stream[id_val_2]
    return current_index + 4


def command_multiply(current_index, memory_stream):
    """Computer will multiply.

        This function multiplies two numbers and saves the result in the memory_stream
        
        The position of these Values in the memory Stream is determined by the values following the current index:
        memory_stream[current_index + 1] := The ID of the first value being multiplied
        memory_stream[current_index + 2] := The ID of the second value being multiplied
        memory_stream[current_index + 3] := The ID of the cell storing the result of the multiplication
        
        Parameters
        ----------
        current_index (int)
            the index in the memory_stream, that indicates the start of the multiply command
        memory_stream (int[])
            the memory_stream used by the mini computer. This will be modified in the function!
        
        Return Values
        -------------
        current_index
            the index where the computer should continue execution
    """

    id_val_1 = memory_stream[current_index + 1]
    id_val_2 = memory_stream[current_index + 2]
    id_result = memory_stream[current_index + 3]
    memory_stream[id_result] = memory_stream[id_val_1] * memory_stream[id_val_2]
    return current_index + 4


def command_halt(current_index, memory_stream):
    """Computer will halt.

        This function just returns the new index -1, indicating the computer exits without an error.
        
        This function will not further change the memory stream

        Parameters
        ----------
        current_index (int)
            the index in the memory_stream, where the computer will halt
        memory_stream (int[])
            the memory_stream used by the mini computer
        
        Return Values
        -------------
        -1
            will be interpreted as an succesfull exit value
    """

    return -1


opt_code_dictionary = {
    1: command_add,
    2: command_multiply,
    99: command_halt
}


def mini_computer(memory_stream):
    """mini computer simulation program.

        This function will run the commands inputed as the argument.
        
        Parameters
        ----------
        memory_stream (int[])
            the commands used by the computer. This will be modified by the function on runtime  
        
        Return Values
        -------------
        memory_stream[0]
            the value in the first slot of th memory_stream
    """
    current_index = 0
    command_length = len(memory_stream)
    while current_index >= 0 and current_index < command_length:
        opt_code = memory_stream[current_index]
        if opt_code in opt_code_dictionary:
            current_index = opt_code_dictionary[opt_code](current_index, memory_stream)
        else:
            raise LookupError(f"Couldn't read optCode with value {opt_code} at position {current_index}")
    
    if current_index == -1:
        print("mini computer finished execution succesfully")
    else:
        print(f"mini computer finished execution with error code: {current_index}")
    
    return memory_stream[0]


commands = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 9, 19, 1, 5, 19, 23, 1, 6, 23, 27, 1, 27, 10, 31, 1, 31, 5, 35, 2, 10, 35, 39, 1, 9, 39, 43, 1, 43, 5, 47, 1, 47, 6, 51, 2, 51, 6, 55, 1, 13, 55, 59, 2, 6, 59, 63, 1, 63, 5, 67, 2, 10, 67, 71, 1, 9, 71, 75, 1, 75, 13, 79, 1, 10, 79, 83, 2, 83, 13, 87, 1, 87, 6, 91, 1, 5, 91, 95, 2, 95, 9, 99, 1, 5, 99, 103, 1, 103, 6, 107, 2, 107, 13, 111, 1, 111, 10, 115, 2, 10, 115, 119, 1, 9, 119, 123, 1, 123, 9, 127, 1, 13, 127, 131, 2, 10, 131, 135, 1, 135, 5, 139, 1, 2, 139, 143, 1, 143, 5, 0, 99, 2, 0, 14, 0]
return_value = mini_computer(commands)
print(f"mini computer returned the value {return_value}")

#output:
#mini computer finished execution succesfully
#mini computer returned the value 3562672

###########################################
# Write a function that takes an arbitrary number of unnamed arguments
# All inputs will be of type string.
# the function should return two lists:
#   The first list should contain all arguments which can be interpreted
#   as a number.
#   The second list should contain all strings which contain just one character.
# Think of some good inputs to test this functionality, write down at least three
# examples and verify that the output for these examples is correct.

def input_splitter(*args):
    """Splits the args in two seperate arrays

        Parameters
        ----------
        *args (strings)
            the inputs the program has to split
        
        Return Values
        -------------
        numbers
            an array of all numbers found in *args (in complex form)
        chars
            an array of all chars found in *args (including one digit numbers)
    """

    numbers = []
    chars = []

    for val in args:
        try:
            numbers.append(complex(val))
        except ValueError:
            pass

        if len(val) == 1:
            chars.append(val)

    return numbers, chars

test1 = [
    'a',
    'b',
    'c',
    'ab',
    '16',
    '25',
    '4',
    '1.32',
    '.5',
    '-8.3',
    '4.62.1',
    '54e-7',
]
#Output of test1:
#The Test with the input: ['a', 'b', 'c', 'ab', '16', '25', '4', '1.32', '.5', '-8.3', '4.62.1', '54e-7'] returned:
#numbers=[(16+0j), (25+0j), (4+0j), (1.32+0j), (0.5+0j), (-8.3+0j), (5.4e-06+0j)]
#chars=['a', 'b', 'c', '4']

test2 = [
    '1',
    '0',
    '-4',
    '123456789789745451212487845154.24689784546587456456',
    'aaaaaaaa',
    'kkj',
    'x'
]
#output of test2:
#The Test with the input: ['1', '0', '-4', '123456789789745451212487845154.24689784546587456456', 'aaaaaaaa', 'kkj', 'x'] returned:
#numbers=[(1+0j), 0j, (-4+0j), (1.2345678978974545e+29+0j)]
#chars=['1', '0', 'x']

test3 = [
    '5+7j',
    'a',
    'pi',
    '7.2-35.0004j',
    '9',
    '270e+3',
    '5.34e-5-24.5e+27j',
]
#output of test3:
#The Test with the input: ['5+7j', 'a', 'pi', '7.2-35.0004j', '9', '270e+3', '5.34e-5-24.5e+27j'] returned:
#numbers=[(5+7j), (7.2-35.0004j), (9+0j), (270000+0j), (5.34e-05-2.45e+28j)]
#chars=['a', '9']

current_test = test1
numbers, chars = input_splitter(*current_test)
print(f"The Test with the input: {current_test} returned:\n{numbers=}\n{chars=}")