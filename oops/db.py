import sqlite3

conn = sqlite3.connect("school.db")
c = conn.cursor()
# c.execute(
#     f"""create table users(
#         id INTEGER primary key,
#         name text not null
#     )""")

# c.execute("""
#           INSERT INTO users(id,name)
#           VALUES(1,'kebede'),
#                 (2,'john')
#           """)

# c.execute(""" 
#           UPDATE users
#           SET name = 'Kebede'
#           WHERE id = 1
#           """)

# statement = c.execute(
#     """
#     SELECT * FROM users
#     """)
# queryset = statement.fetchall()

# c.execute("""
#           DELETE FROM users
#           """)
# c.execute("""
#           DELETE FROM users
#           WHERE id = 1
#           """)

# statement = c.execute(
#     """
#     SELECT * FROM users
#     WHERE id = 1
#     """)

# queryset = statement.fetchone()

# for row in queryset:
#     print(row[1])

# for id,name in queryset:
#     print(name)

# print(queryset)


# c.execute("""
#           CREATE TABLE courses(
#               id INTEGER PRIMARY KEY,
#               title TEXT NOT NULL,
#               price REAL DEFAULT 0,
#               user_id INTEGER NOT NULL,
#               FOREIGN KEY(user_id) REFERENCES users(id)
#           );
#           """)

# c.execute("""
#           INSERT INTO courses(id, title,user_id)
#           VALUES(1,'Python',1),
#                 (2,'JavaScript',1)
#           """)

# c.execute("""
#           UPDATE courses
#           SET price = 10
#           WHERE id = 1
#           """)
# statement = c.execute("""
#           SELECT * FROM courses
#           """)
# # queryset = statement.fetchmany(2)
# queryset = statement.fetchall()

statement = c.execute("""
          SELECT u.name, c.title,c.price
          FROM users u
          JOIN courses c
                    ON u.id = c.user_id
          ORDER BY c.price ASC
          """)
queryset = statement.fetchall()
print(queryset)
conn.commit()

# class User:
#     def __init__(self,id:int,name:str) -> None:
#         self.__id = id
#         self.__name = name

# user = User(1,"dskjghad")
