class atmcard:
    def __init__(self,card_num,pin):
        self.card_num=card_num
        self.pin=pin
        self.balance=3000
        
    def check_balance(self):
        return self.balance
    
    def deposite(self,amount):
        self.balance += amount
        return f"Deposited amount is {self.balance}"
    
    def withdrawl(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            return f"Withdrew amount is {amount}, balance is {self.balance}"
    
    def change_pin(self,new_pin):
        self.pin=new_pin
        return "Pin has been changed successsfully"
        
card = atmcard("0010-0010-1101-1010","6361")
enterd_pin=input("Enter your pin here: ")

if(enterd_pin==card.pin):
    while True:
        print("\n Options :")
        print("1) Check balance: ")
        print("2) Deposite: ")
        print("3) Withdrawl: ")
        print("4) Change the pin: ")
        print("5) Exit: ")
        
        chooise=input("Enter your chooise(1/2/3/4/5): ")
        
        if chooise=="1":
            print(f"YOur balance is {card.check_balance()}")
            
        elif chooise=="2":
            amount=int(input("Enter the amount to be deposited:"))
            print(card.deposite(amount))
            
        elif chooise=="3":
            amount=int(input("Enter the amount to withdrawl: "))
            print(card.withdrawl(amount))
            
        elif chooise=="4":
            new_pin=int(input("Enter the new pin: "))
            print(card.change_pin(new_pin))
            
        elif chooise=='5':
            print("Thanks! Visit again")
            break
        else:
            print("Invalid chooise ")
else:
    print("You have entered a wrong pin")