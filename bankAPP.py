##bankAPP

import sys

class Customer:
    ''' Customer class with Bank related operations '''
    bankname = 'BriceEBANKING'

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("After deposit, your new balance is: ", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds! Sorry, cannot perform this operation!")
            sys.exit()
        else:
            self.balance = self.balance - amount
            print("After withdrawal, your new balance is: ", self.balance)

print("Welcome to ", Customer.bankname)
name = input("Enter your full name: ")
c = Customer(name)
while True:
    print ("d-Deposit \n w-Withdrawal \n e-Exit")
    option = input("Choose your option: ")

    if option == "d" or option == "D":
        amount = float(input("Make a Deposit: "))
        c.deposit(amount)

    elif option == "w" or option == "W":
        amount = float(input("How much would you like to withdraw? "))
        c.withdraw(amount)

    elif option == "e" or option == "E":
        print("Thanks for banking with us! We hope to see you soon! ")
        sys.exit()

    else:
        print("Entry invalid! Please choose a valid option!")





