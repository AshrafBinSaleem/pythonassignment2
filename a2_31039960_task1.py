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
    Constructor
    first_name: str -> the first name of the person
    last_name: str -> the last name of the person
    """
    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name
        self.friends_list = []

    """
    Method that add friends to the objects friend_list[]
    friend_person: Person -> person object
    """
    def add_friend(self, friend_person):
        self.friends_list.append(friend_person)  # adding Person object to friends_list[]

    """
    Method to return person name
    :return: will return first_name + last_name
    """
    def get_name(self):
        return self.first_name + " " + self.last_name

    """
    Method to return person friend_list[]
    :return: return will return friend_list[]
    """
    def get_friends(self):
        return self.friends_list


"""
Method to return Person object if exist in dictionary if not create new dictionary entry and return it.
:param name: takes in name of person to check against dictionary key
:return: person_dict[name]
"""
def dict_loader(name):
    if name not in person_dict:  # validating if dictionary key exist or not, if not create new Person
        person_first_name = name.split(" ")[0]  # assigning first part of string eg : "Gill"
        person_last_name = name.split(" ")[1]  # assigning second part of string eg : "Bates"
        person_dict[name] = Person(person_first_name, person_last_name)  # creating dictionary input with string name as key and Person as value
    return person_dict[name]  # returning the dictionary key/value


"""
Method to load (initialize) people
:return: person_list
"""
def load_people():
    # Validating if file can be opened
    try:
        read_file = open("a2_sample_set.txt", "r")  # reading text file
        person_list = []  # creating a list to store person objects
        for line in read_file:  # looping through each line in the text file
            line_splitted = line.split(": ")  # splitting each line into half's
            person = dict_loader(line_splitted[0])  # assigning the dictionary value based on the input of the first half of the line (aka the person name).
            for friend_name in line_splitted[1].split(", "):  # adding friends
                friend_person = dict_loader(friend_name.rstrip())  # adding a person friend to the list by checking the second half of the line
                person.add_friend(friend_person)  # adding the value friend
            person_list.append(person)  # adding a person to the person_list[]
        return person_list  # returning person_list[]
    except IOError:  # returns and error if file cannot be found or opened
        print("File could not be open !, please check if file named a2_sample_set.txt exist or close file !")


"""
Main method to run all functions required for program to work.
"""
if __name__ == '__main__':
    load_people()  # calling the load people method