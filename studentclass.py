''' This programs sets a student class '''


class Student:
    ''' The enemy objects are what the player fights in the game'''

    def __init__(self, name, age):
        ''' The init function is called when a new object is instantiated
            It begins and ends with two underscores '''

        # Set the name
        self._name = name

        # Set the health
        self._age = age

        # append to the enemy_list
        class_list.append(self)

    def get_name(self):
        
        #get the name
        return self._name
    
    def get_age(self):
        
        #get the age
        return self._age

class_list = []

#create a new student
Student("Jack", 5)
Student("Jill", 7)

for s in class_list:
    print(f"{s.get_name()} is {s.get_age()} old")