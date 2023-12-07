class Person1:

    def __init__(self, name, surname, birth_year):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year


Nish = Person1("Nishchal","Jinturkar",1999)
print(Nish.name)

#Intitially all the variables we declare are public variable, means we can use that variables anywhere we want.

# But if use singe underscore  _before variable name then that variable becomes protected variable

# But if use double underscore  __before variable name then that variable becomes private variable

class Person2:

    def __init__(self, name, surname, birth_year):
        self._name = name # single underscore is protected variable
        self.__surname = surname  ## double underscore is private variable
        self._birth_year = birth_year


Nish = Person2("ab c","xyz",1978)
print(Nish._name)
print(Nish._Person2__surname) # At the time of calling private variable, need to add a _class name before private variable.

# but don't use the private function or variable directly , we should define a public method to access the private methods


class student:

    def __init__(self, name, roll):

        self.__name = name
        self.__roll = roll

    def __display(self):
        print(f"name of student is {self.__name} and roll no is {self.__roll}")


student1 = student("abc", 21)
# student1.__display() # we cannot access it directly but we can access it by below methodw which is wrong
student1._student__display() # there is problem in accessing like this, is we can override the value of private class by using this

student1._student__name = "xyz"
student1._student__display()

# here we have overriden the value of private variable using this method so we should always follow the below method

class student1:

    def __init__(self, name, roll):

        self.__name = name
        self.__roll = roll

    def __display(self):
        print(f"name of student is {self.__name} and roll no is {self.__roll}")

    def display(self):  # Use a public method to display a private method
        self.__display()

student2 = student1("abc", 51)
student2.display() # call a public method instead of private method from object of class

        