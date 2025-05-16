# Class Methods and Static Methods

class Employee:
    # Class variable
    company_name = "Tech Solutions"
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def show_employee_count(cls):
        print(f"Total employees: {cls.employee_count}")

# Creating instances
emp1 = Employee("Amit", 50000)
emp2 = Employee("Lalit", 60000)

# Calling class method
Employee.show_employee_count()

class BankAccount:
    bank_name="State Bank of India"

    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def show_details (self):
        print(f"Account holder name is {self.account_holder} and his bank balance is {self.balance}")

    def deposit(self,amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully!")
        print(f"Updated balance :-{self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance! Withdrawal failed.\n")
        else :
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")
            print(f"Updated balance :₹{self.balance}")

    @classmethod
    def show_bank_name(cls):
        print(f"The bank name is :- {cls.bank_name}")

    @staticmethod
    def bank_polices ():
        print("Minimum balance should be ₹1000.")
        print("Withdrawal limit is ₹50000.")
# Creating Object
Bank1=BankAccount("Amit Mohan",250000)
Bank2=BankAccount("Lalit Mohan",150000)

#Transaction
Bank1.deposit(5000)
Bank1.show_details()
Bank1.withdraw(10000)
Bank1.show_details()

Bank2.deposit(10000)
Bank2.show_details()
Bank2.withdraw(16000)
Bank2.show_details()

BankAccount.show_bank_name()
BankAccount.bank_polices()




