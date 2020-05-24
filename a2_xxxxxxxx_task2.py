# Task 2 code template for FIT9136 Assignment 2.
# Instructions to students:
# 1. Where required, replace the *pass* statements with your own method and
#   function definitions. Your submission must comply with the specification:
#   do not rename specified functions or change the number or type of arguments
#   or return values; otherwise you will be deemed not to have demonstrated
#   clear comprehension of the specified instructions. (You may define
#   your own additional functions and instance variables if you wish, as long
#   as these don't contradict the specified requirements. You may also
#   import any libraries allowed by the assignment specification.)
# 2. Complete task 2 within the framework of this template file.
# 3. Modify the filename (and import statement(s) where required) to replace
#   the xxxxxxxx with your student ID number.
# 4. Complete tasks 1 and 3 within the other template files. The finished
#   program is split into three files, linked together by import statements.
# 5. In this file, you may define your own testing code within the main block
#   to check if your simulation is working when running this script file
#   directly. Code in the main block will not be run by the automarker algorithm,
#   which will instead test the specified functions/methods by attempting to
#   call them directly according to how they are defined in the assignment 
#   requirments specification.
# 6. Before submission, you should remove these instructions from this
#   template file and add your own program comments instead. This template file
#   has omitted program comments, which are your responsibility to add. Any
#   other 'placeholder' comments should be removed from your final submission.

from a2_xxxxxxxx_task1 import *

class Patient(Person):
    def __init__(self, first_name, last_name, health):
        pass # placeholder only. To be implemented in task 2.

    def get_health(self):
        pass # placeholder only. To be implemented in task 2.

    def set_health(self, new_health):
        pass # placeholder only. To be implemented in task 2.

    def is_contagious(self):
        pass # placeholder only. To be implemented in task 2.

    def infect(self, viral_load):
        pass # placeholder only. To be implemented in task 2.

    def sleep(self):
        pass # placeholder only. To be implemented in task 2.


def run_simulation(days, meeting_probability, patient_zero_health):
    pass # placeholder only. To be implemented in task 2.

def load_patients(initial_health):
    pass # placeholder only. To be implemented in task 2.


if __name__ == '__main__':
    # You may add your own testing code within this main block
    # to check if the code is working the way you expect.

    #This is a sample test case. Write your own testing code here.
    test_result = run_simulation(15, 0.8, 49)
    print(test_result)
    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    #
    # Note: since this simulation is based on random probability, the
    # actual numbers may be different each time you run the simulation.


    # Another sample test case (high meeting probability means this will
    # spread to everyone very quickly; 40 days means will get 40 entries.)
    test_result = run_simulation(40, 1, 1)
    #sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200, 
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

    

# do not add code here (outside the main block).
