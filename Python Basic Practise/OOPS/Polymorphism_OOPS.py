class ineuron:

    def student(self):
        print("this will show the students details")
    

class class_type:

    def student(self):
        print("this will show the class type of students")


def ineuron_external(a):
    a.student()


i = ineuron()
c = class_type()
ineuron_external(i) # this will give the output for ineuron class method as i is object of ineuron class
ineuron_external(c) # this will return the output for class type class as c is object of class type class.

# exa: Polymorphism

# the behaviour of a function on changing the variable values.

def test(a, b): # this function is of addition for integer values and concatenation for string values
    return a + b

#print(test(3,4))
#print(test("ab", "cd"))


class Animal:
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def make_sound(self):
        return "generic voice"
    
class Dog(Animal):

    def make_sound(self):
        return "Woof"
    
class cat(Animal):
    
    def make_sound(self):
        return "meow"
    
    
cat = cat("cat")
an = Animal("cow")