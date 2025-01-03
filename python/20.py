class bankAcc:
    def __init__(self,num,name,typ,balance):
        self.account_no=num
        self.name=name
        self.type=typ
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("current balance : ",self.balance)
    def withdraw(self,amount):
        if self.balance<amount:
            print("insufficient balance")
        else:
            self.balance-=amount
            print("current balance : ",self.balance)
    def details(self):
        print("Name : ",self.name,"\nAccount no : ",self.account_no,"\nAccount Type : ",self.type,"\nBalance : ",self.balance)
ac_name=bankAcc(1234,"Afraq","Savings",100000)
while(1):
    choice=int(input("1.Show details\n2.withdraw\n3.Deposit\n4.Exit\nEnter what to do : "))
    if choice==1:
        ac_name.details()
    if choice==2:
        amount=int(input("Enter amount to withdraw : "))
        ac_name.withdraw(amount)
    if choice==3:
        amount=int(input("Enter amount to deposit : "))
        ac_name.deposit(amount)
    if choice==4:
        break
    
