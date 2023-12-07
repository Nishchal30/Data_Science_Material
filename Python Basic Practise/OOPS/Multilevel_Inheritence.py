class Bank:   #Parent class
    
    def transaction(self):
        print("this will show you your transaction status")

    def account(self):
        print("this will show you your account status")

    def deposit(self):
        print("this will show you your deposit status")

    
class HDFC_Bank(Bank):  # Child class
    
    def hdfc_to_icici(self):
        print("this will show the status of hdfc to icici")

    
class ICICI_Bank(HDFC_Bank):  # Multi-level Inheritence (HDFC is child of Bank and we are calling both classes in this class)
    pass

i = ICICI_Bank()
i.hdfc_to_icici()
i.deposit()