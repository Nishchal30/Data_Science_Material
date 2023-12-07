class Person():

    def __init__(self, name, surname, age, email, phone): # __init__() is a constructor of Person class which will pass the data to the class.
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.phone = phone

    def __init__(self, subject, school):
        self.subject = subject
        self.school = school


# If we have to pass the data to the object of the class, only at that point __init__() is required, otherwise not required.

# so if we create two constructors, that is two __init__() methods, then the object will consider the last or the latest one, 
# it will override the first method.
        
# Nishchal = Person("Nishchal", "Jinturkar", 24, "abc@gamil.com", 4637647)
Nishchal = Person("Nishchal", "Jinturkar")
print(Nishchal.subject, Nishchal.school)

# self is just a pointer, we can use any keyword instead of self but to follow standerd coding practises, we use self.

#Example

# class Person1():

#     def __init__(abc, name, surname, age, email, phone, year_of_birth):
#         abc.name = name
#         abc.surname = surname
#         abc.age = age
#         abc.email = email
#         abc.phone = phone
#         abc.year_of_birth = year_of_birth

#     def findage(abc, current_year):

#         return current_year - abc.year_of_birth
    
        
# Nishchal1 = Person1("abc", "xyz", 20, "xyz@gamil.com", 4637647, 2010)
# print(Nishchal1.age, Nishchal1.email)

# abc = Person1("learn", "python", 34, "abjd", 7397, 1990)
# print(abc.year_of_birth)

# print(Nishchal1.findage(2022))

# # Here I have changed self with abc, again the program is running fine

