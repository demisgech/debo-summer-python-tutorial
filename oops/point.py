
#Class => Blueprint
from random import choice


class Point:
    x = 0
    y = 0
    
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Drawing a point at {self.x,self.y}")
    
#Object => Instance
# point1 = Point(1,2)

# # print(point1.x)
# point1.draw()

# point2 = Point(3,4)
# # print(point2.x)
# point2.draw()


class Rectangle:
    def __init__(self,width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height
        
    
# rectangle = Rectangle(4,3)
# print(rectangle.get_area())

class ATM:
    def __init__(self,balance=0) -> None:
        self.__balance = balance
    
    def deposit(self,amount:float)->None:
        if amount <= 0:
            print("Sorry!! Amount must be positive!!")
            return None
        
        self.__balance += amount
        print(f"You've deposited ${amount}")
    
    def withdraw(self,amount:float)->None:
        if amount <= 0:
            print("Sorry!! Amount must be positive!!")
            return None
        if amount > self.__balance:
            print("Insufficient Funds!!")
            return None
        
        self.__balance -= amount
        print(f"You've withdrew ${amount}")
    
    def check_balance(self):
        print(f"Balance: ${self.__balance}")
    
    
atm = ATM()

print("ATM Menu:")
print("""
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
      """)

while True:
    choice = input("Choice: ")
    match choice:
        case "1":
            amount = float(input("Amount: "))
            atm.deposit(amount=amount)
        case "2":
            amount = float(input("Amount: "))
            atm.withdraw(amount=amount)
        case "3":
            atm.check_balance()
        case "4":
            print("Thanks for using out app!!!")
            break
        case _ :
            print("Invalid Choice!!!")

