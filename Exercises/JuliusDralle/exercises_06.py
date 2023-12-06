# You get a recording of a terminal session moving around a file system.
# The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). 
# The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories
# and listing the contents of the directory you're currently in.
#
# Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:
#
# cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
# cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
# cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
# cd / switches the current directory to the outermost directory, /.
# ls means list. It prints out all of the files and directories immediately contained by the current directory:
# 123 abc means that the current directory contains a file named abc with size 123.
# dir xyz means that the current directory contains a directory named xyz.
#
# Here's an example:
#
# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
#
# Based on this example, you can deduce the directory structure must look something like this:
# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)
#
#
# PART 1:
# Write a function that reads a console session like the example above from a file, 
# and then returns a dictionary listing the size of each directory. Directories should
# be identified by their full path. For the example above:
#
# - The total size of directory `e` is 584 because it contains a single file `i` of size 584 and no other directories.
# - The directory `a` has total size 94853 because it contains files
#     `f` (size 29116), `g` (size 2557), and `h.lst` (size 62596),
#     plus file `i` indirectly (`a` contains `e` which contains `i`).
# - Directory `d` has total size 24933642.
# - As the outermost directory, `/` contains every file. Its total size is 48381165.
#
# Based on that functions output, calculate the total size of all directories where the size of each individual
# directory considered is at most 100000, and mention the result in your PR.
# For the example above the two directories meeting the size requirement are `a` and `e`, while `/` and `d` are too large.
# The sum of the size of a and e would be 95437.

import pathlib

path_here = pathlib.Path(__file__).parent
path_dir_exercises = path_here.parent
path_dir_root = path_dir_exercises.parent

path_dir_data = path_dir_root / "data"


######################################################################################

class Directory:
    def __init__(self, parent, name):
        self.parent = parent
        self.children = []
        self.name = name
        self.size = -1

    def __iter__(self):
        return(iterator for iterator in self.children)
    
    def __lt__(self,other):
        return self.size < other.size

    def add_dir(self, name):
        new_dir = Directory(self, name)
        self.children.append(new_dir)
        return new_dir

    def add_file(self,name,size):
        new_file = File(self,name,size)
        self.children.append(new_file)
        return new_file
    
    def get_size(self):
        size = 0 
        for element_of_children in self.children:
            size += element_of_children.size
        # get_size can be seen as "calculate_size"
        self.size = size
        return size
    
    def do_task_one(self,value_for_task_1 = 0):
        for element_of_children in self.children:
            if isinstance(element_of_children, Directory):
                value_for_task_1 += element_of_children.do_task_one()
                size_of_element_of_children = element_of_children.get_size()
                if size_of_element_of_children <= 100000:
                    value_for_task_1 += size_of_element_of_children
                    #print(f"The dir {element_of_children.get_name()} has a size of {size_of_element_of_children} and therefore counts in task 1")
        return value_for_task_1
   
class File:
    def __init__(self, parent, name, size: int):
        self.parent = parent
        self.size = int(size)
        self.name = name

######################################################################################

# #Testing of own classes
# root = Directory(None)
# childofRoot = root.add_dir()
# childofRoot.add_file(20)
# childofRoot.add_file(30)
# root.add_file(5)



with open(path_dir_data / "terminal_record.txt", "r") as input_file:
    input_lines = [input_single_line for input_single_line in input_file.read().split("\n")[:-1]]

#The whole file is saved in "input_lines" line for line

#print(input_lines)

root_directory = Directory(None, "/")
current_directory = root_directory

######################################################################################

def command_changedir(current_directory, root_directory,target):
    if target == "..":
        current_directory = current_directory.parent
        return current_directory, root_directory
    elif target == "/":
        current_directory = root_directory
        return current_directory, root_directory
    else:
        for searching_dir in current_directory:
            if searching_dir.name == target:
                current_directory = searching_dir
                return current_directory, root_directory
    raise ValueError("Directory not Found or not created, try creating one first!")


def command_list():
    pass

def command_add_file(size, name):
    current_directory.add_file(name, size)
    pass

######################################################################################

def command_handler(current_directory, root_directory, command):
    if command[0] == '$':
        command = command[2:]
        if command == "ls":
            pass
        else:
            command_p1, command_p2 = command.split(" ")
            current_directory, root_directory = command_changedir(current_directory, root_directory,command_p2)
    elif command[:3] == "dir":
        current_directory.add_dir(command[4:])
    else:
        size, name = single_line_i.split(" ")
        #print(f"File named {name} with size of {size}")
        command_add_file(size, name)
    return current_directory, root_directory



for single_line_i in input_lines:
    current_directory, root_directory = command_handler(current_directory, root_directory, single_line_i)
        


#print(root_directory.get_size())

print(root_directory.do_task_one())



# PART 2:
# In part 2 you need to identify a single directory to delete (including all sub-directories of course).
# The total space available to the filesystem is 70000000, and you need to make enough room to fit a file of 
# size 30000000.
#
# In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; 
# this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required.
# Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.
#
# To achieve this, you have the following options:
#
# Delete directory `e`, which would increase unused space by 584.
# Delete directory `a`, which would increase unused space by 94853.
# Delete directory `d`, which would increase unused space by 24933642.
# Delete directory `/`, which would increase unused space by 48381165.
# Directories `e` and `a` are both too small; deleting them would not free up enough space.
# However, directories `d` and `/` are both big enough! 
# Between these, choose the smallest: `d`, increasing unused space by 24933642.
# 
# Mention the total size of the deleted directory in the PR.
# 
# You can find the /actual/ input to both parts in data/terminal_record.txt
###############################################################################
list_of_directories = []

#calculates the sizes:
root_directory.get_size()

def put_all_dir_sizes_in_list(directory):
    global list_of_directories
    for element_of_children in directory.children:
            if isinstance(element_of_children, Directory):
                list_of_directories.append(element_of_children)
                put_all_dir_sizes_in_list(element_of_children)

def search_for_bigenough_dir(needed_size):
    for directory in list_of_directories:
        if directory.size >= needed_size:
            return directory

put_all_dir_sizes_in_list(root_directory)
list_of_directories.sort()


needed_size = 0
needed_size += root_directory.size
needed_size = 70000000 - needed_size
needed_size = 30000000 - needed_size

print(search_for_bigenough_dir(needed_size).size)

                