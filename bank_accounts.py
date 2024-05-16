class BalanceException(Exception):
    pass

class BankAccount:
    
    def __init__(self, acctName, initialAmt):
        self.acctName = acctName
        self.acctBalance = initialAmt
        print(f"\n Account '{self.acctName}' created with balance of ${self.acctBalance:.2f}.")
    

    def getBalance(self):
        print(f"\n Account '{self.acctName}' has balance of ${self.acctBalance:.2f}.")


    def deposit(self, amt):
        self.acctBalance += amt
        print("Deposit complete.")
        self.getBalance()

    def viableTransaction(self, amt):
        if self.acctBalance < amt:
            raise BalanceException(f"\nSorry, account '{self.acctName}' has balance of only ${self.acctBalance:.2f}." )
        else:
            return
    
    def withdraw(self, amt):
        try:
            self.viableTransaction(amt)
            self.acctBalance -= amt
            print("\nWithdrawal complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdrawal Interrupted : {error}")   
        
    def transfer(self, amt, account):
        try:
            print('\n **************************** Beginning Transfer..🚀 *********************')
            self.viableTransaction
            self.withdraw(amt)
            account.deposit(amt)
            print('\n **************************** Transfer Complete..👍👍👍 *********************')
        except BalanceException as error:
            print(f"\nTransfer Interrupted : {error}")   
