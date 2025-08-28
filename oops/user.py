
# class User:
#     object_count = 1
#     def __init__(self,id:int,name) -> None:
#         self.__id = id
#         self.__name = name
    
#     def __str__(self) -> str:
#         return self.__name
    
#     # def __repr__(self) -> str:
#     #     return f"User {self.__id,self.__name}"
# User.object_count = 2
# user = User(1,"John")

# print(user)
# print(User.object_count)
    
# user2 = User(2,"Smith")
# print(user2.object_count)

class Person:
    def __init__(self,first_name:str,last_name:str) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
    
    # Mutator(change(setter))
    def set_first_name(self,first_name:str)->None:
        self.__first_name = first_name
    
    # Accessor(getter)
    def get_first_name(self):
        return self.__first_name
    
    def set_last_name(self,last_name):
        self.__last_name = last_name
        
    def get_last_name(self):
        return self.__last_name
    
    def get_full_name(self)->str:
        return f"{self.__first_name} {self.__last_name}"
    
    def __str__(self) -> str:
        return f"{self.__first_name} {self.__last_name}"

# p = Person("John","Smith")
# # p.set_first_name("Alex")

# print(p.get_full_name())

class Student(Person):
    def __init__(self, id:int, first_name: str, last_name: str) -> None:
        super().__init__(first_name, last_name)
        self.__id = id
    
    def get_full_name(self) -> str:
        # return "Student " + super().get_full_name()
        return f"Student {self.get_first_name()} {self.get_last_name()}"


# s = Student(1,"Alex","Kebede")
# s.set_first_name("John")
# print(s.get_full_name())

class Teacher(Person):
    def __init__(self,id, first_name: str, last_name: str) -> None:
        super().__init__(first_name, last_name)
    
    def get_full_name(self) -> str:
        return "Teacher " + super().get_full_name()

t = Teacher(1,"Mr.X","Mr.Y")
print(t.get_full_name())