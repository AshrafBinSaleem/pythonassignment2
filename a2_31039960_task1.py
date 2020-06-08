"""
-------------------
Student Information

Name: Ashraf Bin Saleem
Student ID: 31039960

Start Date:  28/5/2020
Last Edit Date: 8/6/2020
"""

"""
---------------------
Overview Of Program
---------------------

This file contains code for the task 1.

Task 1 objective is to create a program that creates and stores a list of people with their social connections with
fellow members on the list. The program achieves this by reading a text file that was provided with its own specified
reading method. Upon reading the file, the program will store each person and their friends within a dictionary that
contains the objects of each person created. 
"""

"""
----------------------
References
______________________
(1) 
URL: https://www.w3schools.com/python/ref_string_rstrip.asp
Date of retrieval: 3/06/2020

(2)
URL: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
Date of retrieval: 4/06/2020

(3)
URL: https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot
Date of retrieval: 4/06/2020

(4)
URL: https://realpython.com/documenting-python-code/#basics-of-commenting-code
Date of retrieval: 8/6/2020
"""

"""
-----------------------
Code
-----------------------
"""

# creating a dictionary to store unique person name and store their person object.
# person_dict -> map the name with Person object
# { str : Person }
# key = person_name (str) & value =  Person_object
person_dict = {}


class Person:
    """
    Person class
    """
    def __init__(self, first_name, last_name):
        """
        Constructor
        first_name: str -> the first name of the person
        last_name: str -> the last name of the person
        """
        self.first_name = first_name
        self.last_name = last_name
        self.friends_list = []

    def add_friend(self, friend_person):
        """
        Method that add friends to the objects friend_list[]
        friend_person: Person -> person object
        """

        # adding Person object to friends_list[]
        self.friends_list.append(friend_person)

    def get_name(self):
        """
        Method to return person name
        :return: will return first_name + last_name
        """

        return self.first_name + " " + self.last_name

    def get_friends(self):
        """
        Method to return person friend_list[]
        :return: return will return friend_list[]
        """
        return self.friends_list

def dict_loader(name):
    """
    Method to return Person object if exist in dictionary if not create new dictionary entry and return it.
    :param name: takes in name of person to check against dictionary key
    :return: person_dict[name]
    """

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



def load_people():
    """
    Method to load (initialize) people
    :return: person_list
    """

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
    """
    Main method to run all functions required for program to work.
    """

    # calling the load people method
    load_people()