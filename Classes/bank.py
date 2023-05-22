class Account:
    def __init__(self, amount, accountNumber, pin, balance):
        self.amount = amount
        self.accountNumber = accountNumber
        self.pin = pin
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0


    def deposit_money(self, amount):
        self.balance += amount
        return f"I have deposited {amount}, and your new balance is {self.balance} "

    def withdraw_money(self):
        if self.balance <= self.amount:
            self.balance -= self.amount
            return f"your withdraw {self.amount}, and the balance is {self.balance}"
        else:
            self.balance - self.amount
        return self.balance

    def check_balance(self):
        return f"With my {self.pin} and {self.accountNumber}, I can be able to check the {self.amount}"
    

    def check_balance(self):
        return f"Your account balance is {self.balance} Ksh."
    
    def deposit(self, amount):
        self.balance += amount
        transaction = {"amount":amount, 
                       "narration": "deposit"}
        self.deposits.append(transaction)
        return "Deposit Successful"
    


        def borrow_loan(self, amount):
         if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10:
            total_deposits = sum(transaction["amount"] for transaction in self.deposits)
            if amount <= (total_deposits / 3):
                self.loan_balance += amount
                print("Loan successfully borrowed.")
            else:
                print("Amount requested exceeds borrowing limit.")
         else:
            print("Loan request not eligible.")

         def repay_loan(self, amount):
           if amount <= self.loan_balance:
            self.loan_balance -= amount
            print("Loan repayment successful.")
           else:
            overpayment = amount - self.loan_balance
            self.loan_balance = 0
            self.balance += overpayment
            print(f"Loan fully repaid with an overpayment of {overpayment}.")

        def transfer(self, amount, target_account):
           if self.balance >= amount:
            self.balance -= amount
            target_account.deposit(amount)
            print("Transfer successful.")
           else:
            print("Insufficient balance for transfer.")

    


# account1 = Account(34567, 123345, 89000, "mama")

my_account = Account(100, "123456789", "1234", 1000)
my_account.withdrawals(200)
print(my_account.deposit_money(4560))
print(my_account.withdrawals)
my_account.borrow_loan(500)

account1 = Account(100, "123456789", "1234", 1000)
account2 = Account(200, "987654321", "4321", 500)
account1.transfer(300, account2)

