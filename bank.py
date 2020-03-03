from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
	@abstractmethod
	def createAccount():
		return 0
	@abstractmethod
	def authenticate():
		return 0
	@abstractmethod
	def withdrawl():
		return 0
	@abstractmethod
	def deposit():
		return 0
	@abstractmethod
	def displayBalance():
		return 0

class SavingsAccount:
	def __init__(self):
		self.SavingsAccount = {}
	def createAccount(self, name, initialDeposit):
		self.accountNumber = randint(10000, 99999)
		self.SavingsAccount[self.accountNumber] = [name, initialDeposit]
		print("account creation has been sucessful. your account number is ", self.accountNumber)
		pass
	def authenticate(self, name, accountNumber):
		if accountNumber in self.SavingsAccount.keys():
			if self.SavingsAccount[accountNumber][0] == name:
				print("authentication sucessful")
				return True
			else:
				print("authentication failed")
				return False
		else:
			print("authentication failed")
			return False
		
	def withdraw(self, withdrawlAmount):
		if withdrawlAmount > self.SavingsAccount[self.accountNumber][1]:
			print("Insufficient balance")
		else:
			self.SavingsAccount[self.accountNumber][1] -= withdrawlAmount
			print("withdrawl was sucessful. Available balance: ")
			self.displayBalance()
		pass
	def deposit(self, depositAmount):
		self.SavingsAccount[self.accountNumber][1] += depositAmount
		print("deposit was sucessful. Available balance: ")
		self.displayBalance
		pass
	def displayBalance(self):
		print("Available balance: ",self.SavingsAccount[self.accountNumber][1])
		pass

savingsAccount = SavingsAccount()
while True:
	print("Enter 1 to create a new account")
	print("Enter 2 to access an existing account")
	print("Enter 3 to exit")
	userChoice = int(input())
	if userChoice == 1:
		print("Enter your name: ")
		name = input()
		print("enter the initial deposit: ")
		deposit = int(input())
		savingsAccount.createAccount(name, deposit)
	elif userChoice == 2:
		print("Enter your name: ")
		name = input()
		print("enter the account number: ")
		accountNumber = int(input())
		authenticationStatus =  savingsAccount.authenticate(name, accountNumber)
		if authenticationStatus == True:
			while True:
				print("Enter 1 to withdraw from a created account")
				print("Enter 2 to deposit into the created account")
				print("Enter 3 to display available balance of the account")
				print("enter 4 to go back to the previous menu")
				userChoice = int(input())
				if userChoice == 1:
					print("Enter a withdrawl amount")
					withdrawlAmount = int(input())
					savingsAccount.withdraw(withdrawlAmount)
				elif userChoice == 2:
					print("Enter an amount to be deposited")
					depositAmount = int(input())
					savingsAccount.deposit(depositAmount)
				elif userChoice == 3:
					savingsAccount.displayBalance()
				elif userChoice == 4:
					break
	elif userChoice == 3:
		quit()



		