import logging
logging.basicConfig(filename="string_logs", level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s')


logging.info("First we will define one class for the string opeartions")


class string_operations:

#first function for string slicing

    def string_slicing(self, string):
        logging.info("1st string opeartion function")
        try:
            self.string = string
            index = int(input("enter the slicing index :"))
            logging.info("The string slicing is executed successfully")
            result1 = string[0: index]
        except Exception as e:
            print(e)
            logging.info("the error %s is", e)
        
        return result1
    
# second function for string concatenation
    logging.info("the second function for string opeartion will start here")

    def string_concat(self):
        try:
            logging.info("Here we will try to concat two strings")
            string1 = input("enter the first string :")
            string2 = input("enter the second string :")
            result2 = string1 + string2
            logging.info("The string concatenation is successfull")
        except Exception as e:
            print(e)
            logging.info("the error %s is", e)
        return result2
    

# The third function for string opeartion is count of the string
    logging.info("the third function for string opeartion will start here")

    def count_string(self, string):
        logging.info("Here we will try to count the element from the strings")
        try: 
            self.string = string
            count_str = input("enter what needs to be counted")
            result3 = string.count(count_str)
            logging.info("The count of string is successfull")
        except Exception as e:
            print(e)
            logging.info("the error %s is", e)
        return result3



          
    
first_example = string_operations()
slicing = first_example.string_slicing("Nishchal")
print(slicing)

second_example = string_operations()
concat = second_example.string_concat()
print(concat)

third_example = string_operations()
count = third_example.count_string("atufgvvjhh")
print(count)



class vehicle():

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"start the vehicle of {self.brand}")

class Bicycle(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start(self):
        super().start()
        print(f"the {self.model} is of {self.brand}")

    
a = vehicle("Tata")
a.start()

b = Bicycle("Maruti", "WaganoR")
b.start()


