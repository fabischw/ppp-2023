import math


def split_digits(n:int, base=10):
    """
    Generator to split number into digits
    #! the digit list is inverted 
    """
    if n == 0:
        yield 0
    while n:
        n, d = divmod(n, base)
        yield d




def calculate_current_digit_params(inpt_num:int, known_digit_count=None):
    """
    function to determine how many digits the number has and how many steps until the count increases
    - inpt_num: Input Number
    - known_digit_count: used if the present digit count is already known
    """
    if known_digit_count:
        pass

        return digit_count+1, 10**(known_digit_count+1) - 10**known_digit_count - 1

    else:
        digit_count = int(math.log10(inpt_num)+1)#get current digit count

        return digit_count, 10**digit_count - inpt_num - 1#return amount of iterations before digit count has to be re-checked


def is_in_order(inpt:tuple):
    """determine if a set is in descending order
    """
    prev_element = 9#setting to 0 to not interfere with the logic
    for elements in inpt:
        if elements > prev_element:
            return False
        else:
            prev_element = elements
    return True



def contains_adjacent_double(digit_count:int, digit_tuple:tuple):
    """check whether there is at least one double
    """
    prev_element = digit_tuple[digit_count-1]
    digit_counter = 0#count how often a digit has appeared
    for i in range(1, digit_count+2):
        curr_element = digit_tuple[digit_count-i]
        if curr_element == prev_element:#loop from right to left, check if double is present
            digit_counter += 1
        else:
            if digit_counter == 2:#double found
                return digit_count-2-(i-3)#return index of first appearence of a double in inverted tuple
            digit_counter = 1
        prev_element = curr_element
    return None#return None if there was no adjacent double found




test_data = 123345
test_data_tuple = tuple(split_digits(test_data))
test_data_set = set(test_data_tuple)
print(test_data_tuple)
print(test_data_set)


test_data_digit_params = calculate_current_digit_params(test_data)
digit_count = test_data_digit_params[0]
#print(test_data_digit_params)
print(digit_count)


#print(is_in_order(test_data_tuple))


print(contains_adjacent_double(digit_count=digit_count, digit_tuple=test_data_tuple))