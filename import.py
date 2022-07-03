''' This program is for creating students into an object orientated way'''

#classes should have a capital first letter
class Student:
    '''This holds all the student objects'''
    def __init__(self, name, age, phonenumber, enrollment, classes):
        '''The init function is called when a new object is instantiated'''
        #sets name
        self._name = name
        #sets age
        self._age = age
        #sets phonenumber
        self._phonenumber = phonenumber
        #sets enrollment
        self._enrollment = enrollment
        if enrollment == True:
            #sets classes the student is in
            self._classes = classes
        else:
            self._classes = "Student has no classes"
        student_list.append(self)
 
    def get_name(self):
        ''' THis function returns the name of the student object'''
        return self._name

    def get_age(self):
        '''This is a getter function that returns the age of the student object'''
        return self._age

    def get_phonenumber(self):
        '''This is a getter function that returns the phonenumber of the student object'''
        return self._phonenumber

    def get_enrollment(self):
        '''This is a getter function that returns the enrollment of the student object'''
        return self._enrollment

    def get_classes(self):
        '''This is a getter function that returns the classes of the student object'''
        return self._classes

def display_students():
    '''This function loops through enemy_list and displays their name and health'''
    for student in student_list:
        print(f"Name: {student.get_name()}")
    print("")

def display_student(name):
    '''This function loops through enemy_list and displays their name and health'''
    for student in student_list:
        if name in student.get_name():
            print("="*30)
            print(f"Name: {student.get_name()}\nAge: {student.get_age()}\nPhone Number: {student.get_phonenumber()}\nEnrollment status: {student.get_enrollment()}\nClasses: {student.get_classes()}")
            print("="*30)
            print("")
 
def generate_students():
    '''Import students from a csv file'''
    #import the scv package to enable the program to work with a csv
    import csv
    #open the csv file, call is csvfile
    with open("myRandomStudents.csv", newline='') as csvfile:
        #use the reader() function and put the results intp a vairable called filereader
        filereader = csv.reader(csvfile)
        #loop through the csv, one row at a time
        for line in filereader:
            #for each row, we grab the classes in columns D-H and put them into a list
            #the classes can be found in line[3] to line[7]
            classes = []
            i=3
            while i in range(3,8):
                classes.append(line[i])
                i += 1
                #create a new student object
            Student(line[0],int(line[1]),line[2],True,classes)

def add_student():
    '''This function enables us to add a new student'''
    name = input("Name: ")
    age = int(input("Age: "))
    phone_number = input("Phone Number: ")
    classes = []
    enrolement = True
    ask_class = True
    while ask_class == True:
        c = input("Enter Class code (Press -1 to end): ")
        if c == "-1":
            ask_class = False
        else: 
            classes.append(c)
        
    
    Student(name, age, phone_number, classes, enrolement)

student_list = []        
generate_students()
keep_asking = True
while keep_asking:
    print(" 1. Add Student \n 2. Class Lists \n 3. Search for Students \n 4. All Students")
    selection = int(input(" : "))
    if selection == 1:
        add_student()
    elif selection == 2:
        add_student()
    elif selection == 3:
        add_student()
    elif selection == 4:
        display_students()
        
     



