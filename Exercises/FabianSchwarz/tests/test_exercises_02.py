"""
Test for the Exercise 2, Task 2
"""

import math
import unittest
import random



#Import the exercise 2
import pathlib
import importlib
import sys

here = pathlib.Path(__file__).parent
exercise_dir = here.parent

exercise2_spec=importlib.util.spec_from_file_location("exercise2",exercise_dir / "exercises_02.py")
exercise2 = importlib.util.module_from_spec(exercise2_spec)
exercise2_spec.loader.exec_module(exercise2)
sys.modules["exercise2"] = exercise2




class task_2_test(unittest.TestCase):
    """
    Test Class for assignement 2, task 2
    """


    def run_test(self,test_inpt):
        """
        wrapper for calling the function that is to be evaluated (-> easier to adjust if the testfunction name is different)
        """
        return exercise2.task2(*test_inpt)



    def test_normal_cases(self):
        #test fairly normal cases
        inpt = ["a","7","gh","fs","f","dlr","1","0","5.1"]
        response_expected = (['7', '1', '0', '5.1'], ['a', '7', 'f', '1', '0'])
        response = self.run_test(inpt)
        try:#test both orders
            self.assertTupleEqual(response,response_expected)
        except:
            self.assertTupleEqual(response, response_expected[::-1])


    def test_edge_cases(self):
        #test some arrays that are possible more challenging
        inpt = ["f","shkjsf","65.68686","7.",".55",".5555",str(math.pi),str(math.sqrt(2)),""," ","char","6.5.7"]
        response_expected = (['65.68686', '7.', '.55', '.5555', '3.141592653589793', '1.4142135623730951'], ['f', ' '])
        response = self.run_test(inpt)
        try:#test both orders
            self.assertTupleEqual(response, response_expected)
        except:
            self.assertTupleEqual(response, response_expected[::-1])
        


    def test_additional_cases(self):
        #test many floats
        inpt1 = [str(random.random()) for _ in range(2000)]
        self.assertTrue([] in self.run_test(inpt1))
        
        #test many one digit ints
        inpt2 = [str(random.randint(0,9)) for _ in range(2000)]
        response2 = self.run_test(inpt2)
        self.assertTrue(len(response2[0]) == len(response2[1]))



if __name__ == '__main__':
    unittest.main()


