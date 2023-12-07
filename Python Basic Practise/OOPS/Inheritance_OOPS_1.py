# importing the class and function from different file to the curret file
# this method is called as package and modules

from Constructor__OOPS import name

obj1 = name()
print(obj1.age(2023,1999))



class Person:

# Its not necessary to create variables for a class in constructor __init__() 
# because if we do so, then we need to pass that values of the cariable at the time of object creation

    _name = "Nishchal"
    __surname = "Jinturkar"
    birth_year = 1999


    def _age(self, current_year):  # Protected function with single underscore
        return current_year - self.birth_year    
    

    def __age1(self, current_year): # Private function with double underscore
        return current_year - self.birth_year   

obj_person = Person()
print(obj_person)
print(obj_person._age(2023)) # Function calling is same as the variables
print(obj_person._Person__age1(2023))


# Inheritance

class employee(Person):
    _name = "abc"
    __surname = "xyz"
    birth_year = 1938

obj_employee = employee()
print(obj_employee)
print(obj_employee._age(2023)) # we can access functions and variables of one class inside the different class
print(obj_employee._Person__age1(2023)) # we can access even private and protected functions and variables of one class inside the different class
print(obj_employee.birth_year)
print(obj_employee._name)
print(obj_employee._Person__surname)
print(obj_employee._employee__surname)