# PART 1:
# Write a class for a French deck of cards (2-Ace of diamonds, hearts, spades, clubs).
# The deck of cards should behave like a sequence.
# When initialized the cards should all be in a well-defined order (2-Ace of each suite, suites in the order above
# I should be able to index into the deck to retrieve one card.
# I should be able to iterate over all cards in the deck.
# Printing a cards string representation should give me a nice, 
# readable description of that card.

import unittest
import math



class Card:
    """Card - Represent a Card by it's suite and value

    Attributes:
    --------------
    self.suits(str):                    the Card's suite
    self.type(str):                     Card type
    """
    def __init__(self, suit:str, type:str):
        self.suit = suit#define Card suits (hearts, spades etc.)
        self.type = type#define Card value (2,7,king, ace)

    def __repr__(self) -> str:
        return f"Card({self.suit}, {self.type})"
    
    def __str__(self) -> str:#string representation
        return f"{self.type} of {self.suit}"




class CardDeck:
    """CardDeck - A deck of Cards represented by a list of Card objects
    
    Attributes:
    --------------
    self.cards(list):                   list of Card objects
    """
    def __init__(self, cards:list):
        self.__class__.cards = cards

    def __iter__(self):
        return (elements for elements in self.__class__.cards)

    def __str__(self) -> str:#string representation
        return_str = ""
        for elements in self.__class__.cards:
            return_str += str(elements) + ", "

        return return_str[:-2]


    def __repr__(self) -> str:
        return f"CardDeck({self.__class__.cards})"

    def __getitem__(self,index: int):
        if 0 <= index < len(self.__class__.cards):
            return self.__class__.cards[index]
        else:
            raise IndexError(f"Index out of range ({index})")








class FrenchCardDeck(CardDeck):
    """Deck of French Cards
    
    """

    def __init__(self):
        cards = []
        card_suits = ["diamonds", "hearts", "spades","clubs"]
        card_types = ["2","3","4","5","6","7","8","9","jack","queen","king","ace"]
        for suits in card_suits:
            for types in card_types:
                cards.append(Card(suit=suits, type=types))

        super().__init__(cards=cards)


# PART 2:
# Create a second class that represents a deck of cards usable for Skat -- it should only contain cards from 7 upwards.
# It should offer all the same functionality of the first class.



class SkatDeck(CardDeck):
    """Deck of Cards for Skat
    
    """

    def __init__(self):
        cards = []
        card_suits = ["diamonds", "hearts", "spades","clubs"]
        card_types = ["7","8","9","jack","queen","king","ace"]
        for suits in card_suits:
            for types in card_types:
                cards.append(Card(suit=suits, type=types))

        super().__init__(cards=cards)




# Write some code to test the functionality of both kinds of decks. (You can use `assert` to make sure your classes behave the way you expect them to.)




class card_game_test(unittest.TestCase):
    """
    Test class for the card games
    """

    def test_Card_object(self):
        TestCard = Card(suit="diamonds",type="ace")#create Test Card
        #test string representation
        test_str_representation_expected = "ace of diamonds"
        test_str_representation_actual = str(TestCard)
        self.assertEqual(test_str_representation_expected,test_str_representation_actual)

        #test attribtes (assert they are public)
        test_attr_type_public_expected = "ace"
        test_attr_type_public_actual = TestCard.type
        self.assertEqual(test_attr_type_public_expected,test_attr_type_public_actual)


    def test_indexing(self):
        TestFrenchCardDeck = FrenchCardDeck()
        TestSkatDeck = SkatDeck()

        ExampleCardFrench = TestFrenchCardDeck[0]
        ExampleCardSkat = TestSkatDeck[0]
        self.assertIsInstance(ExampleCardFrench,Card)
        self.assertIsInstance(ExampleCardSkat,Card)


    def test_iterating(self):
        TestFrenchCardDeck = FrenchCardDeck()
        TestSkatDeck = SkatDeck()

        for cards in TestFrenchCardDeck:#test iterating through the FrenchCardDeck
            self.assertIsInstance(cards, Card)
            self.assertIsInstance(str(cards), str)

        for cards in TestSkatDeck:#test iteratin through the SkatDeck
            self.assertIsInstance(cards, Card)
            self.assertIsInstance(str(cards), str)

    def test_str_representation(self):
        TestFrenchCardDeck = FrenchCardDeck()
        TestSkatDeck = SkatDeck()
        #FrenchDeck representation as string
        FrenchDeck_str_expected = "2 of diamonds, 3 of diamonds, 4 of diamonds, 5 of diamonds, 6 of diamonds, 7 of diamonds, 8 of diamonds, 9 of diamonds, jack of diamonds, queen of diamonds, king of diamonds, ace of diamonds, 2 of hearts, 3 of hearts, 4 of hearts, 5 of hearts, 6 of hearts, 7 of hearts, 8 of hearts, 9 of hearts, jack of hearts, queen of hearts, king of hearts, ace of hearts, 2 of spades, 3 of spades, 4 of spades, 5 of spades, 6 of spades, 7 of spades, 8 of spades, 9 of spades, jack of spades, queen of spades, king of spades, ace of spades, 2 of clubs, 3 of clubs, 4 of clubs, 5 of clubs, 6 of clubs, 7 of clubs, 8 of clubs, 9 of clubs, jack of clubs, queen of clubs, king of clubs, ace of clubs"
        FrenchDeck_str_actual = str(TestFrenchCardDeck)
        self.assertEqual(FrenchDeck_str_expected,FrenchDeck_str_actual)
        
        #SkatDeck representation as string
        SkatDeck_str_expected = "7 of diamonds, 8 of diamonds, 9 of diamonds, jack of diamonds, queen of diamonds, king of diamonds, ace of diamonds, 7 of hearts, 8 of hearts, 9 of hearts, jack of hearts, queen of hearts, king of hearts, ace of hearts, 7 of spades, 8 of spades, 9 of spades, jack of spades, queen of spades, king of spades, ace of spades, 7 of clubs, 8 of clubs, 9 of clubs, jack of clubs, queen of clubs, king of clubs, ace of clubs"
        SkatDeck_str_actual = str(TestSkatDeck)
        self.assertEqual(SkatDeck_str_expected,SkatDeck_str_actual)



# PART 3:
# write a function that accepts two numbers, a lower bound and an upper bound.
# the function should then return the count of all numbers that meet certain criteria:
# - they are within the (left-inclusive and right-exclusive) bounds passed to the function
# - there is at least one group of exactly two adjacent digits within the number which are the same (like 33 in 123345)
# - digits only increase going from left to right
#
# Examples:
# - 123345 is a valid number
# - 123341 is not a valid number, as the digits do not increase from left to right
# - 123334 is not a valid number as there is no group of exactly two repeated digits
# - 111334 is a valid number. while there are three 1s, there is also a group of exactly two 3s.
# - 112233 is a valid number. At least one group of two is fulfilled, there is no maximum to the number of such groups.
#
# run your function with the lower bound `134564` and the upper bound `585159`. Note the resulting count
# in your pull request, please.



def split_digits(n:int, base=10):
    """Generator to split number into digits

    Parameters:
    --------------
    n(int):                             integer to split into digits
    base(int)=10                        base to split integer to

    Return Values:
    --------------
    function:                           function to split ints into digits

    #! the digits this returns are in descending order !
    """
    if n == 0:
        yield 0
    while n:
        n, d = divmod(n, base)
        yield d


def calculate_current_digit_params(inpt_num:int, known_digit_count=None) -> int:
    """calculate the current digit count and difference between biggest possible number with that many digits
    Parameters:
    --------------
    inpt_num(int):                      input number

    Return Values:
    --------------
    Tuple of:
    digit_count(int):                   Digit count
    int:                                10**digit_count - inpt_num - 1 - nums of iterations until the digit_count increases


    function to determine how many digits the number has and how many steps until the count increases
    - inpt_num: Input Number
    - known_digit_count: used if the present digit count is already known
    """
    if known_digit_count:
        pass

        return known_digit_count+1, 10**(known_digit_count+1) - 10**known_digit_count - 1

    else:
        digit_count = int(math.log10(inpt_num)+1)#get current digit count

        return digit_count, 10**digit_count - inpt_num - 1#return amount of iterations before digit count has to be re-checked


def is_in_order(inpt:tuple) -> bool:
    """determine if a tuple is in descending order

    Parameters:
    --------------
    inpt(tuple):                        input tuple

    Return Values:
    --------------
    bool:                               True if the tuple is descending order
    """
    prev_element = 9#setting to 9 to not interfere with the logic
    for elements in inpt:
        if elements > prev_element:
            return False
        else:
            prev_element = elements
    return True


def determine_runs(current_num:int, current_num_digit_tuple:tuple, valid:bool, double_appearance=None):
    #TODO: implemented run calculation
    """calculate skippable numbers
    Function that calculates `runs` in the task, enabling skipping iterations

    Parameters:
    --------------
    current_num(int):                   current number 
    current_num_digit_tuple(tuple):     tuple of digits of current number, inverted
    valid(bool):                        determines whether the function is looking for runs of valid or invalid numbers

    Return Values:
    --------------
    skip_count(int):                    how many iterations to skip

    NOTES:
    --------------
    for invalid:
    1. find 'problem' in data -> loop trough array until point is found at which the order is broken
    2. calculate how many runs are left until the 'problem' dissapears

    for valid:
    1. get first valid double in inverted list
    """
    skip_count = None#placeholder

    return skip_count



def contains_adjacent_double(digit_count:int, digit_tuple:tuple) -> int:
    """check whether there is at least one `double`

    Parameters:
    --------------
    digit_count(int):                   the count of digits currently used
    digit_tuple(tuple):                 Tuple of the number to analyze (order inverted!)

    Return Values:
    --------------
    if there is a double:
    int:                                position of the firts element of the double in the tuple
    if there is no double:
    None
    
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






def double_finder(lower_bound:int, upper_bound:int) -> int:
    """Solution for Exercise 3

    Parameters:
    --------------
    lower_bound(int):                   lower bound of the loop(inclusive)
    upper_bound(int):                   upper bound of the loop(exclusive)
    
    Return Values:
    --------------
    int:                                count of numbers that fulfill the requirements:

    - they are within the (left-inclusive and right-exclusive) bounds passed to the function
    - there is at least one group of exactly two adjacent digits within the number which are the same (like 33 in 123345)
    - digits only increase going from left to right

    """

    hit_count = 0
    skip_count = 0#Debug information, counts how many numbers have been skipped
    starting_digit_params = calculate_current_digit_params(lower_bound)
    current_digit_count = starting_digit_params[0]
    runs_left_to_digit_increase = starting_digit_params[1]
    run_present = False


    i = lower_bound
    while i < upper_bound:
        iterator_digits_tuple = tuple(split_digits(i))
        iterator_digits_set = set(iterator_digits_tuple)
        iterator_unique_digit_count = len(iterator_digits_set)#unique digit count
        #only continue if there's less unique digits then total digits -> at least one element exists twice
        #print(i)
        if iterator_unique_digit_count < current_digit_count:
            if is_in_order(iterator_digits_set):#continue searching if in order
                adjacent_digit = contains_adjacent_double(current_digit_count,iterator_digits_tuple)
                if adjacent_digit != None:
                    hit_count += 1
            else:# don't continue searching if not in order, instead find runs
                pass
                """#TODO: uncomment code once run calculation is finished
                skips = determine_runs(current_num=i, current_num_digit_tuple=iterator_digits_tuple, valid=False)#determine amounts of skips
                i += skips
                skip_count += skips
                """



        runs_left_to_digit_increase -= 1
        i += 1

        if runs_left_to_digit_increase == 0:#check whether a re-calculation of the digit count is needed
            new_digit_params = calculate_current_digit_params(i, current_digit_count)
            current_digit_count = new_digit_params[0]
            runs_left_to_digit_increase = new_digit_params[1]

    return hit_count








class double_finder_test(unittest.TestCase):

    def test_response_given(self):
        """Test with given upper and lower bound
        """
        lower_bound = 134564
        upper_bound = 585159
        response_expected = 1306
        response_actual = double_finder(lower_bound=lower_bound,upper_bound=upper_bound)
        self.assertEqual(response_expected, response_actual)


"""
if __name__ == '__main__':#unittest test runner
    unittest.main()
"""

