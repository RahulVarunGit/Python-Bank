from bank_accounts import *

Smith = BankAccount("Smith",1000)
Will = BankAccount("Will",2000)

Smith.deposit(1000)

Will.getBalance()
Will.withdraw(1500)
Will.withdraw(1500)

Smith.transfer(1000,Will)