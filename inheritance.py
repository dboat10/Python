# Date: September 18th, 2022
# Description: Checking and Savings account child classes taking on the properties of the parent class Bank Account.
# Comment: This has been a hard challenge for me. It took me a lot of tweaking to be able to fix my code to not deduct
# the $5 fee if initial balance is greater than $50.

# This is the parent class with its attributes and methods. These are the properties which will be inherited by the
# subclasses CheckingAccount and SavingsAccount.
class BankAccount:
    def __init__(self, account_number, balance):
        if balance < 0:
            raise ValueError('Insufficient balance')
        self._account_number = account_number
        self._balance = balance

    def withdrawal(self, amount):  # This is a method that will be inherited by the subclasses
        if amount < 0:
            raise ValueError('Cannot withdraw a negative amount.')
        if amount < self._balance:
            raise ValueError('Dont have sufficient balance.')
        self._balance -= amount

    def deposit(self, amount):  # This is a method that will be inherited by the subclasses
        if amount < 0:
            raise ValueError('Deposit amount is negative')
        self._balance += amount

    def get_balance(self):  # This is a method that will be inherited by the subclasses
        return self._balance


# Subclass CheckingAccount takes on the properties of the parent class BankAccount. To create a subclass, you use the
# built-in keyword class, the class name then the parent class name in parentheses.
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, fees, minimum_balance):
        super().__init__(account_number, balance)  # This line initializes additional attributes to the subclass.
        self._fees = fees
        self._minimum_balance = minimum_balance
        if self._minimum_balance:
            self.deduct_fees()

    def deduct_fees(self):  # Additional methods belonging to the subclass CheckingAccount
        print('${} deducted for not maintaining sufficient balance'.format(self._fees))
        self._balance -= self._fees

    def CheckMinimumBalance(self):  # Additional methods belonging to the subclass CheckingAccount
        return self.get_balance() < self._minimum_balance

    def withdraw(self, amount):
        super().withdraw(amount)

        if self.CheckMinimumBalance():
            self.deduct_fees()

    def __str__(self):
        return 'Account Number: {}, Current Balance: ${:.2f}'.format(self._account_number, self.get_balance())


# Subclass SavingsAccount takes on the properties of the parent class BankAccount. To create a subclass, you use the
# built-in keyword class, the class name then the parent class name in parentheses.
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)  # This line initializes additional attributes to the subclass.
        self._interest_rate = interest_rate

    def addInterest(self):  # Additional methods belonging to the subclass SavingsAccount
        interest = self.getBalance * self._interest_rate / 100
        self.deposit(interest)


# This is where the actual program runs, all the functions abd other aspects of the program are called from the main.
def main():
    acct_number = input('Enter checking account number: ')
    balance = float(input('Enter checking account initial balance: '))
    minimum_balance = 50
    fees = 5
    try:
        if balance < minimum_balance:
            check_account = CheckingAccount(acct_number, balance, fees, minimum_balance)
            print(check_account)
        if balance > minimum_balance:
            print('You have sufficient balance for withdrawal')
    except Exception as e:
        print(str(e))


main()

