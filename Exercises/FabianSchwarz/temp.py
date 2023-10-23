def is_in_order(inpt:list):
    """determine if a set is in descending order
    """
    prev_element = 9#setting to 0 to not interfere with the logic
    for elements in inpt:
        if elements > prev_element:
            return False
        else:
            prev_element = elements
    return True



def is_in_order_2(inpt:list):
    return inpt.copy().sort() == inpt



from timeit import timeit

a = [2,3,5,3,3,6,5,6,6,7,8,3,3,4,6,8,4,2,3,4]

import random
a = [random.random() for i in range(1000000)]


print(timeit(lambda: is_in_order(a),number=100))
print(timeit(lambda: is_in_order_2(a), number=100))





