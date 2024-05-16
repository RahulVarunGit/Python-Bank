from bank_accounts import *

Smith = BankAccount("Smith",1000)
Will = BankAccount("Will",2000)

Smith.deposit(1000)

Will.getBalance()
Will.withdraw(1500)
Will.withdraw(1500)

Smith.transfer(1000,Will)

Jill = InterestRewardsAcct("Jill", 1000)
Jill.deposit(100)
Jill.transfer(100,Will)

Bliss = SavingsAcct("Bliss",1000)
Bliss.withdraw(500)