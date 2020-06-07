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

"""
-------------------
Student Information
-------------------
"""

"""
Name: Ashraf Bin Saleem
Student ID: 31039960

Start Date:  28/5/2020
Last Edit Date: 8/6/2020
"""

"""
---------------------
Overview Of Program
---------------------
"""

"""
This file contains code for the task 1.

Task 1 objective is to create a program that creates and stores a list of people with their social connections with
fellow members on the list. The program achieves this by reading a text file that was provided with its own specified
reading method. Upon reading the file, the program will store each person and their friends within a dictionary that
contains the objects of each person created. 
"""

"""
-----------------------
Beginning Of Code
-----------------------
"""

# creating a dictionary to store unique person name and store their person object.
# person_dict -> map the name with Person object
# { str : Person }
# key = person_name (str) & value =  Person_object
person_dict = {}


class Person:

    # Constructor
    # first_name: str -> the first name of the data
    # last_name: str -> the last name of the data
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.friends_list = []

    # Method that add friends to the objects friend_list[]
    # friend_person: Person -> person object
    def add_friend(self, friend_person):
        # adding Person object to friends_list[]
        self.friends_list.append(friend_person)

    # Method to return person name
    # return will return first_name + last_name
    def get_name(self):
        return self.first_name + " " + self.last_name

    # Method to return person friend_list[]
    # return will return friend_list[]
    def get_friends(self):
        return self.friends_list


# Return Person object if exist in dictionary if not create new dictionary entry and return it.
# name: str -> string read from text file
def dict_loader(name):
    # validating if dictionary key exist or not, if not create new Person
    if name not in person_dict:
        # assigning first part of string eg : "Gill"
        person_first_name = name.split(" ")[0]
        # assigning second part of string eg : "Bates"
        person_last_name = name.split(" ")[1]
        # creating dictionary input with string name as key and Person as value
        person_dict[name] = Person(person_first_name, person_last_name)
    # returning the dictionary key/value
    return person_dict[name]

# Method to load (initialize) people
def load_people():
    # Validating if file can be opened
    try:
        # reading text file
        read_file = open("a2_sample_set.txt", "r")
        # creating a list to store person objects
        person_list = []
        # looping through each line in the text file
        for line in read_file:
            # splitting each line into half's
            line_splitted = line.split(": ")

            # assigning the dictionary value based on the input of the first half of the line (aka the person name).
            person = dict_loader(line_splitted[0])

            # adding friends
            for friend_name in line_splitted[1].split(", "):
                # adding a person friend to the list by checking the second half of the line
                friend_person = dict_loader(friend_name.rstrip())
                # adding the value friend
                person.add_friend(friend_person)
            # adding a person to the person_list[]
            person_list.append(person)
        # returning person_list[]
        return person_list
    # returns and error if file cannot be found or opened
    except IOError:
        print("File could not be open !, please check if file named a2_sample_set.txt exist or close file !")


if __name__ == '__main__':
    # calling the load people method
    load_people()