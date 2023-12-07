class ineuron:

    def student(self):
        print("this will show the information of students")

    def achievers(self):
        print("this will display the info of achievers")

    def Hall_of_fame(self):
        print("this will show info of hall of fame students")

    

class ineuron_vision(ineuron):

    def student(self):  # Method overriding as we have override the student class in child class from the parent class  
        print("this will be the students list from ineuron vision class")

iv = ineuron_vision()
iv.student()