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



    i = lower_bound
    while i < upper_bound:
        digit_tuple = tuple(split_digits(i))

        elem_counter = 1
        ordered = True
        adj_elements = False
        for idx,elements in enumerate(digit_tuple):
            if idx == 0:
                continue
            if elements > digit_tuple[idx-1]:
                ordered = False
                #calculate skips
                curr_skips = 0
                for j in range(0,idx+1):
                    if digit_tuple[j] < elements:
                        curr_skips += elements - digit_tuple[j]
                #print(f"i: {i}, skips: {curr_skips}, new_i: {i+curr_skips}")#Debug statement
                if curr_skips > 0:
                    i += curr_skips - 1
                    skip_count += curr_skips - 1
                if i >= upper_bound:
                    return hit_count
                break
            elif elements == digit_tuple[idx-1]:
                elem_counter += 1
            else:
                if elem_counter == 2:
                    adj_elements = True
                elem_counter = 1
        if elem_counter == 2:
            adj_elements = True

        if ordered and adj_elements:
            hit_count += 1

        i += 1
    print(f"{skip_count} Skips have been performed")
    return hit_count




"""
from timeit import timeit
print(double_finder(134564, 585159))

print(timeit(lambda: double_finder(134564, 585159), number=10)/10)# on average: 0.25s on personal hardware
"""







class double_finder_test(unittest.TestCase):

    def test_response_given(self):
        """Test with given upper and lower bound
        """
        lower_bound = 134564
        upper_bound = 585159
        response_expected = 1306
        response_actual = double_finder(lower_bound=lower_bound,upper_bound=upper_bound)
        self.assertEqual(response_expected, response_actual)



if __name__ == '__main__':#unittest test runner
    unittest.main()


