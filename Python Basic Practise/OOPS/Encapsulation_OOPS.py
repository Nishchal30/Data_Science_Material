class ineuron:

    def __init__(self):
        self.student = "data_science"

    def students(self):
        print(self.student)

    
i = ineuron()
#i.students()
i.student = "data analytics" # Overriding the variable of the class by assigning new values in object calling
#i.students()


class ineuron1:

    def __init__(self):
        self.__student1 = "data_science"

    def students(self):
        print(self.__student1)

    def student_change(self):
        self.__student1 = "data engineer new"
    
    def student_change_2(self, new_value):
        self.__student1 = new_value

    
i1 = ineuron1()
i1.students()
i1.__student1 = "data engineer" # if the variable is private inside the class, we cannot override its value in object calling
i1.students()
i1.student_change()
i1.students()
i1.student_change_2("data enginner") # for that we need to create a method and assign a new value to that same variable
i1.students() # and then we can call again the same method where that variable is used