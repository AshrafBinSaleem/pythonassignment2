# Visualisation code template for FIT9136 Assignment 2.
# Instructions to students:
# 1. Implement task 3 within this file as a working program. You may define
#   as many functions or classes as you require to complete this task, if needed.
#   You may also import any libraries allowed by the assignment specification.
# 2. Modify the filename (and import statement(s) where required) to replace
#   the xxxxxxxx with your student ID number.
# 3. Complete tasks 1 and 2 within the other template files. The finished
#   program is split into three files, linked together by import statements.
#   In your IDE, ensure all files are part of the same project so the Python
#   interpreter can locate them.
# 4. Before submission, you should remove these instructions from this
#   template file and add your own program comments instead. This template file
#   has omitted program comments, which are your responsibility to add. Any
#   other 'placeholder' comments should be removed from your final submission.


from a2_31039960_task2 import *
# as a re-naming namespace
import pandas as pd

# import statement to make use of functions/classes from earlier task(s).
# (change the xxxxxxxx to match the actual filename.)


def visual_curve(days, meeting_probability, patient_zero_health):
    result = run_simulation(days, meeting_probability, patient_zero_health)
    df = pd.DataFrame(result)
    graph = df.plot.line(legend=False)
    graph.set_ylabel('Count')
    graph.set_xlabel('Days')
    graph.figure.savefig('task3.png')


if __name__ == '__main__':
    visual_curve(60, 0.25, 49)
# do not add code here (outside the main block).
