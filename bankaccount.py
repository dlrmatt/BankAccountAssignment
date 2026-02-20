import random

#This is our main bank account class
class bankAccount:
    #This is the class attribute that holds the name of the bank.
    bankName = ""

    #These are the instance attributes that hold information about the specific account (such as balance, customer name, etc)
    customerBalance = 0.00
    customerName = ""
    minimumBalance = 0.00

    #protected and private variables both with random 10 digit routing and account numbers
    _accountNumber = random.randint(1000000000, 9999999999)
    __routingNumber = random.randint(1000000000, 9999999999)

    #This method deposits money into the bank account
    def deposit(self, amount):
        self.customerBalance += amount
        print(self.customerName + " deposited " + str(amount))

    #This method withdraws money from the bank account but only after checking if the balance remaining in the account would be above the minimum balance
    def withdraw(self, amount):
        if self.minimumBalance < (self.customerBalance - amount):
            self.customerBalance -= amount
            print(self.customerName + " withdrew " + str(amount))
        else:
            print(self.customerName + " tried to withdraw " + str(amount) + ". Balance was low and the transaction failed.")

    #This method prints out all the attributes (class and instance) for the user to view
    def printAccountInfo(self):
        print("Bank: " + self.bankName)
        print("Name: " + self.customerName)
        print("Balance: " + str(self.customerBalance))
        print("Minimum Balance: " + str(self.minimumBalance) + "\n")
