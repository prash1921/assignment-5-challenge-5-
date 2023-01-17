class account:
 def __init__(self,title=none,balance=0):
  self.title=title
  self.balance=balance
def withdrawl(self,amount):
    amount= float(input("enter amount to be withdrawn:"))
    if self.balance >= amount:
        self.balance -=amount
        print("you withdraw :",amount)
    else:
            print("insufficient balance")
            def display(self):
                print("net available balance =",self.balance)
                pass
def deposit(self,amount):
    amount=float(input("enter amount to be deposited:"))
    self.balance +=amount
    print("amount deposited:",amount)
    pass
def get_balance(self):
 print("getter method called")
 return self._balance
 pass
 class savingsaccount(account):
    def__init__(self,title=none,balance=0,interestrate=0)
    super().__init__(titlt,balance)
    self.interestrate=interestrate
    def interestamount(self):
        balance=startbalance
        interestamount=interestrate * balance/100
        pass
    s=account
    s.deposit()
    s.withdraw()
    s.display()

        



