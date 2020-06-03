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

from a2_31039960_task1 import *
import random

# patient_dict -> map the name with Patient object
# { str : Patient }
# key = patient_name (str) & value =  Patient_object
patient_dict = {}


class Patient(Person):
    def __init__(self, first_name, last_name, health):
        Person.__init__(self, first_name, last_name)
        self.health = health

    def get_health(self):
        return self.health

    def set_health(self, new_health):
        self.health = new_health

    def is_contagious(self):
        if 0 <= self.health <= 49:
            return True
        else:
            return False

    def infect(self, viral_load):
        if self.health <= 29:
            self.health = round(self.health - (0.1 * viral_load))
        elif 29 < self.health < 50:
            self.health = round(self.health - (1.0 * viral_load))

        elif self.health >= 50:
            self.health = round(self.health - (2.0 * viral_load))

        if self.health < 0:
            self.health = 0

    def get_viral_load(self):
        return 5.0 + (pow((self.health - 25.0), 2)/62.0)

    def sleep(self):
        self.health += 5
        if self.health >= 100:
            self.health = 100

    def __str__(self):
        return self.first_name + " " + self.last_name + " : " + str(self.get_health())


def run_simulation(days, meeting_probability, patient_zero_health):
    patients = load_patients(75)
    patients[0].set_health(patient_zero_health)
    contagious_count_list = []
    for day in range(days):
        # count is a variable that stores the number of contagious people
        count = 0
        for patient in patients:
            for friend in patient.get_friends():

                if random.random() <= meeting_probability:
                    if patient.is_contagious():
                        friend.infect(patient.get_viral_load())
                    if friend.is_contagious():
                        patient.infect(friend.get_viral_load())
        for patient in patients:
            if patient.is_contagious():
                count += 1
            patient.sleep()
        contagious_count_list.append(count)

    return contagious_count_list


def dict_loader(name, health):
    if name not in patient_dict:
        person_first_name = name.split(" ")[0]
        person_last_name = name.split(" ")[1]
        patient_dict[name] = Patient(person_first_name, person_last_name, health)
    return patient_dict[name]


def load_patients(initial_health):
    try:
        read_file = open("a2_sample_set.txt", "r")
        patient_list = []
        for line in read_file:
            # splitting each line
            line_splited = line.split(": ")

            patient = dict_loader(line_splited[0], initial_health)

            # adding friends
            for friend_name in line_splited[1].split(", "):
                friend_person = dict_loader(friend_name.rstrip(), initial_health)
                patient.add_friend(friend_person)

            patient_list.append(patient)
        return patient_list
    except IOError:
        print("File could not be open !, please check if file named a2_sample_set.txt exist or close file !")


if __name__ == '__main__':
    # You may add your own testing code within this main block
    # to check if the code is working the way you expect.

    #This is a sample test case. Write your own testing code here.
    #test_result = run_simulation(15, 0.8, 49)
    #print(test_result)
    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    #
    # Note: since this simulation is based on random probability, the
    # actual numbers may be different each time you run the simulation.


    # Another sample test case (high meeting probability means this will
    # spread to everyone very quickly; 40 days means will get 40 entries.)
    test_result = run_simulation(40, 1, 1)
    print(test_result)
    #sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200, 
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

    

# do not add code here (outside the main block).
