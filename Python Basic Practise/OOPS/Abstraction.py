class ineuron:

    __students = "data_science"  # Data Abstraction as here we are hiding the students variable under the class ineuron

# as the __students variable is a protected under the class hence its not directly accessible from the object also.

    def students(self):
        print("the class of students",ineuron.__students)

    
i = ineuron()
print(i._ineuron__students) 
