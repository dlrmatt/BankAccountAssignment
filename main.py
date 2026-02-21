#Matt and Wesley
#Bank Account Assignment
import random
from bankaccount import bankAccount
from checkingaccount import checkingAccount
from savingsAccount import savingsAccount

#Customer opens account
account1 = bankAccount()
account1.bankName = "UNCC Bank"
account1.customerBalance = 100.00
account1.customerName = "Account1 Owner"
account1.printAccountInfo()

#Customer and printing account1 information
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
