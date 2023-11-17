#Gerrit Fritz
#29.10.2023

def add(i, pos, commands):
    commands[commands[i + 3]] = commands[pos[0]] + commands[pos[1]]
    return i + 4

def mul(i, pos, commands):
    commands[commands[i+3]] = commands[pos[0]] * commands[pos[1]]
    return i + 4

def inp(i, pos, commands):
    try: commands[commands[i + 1]] = int(input(":"))
    except: raise RuntimeError("invalid input")
    return i + 2

def out(i, pos, commands):
    print(commands[pos[0]])
    return i + 2

def jump_True(i, pos, commands):
    if commands[pos[0]] != 0: return commands[pos[1]]
    else: return i + 3

def jump_False(i, pos, commands):
    if commands[pos[0]] == 0: return commands[pos[1]]
    else: return i + 3

def less(i, pos, commands):
    if commands[pos[0]] < commands[pos[1]]: commands[pos[2]] = 1
    else: commands[pos[2]] = 0
    return i + 4 
    
def equals(i, pos, commands):
    if commands[pos[0]] == commands[pos[1]]: commands[pos[2]] = 1
    else: commands[pos[2]] = 0
    return i + 4


opcodes = {
    1: add,
    2: mul,
    3: inp,
    4: out,
    5: jump_True,
    6: jump_False,
    7: less,
    8: equals,
}


def mode_to_index(index, mode, commands):
    positions = []
    for i in range(0,len(mode)):
        if mode[i] == "0" and len(commands)>index+i+1:
            positions.append(commands[index+i+1])
        elif mode[i] == "1" and len(commands)>index+i+1:
            positions.append(index+i+1)
        else: raise KeyError("Wrong mode")
    return positions


def get_commands(number):
    command_tuple = divmod(number,100)
    return command_tuple[1], f"{command_tuple[0]:03d}"[::-1]


def get_output(commands):
    i=0
    while commands[i] != 99:
        opcode, mode = get_commands(commands[i])
        if opcode in opcodes.keys():
            positions = mode_to_index(i, mode, commands)
            i = opcodes[opcode](i, positions, commands)
        else: raise KeyError("Wrong opcode")
        

commands = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 40, 71, 224, 1001, 224, -111, 224, 4, 224, 1002, 223, 8, 223, 101, 7, 224, 224, 1, 224, 223, 223, 1102, 66, 6, 225, 1102, 22, 54, 225, 1, 65, 35, 224, 1001, 224, -86, 224, 4, 224, 102, 8, 223, 223, 101, 6, 224, 224, 1, 224, 223, 223, 1102, 20, 80, 225, 101, 92, 148, 224, 101, -162, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 5, 224, 224, 1, 224, 223, 223, 1102, 63, 60, 225, 1101, 32, 48, 225, 2, 173, 95, 224, 1001, 224, -448, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 4, 224, 1, 224, 223, 223, 1001, 91, 16, 224, 101, -79, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 3, 224, 224, 1, 224, 223, 223, 1101, 13, 29, 225, 1101, 71, 70, 225, 1002, 39, 56, 224, 1001, 224, -1232, 224, 4, 224, 102, 8, 223, 223, 101, 4, 224, 224, 1, 223, 224, 223, 1101, 14, 59, 225, 102, 38, 143, 224, 1001, 224, -494, 224, 4, 224, 102, 8, 223, 223, 101, 3, 224, 224, 1, 224, 223, 223, 1102, 30, 28, 224, 1001, 224, -840, 224, 4, 224, 1002, 223, 8, 223, 101, 4, 224, 224, 1, 223, 224, 223, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 107, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 329, 1001, 223, 1, 223, 8, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 344, 101, 1, 223, 223, 7, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 359, 101, 1, 223, 223, 1007, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 374, 1001, 223, 1, 223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 389, 101, 1, 223, 223, 1008, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 404, 1001, 223, 1, 223, 108, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 419, 1001, 223, 1, 223, 1108, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 434, 1001, 223, 1, 223, 108, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 449, 101, 1, 223, 223, 7, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 464, 1001, 223, 1, 223, 8, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 479, 1001, 223, 1, 223, 107, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 494, 101, 1, 223, 223, 1007, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 509, 1001, 223, 1, 223, 1107, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 524, 1001, 223, 1, 223, 108, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 539, 101, 1, 223, 223, 1107, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 554, 1001, 223, 1, 223, 107, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 569, 101, 1, 223, 223, 8, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 584, 1001, 223, 1, 223, 7, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 599, 101, 1, 223, 223, 1008, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 614, 101, 1, 223, 223, 1008, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 629, 1001, 223, 1, 223, 1108, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 644, 101, 1, 223, 223, 1108, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 659, 1001, 223, 1, 223, 1107, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 674, 1001, 223, 1, 223, 4, 223, 99, 226]
get_output(commands)