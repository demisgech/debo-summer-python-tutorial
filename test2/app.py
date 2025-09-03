
from typing import Union
from functools import reduce

class ExpenseTracker:
    def __init__(self,expense:list[dict] = []) -> None:
        self.__expenses = [*expense]
    
    def add_expense(self,expense:dict)->None:
        self.__expenses.append(expense)
    
    def remove_expense(self,id:int):
        self.__expenses = list(filter(lambda expense:expense['id'] != id,self.__expenses))
    
    def show_expense(self):
        for expense in self.__expenses:
            print(f"{{id: {expense['id']}, name: {expense['name']}, amount: {expense['amount']}}}")
    
    def get_total_expense(self):
        return reduce(
            lambda acc,cur: acc + cur,
            list(map(lambda expense: expense['amount'],self.__expenses)))
    
    def search_expense(self,name:str)->list[dict]:
        result = list(filter(lambda expense: expense['name'].lower() == name.lower(),self.__expenses))
        return result
        
    
# expense_tracker = ExpenseTracker()
# expense_tracker.add_expense({"id":1, "name":"Electronics","amount":10})
# expense_tracker.add_expense({"id":2, "name":"Appliances","amount":20})
# expense_tracker.show_expense()

# expense_tracker.remove_expense(2)
# print("After removed")
# expense_tracker.show_expense()
# total = expense_tracker.get_total_expense()
# print(f"Total Expense: {total}")

# print(f"search result: {expense_tracker.search_expense("electronics")}")

import sqlite3

def note_app():
    conn = sqlite3.connect("note_app.db")
    db = conn.cursor()
    db.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NULL,
                email TEXT NOT NULL UNIQUE
            );
            """)
    # db.execute('''
    #            INSERT INTO users(name,email)
    #            VALUES('yohannis','yohannis@domain.com');
    #            ''')

    # db.execute("""
    #            UPDATE users SET name = 'John'
    #            WHERE email = 'john@domain.com'
    #            """)

    # db.execute("""
    #            DELETE FROM users
    #            WHERE email = 'john@domain.com';
    #            """)

    # statement = db.execute("""
    #            SELECT * FROM users
    #            """)
    # queryset = statement.fetchall()
    # for (id,name, password, email) in queryset:
    #     print(name, email)

    db.execute("""
            CREATE TABLE IF NOT EXISTS notes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                CONSTRAINT users_fk FOREIGN KEY(user_Id) REFERENCES users(id)
            )
            """)

    # db.execute("""
    #            INSERT INTO notes(title,description,user_id)
    #            VALUES('My first note','My first note description',1);
    #            """)

    statement = db.execute("""
            SELECT u.name, u.email, n.title,n.description FROM users u
            JOIN notes n ON u.id = n.user_id
            """)
    queryset = statement.fetchall()
    print("Name\t\t Email\t\t\ttitle\t\tdescription")
    for name,email,title,description in queryset:
        print(F"{name}\t{email}\t{title}\t{description}")
        
    conn.commit()

note_app()