
class ExpenseTrackerController:
    def __init__(self,expenses:list[dict]=[]) -> None:
        self.__expenses = [*expenses]
    
    def add_expense(self, expense:dict):
        expense = {
            'id':len(self.__expenses) + 1,
            'name':expense['name'],
            'amount':expense['amount']
        }
        self.__expenses = [*self.__expenses,expense]
    
    def remove_expense(self,id:int):
        self.__expenses = [expense for expense in self.__expenses if expense['id'] != id]
    
    def get_total_expense(self)->float:
        return sum([expense['amount'] for expense in self.__expenses])
    
    def search(self,name:str)->list[dict]:
        return [expense for expense in self.__expenses if expense['name'].lower() == name.lower()]
    
    def sort(self):
        self.__expenses = sorted(self.__expenses,key=lambda expense: expense['name'])
    
    def show_expense(self):
        for expense in self.__expenses:
            print(f"{{ id: {expense['id']}, name: {expense['name']}, amount: {expense['amount']} }}")

tracker = ExpenseTrackerController([
    {'id':1,"name":"a",'amount':10.99},
    {'id':2,"name":"c","amount":20.78}
    ])

print("""***** WELCOME TO EXPENSE TRACKER SYSTEM ****
1. Add
2. Remove
3. Show
4. Get Total
5. Search
6. Sort
7. Exit
""")
while True:
    option = input("Option: ")
    match option:
        case '1':
            name = input("Name: ")
            amount = float(input("Amount: "))
            tracker.add_expense({"name": name,"amount":amount})
        case '2':
            id = int(input("Id: "))
            tracker.remove_expense(id)
        case '3':
            tracker.show_expense()
        case '4':
            print(f"Total Expense: ${tracker.get_total_expense()}")
        case '5':
            name = input("Name: ")
            print(tracker.search(name))
        case '6':
            tracker.sort()
        case '7':
            print("Thank you for using our app!!")
            break
        case _:
            print("Please try again!!")