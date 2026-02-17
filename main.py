#Matt and Wesley
#Bank Account Assignment

#This is our main bank account class
class bankAccount:
    #This is the class attribute that holds the name of the bank.
    bankName = ""

    #These are the instance attributes that hold information about the specific account (such as balance, customer name, etc)
    customerBalance = 0.00
    customerName = ""
    minimumBalance = 0.00

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

    #This method prints out all of the attributes (class and instance) for the user to view
    def printAccountInfo(self):
        print("Bank: " + self.bankName)
        print("Name: " + self.customerName)
        print("Balance: " + str(self.customerBalance))
        print("Minimum Balance: " + str(self.minimumBalance) + "\n")

#Savings Account Subclass
class savingsAccount(bankAccount):
    interestRate = 0.00

#Initilizing account and printing account1 information
account1 = bankAccount()
account1.bankName = "UNCC Bank"
account1.customerBalance = 100.00
account1.customerName = "Account1 Owner"
account1.printAccountInfo()

#Testing withdraw and printing account1 information
account1.withdraw(50.00)
account1.printAccountInfo()

#Testing deposit and printing account1 information
account1.deposit(50.00)
account1.printAccountInfo()

#Testing withdraw validation and printing account1 information
account1.withdraw(101.00)
account1.printAccountInfo()

#Initilizing account and printing account2 information
account2 = bankAccount()
account2.bankName = "Bank of UNCC"
account2.customerBalance = 100.00
account2.customerName = "Account 2 Owner"
account2.printAccountInfo()

#Testing withdraw and printing account2 information
account2.withdraw(50.00)
account2.printAccountInfo()

#Testing deposit and printing account2 information
account2.deposit(50.00)
account2.printAccountInfo()

#Testing withdraw validation and printing account2 information
account2.withdraw(101.00)
account2.printAccountInfo()
