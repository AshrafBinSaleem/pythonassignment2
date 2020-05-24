# Task 1 code template for FIT9136 Assignment 2.
# Instructions to students:
# 1. Where required, replace the *pass* statements with your own method and
#   function definitions. Your submission must comply with the specification:
#   do not rename specified functions or change the number or type of arguments
#   or return values; otherwise you will be deemed not to have demonstrated
#   clear comprehension of the specified instructions. (You may define
#   your own additional functions and instance variables if you wish, as long
#   as these don't contradict the specified requirements. You may also
#   import any libraries allowed by the assignment specification.)
# 2. Complete task 1 within the framework of this template file.
# 3. Modify the filename (AND import statement(s), where required) to replace
#   the xxxxxxxx with your student ID number.
# 4. Complete tasks 2 and 3 within the other template files. The finished
#   program is split into three files, linked together by import statements.
# 5. In this file, you may define your own testing code within the 'main'
#   block to check if your simulation is working when running this script file
#   directly. Code in the main block will not be run by the automarker algorithm,
#   which will instead test the specified functions/methods by attempting to
#   call them directly according to how they are defined in the assignment 
#   requirments specification.
# 6. Before submission, you should remove these instructions from this
#   template file and add your own program comments instead. This template file
#   has omitted program comments, which are your responsibility to add. Any
#   other 'placeholder' comments should be removed from your final submission.

class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.friends_list = []
        #pass # placeholder only. To be implemented in task 1.

    def add_friend(self, friend_person):
        self.friends_list.append(friend_person)
        #pass # placeholder only. To be implemented in task 1.

    def get_name(self):
        return self.first_name + " " + self.last_name
        #pass # placeholder only. To be implemented in task 1.

    def get_friends(self):
        return self.friends_list
        #pass # placeholder only. To be implemented in task 1.


def load_people():
    read_file = open("a2_sample_set.txt", "r")
    person_list = []
    for line in read_file:
        #spliting each line
        line_splited = line.split(": ")

        #seperating first name and last name and seperating person from friend
        person_first_name = line_splited[0].split(" ")[0]
        person_last_name = line_splited[0].split(" ")[1]
        person = Person(person_first_name, person_last_name)

        #adding friends
        for friend_name in line_splited[1].split(", "):
            friend_first_name = friend_name.split(" ")[0]
            friend_last_name =  friend_name.split(" ")[1]
            friend_person = Person(friend_first_name, friend_last_name)
            person.add_friend(friend_person)

        person_list.append(person)
        print(person.get_friends())
    #pass # placeholder only. To be implemented in task 1.
    print(person_list)
    return person_list

if __name__ == '__main__':
    load_people()
    #pass # placeholder only. You may add your own testing code within this
         # main block to check if the code is working the way you expect.



# do not add code here (outside the main block).
