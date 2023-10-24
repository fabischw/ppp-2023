import unittest


#import required modules for importing the code to be tested
import pathlib
import importlib
import sys

here = pathlib.Path(__file__).parent
exercise_dir = here.parent

#Import the exercise 2 python file to test the task 2 module
exercise3_spec=importlib.util.spec_from_file_location("exercise3",exercise_dir / "exercises_03.py")
exercise3 = importlib.util.module_from_spec(exercise3_spec)
exercise3_spec.loader.exec_module(exercise3)
sys.modules["exercise3"] = exercise3




class task_3_component_test(unittest.TestCase):
    """
    Test Class for assignement 3, task 3 components
    """

    def test_split_digits(self):
        """Test the split_digits function
        
        """
        inpt1 = 1234
        response1_expected = (4,3,2,1)
        response1_actual = tuple(exercise3.split_digits(inpt1))
        self.assertTupleEqual(response1_expected,response1_actual)

        inpt2 = 5739236363333
        response2_expected = {2,3,5,6,7,9}
        response2_actual = set(exercise3.split_digits(inpt2))
        self.assertSetEqual(response2_expected,response2_actual)


    def test_calculate_current_digit_params(self):
        """Test the calculate_current_digit_params function
        
        """
        #test initial calculation
        inpt1 = 123445
        known_digit_count1 = None
        response1_expected = (6,876554)
        response1_actual = exercise3.calculate_current_digit_params(inpt_num=inpt1, known_digit_count=known_digit_count1)
        self.assertTupleEqual(response1_expected,response1_actual)

        #test calculation with known data
        inpt2 = None
        known_digit_count2 = 6
        response2_expected = (7,8999999)
        response2_actual = exercise3.calculate_current_digit_params(inpt_num=inpt2, known_digit_count=known_digit_count2)
        self.assertTupleEqual(response2_expected,response2_actual)



    def test_is_in_order(self):
        """Test the is_in_order function
        
        """
        inpt1 = (4,3,2,1)
        #response1_expected = True
        response1_actual = exercise3.is_in_order(inpt1)
        self.assertTrue(response1_actual)

        inpt2 = (4,4,3,2,1,1)
        #response2_expected = True
        response2_actual = exercise3.is_in_order(inpt2)
        self.assertTrue(response2_actual)

        inpt3 = (4,5,3,2,5,1)
        #response3_expected = False
        response3_actual = exercise3.is_in_order(inpt3)
        self.assertFalse(response3_actual)


    def test_contains_adjacent_double(self):
        """Test the contains_adjacent_double function
        
        """
        #check double at beginning
        inpt1_digit_tuple = (4,4,3,2,1)
        inpt1_digit_count = len(inpt1_digit_tuple)
        response1_expected = 0
        response1_actual = exercise3.contains_adjacent_double(inpt1_digit_count, inpt1_digit_tuple)
        self.assertEqual(response1_expected,response1_actual)

        #check no double
        inpt2_digit_tuple = (4,3,2,1)
        inpt2_digit_count = len(inpt2_digit_tuple)
        response2_expected = None
        response2_actual = exercise3.contains_adjacent_double(inpt2_digit_count, inpt2_digit_tuple)
        self.assertEqual(response2_expected,response2_actual)

        #check double near end
        inpt3_digit_tuple = (4,3,2,1,1)
        inpt3_digit_count = len(inpt3_digit_tuple)
        response3_expected = 3
        response3_actual = exercise3.contains_adjacent_double(inpt3_digit_count, inpt3_digit_tuple)
        self.assertEqual(response3_expected,response3_actual)

        #check duplicate doubles
        inpt4_digit_tuple = (9,9,8,6,6,4)
        inpt4_digit_count = len(inpt4_digit_tuple)
        response4_expected = 3
        response4_actual = exercise3.contains_adjacent_double(inpt4_digit_count, inpt4_digit_tuple)
        self.assertEqual(response4_expected,response4_actual)









if __name__ == '__main__':
    unittest.main()