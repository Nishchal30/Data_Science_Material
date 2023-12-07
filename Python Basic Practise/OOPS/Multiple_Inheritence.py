class Bank:  
    
    def transaction(self):
        print("this will show you your transaction status")

    def account(self):
        print("this will show you your account status")

    def deposit(self):
        print("this will show you your deposit status")

    def test(self):
        print("this is the test method from bank class")

    
class HDFC_Bank: 
    
    def hdfc_to_icici(self):
        print("this will show the status of hdfc to icici")

    def test(self):
        print("this is the test method from HDFC Bank class")

    
class ICICI_Bank(Bank, HDFC_Bank): # Multiple classes inherited to a new class and all the functions are accessible from the new class
    
    def icici(self):
        print("this will show the status of your icici account")

i = ICICI_Bank()
i.hdfc_to_icici()
i.deposit()
i.test()

# If we use exactly same functions in both classes from which we have inherited a new class, then it will take
# a function from the first class only

# exa here from bank class it is taking test function

    
