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
        pass



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
        pass









if __name__ == '__main__':
    unittest.main()