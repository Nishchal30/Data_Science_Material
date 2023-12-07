class Person:

    def __init__(self, name, surname, age): 
        self.name = name
        self.surname = surname
        self.age = age

    def __init__(self, phone, email):
        self.phone = phone
        self.email = email


learn = Person(537, "aba")
print(learn.email)

#This is taking the second __int__() for the class Person, hence it is taking only two arguments in the object.

class name:

    def age(self, current_year, birth_year):
        return current_year - birth_year

    def email_input(self, email):
        print("email is : ", email)

    def ask_name(self):
        name = input("enter your name")
        return name
    
    def ask_dob(self):
        dob = input("enter the dob")
        return dob

sudh = name()
anuj = name()
gargi = name()
krish = name()

print(sudh.ask_name())
print(gargi.ask_dob())
print(gargi.age(2023, 1999))