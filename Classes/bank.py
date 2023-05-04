class Account:
    amount=2500
    def __init__(self,amount,accountNumber,pin):
        self.amount=amount
        self.accountNumber=accountNumber
        self.pin=pin
    def withdraw_money(self):
        return f"I have received my {self.accountNumber}, and a {self.pin} with the {self.amount}"
    def deposit_money(self):
        return f"I have deposited {self.amount}, and {self.accountNumber} and {self.pin} "
    def check_balance(self):
        return f"With my {self.pin} and {self.accountNumber}, I can be able to check the {self.amount}"