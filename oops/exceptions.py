
class AccountLocked(Exception): ...

class NetworkError(Exception): ...

def get_account(name=None):
    if name == None:
        raise AccountLocked("Account locked!!")
    
file = ""
try:
    # result = 10 / 0
    # print(result)
    # file
    # value = int(input("Value: "))
    file = open("hello.txt")
    # get_account()
   

# except AccountLocked as ex:
#     print(ex)
# except ZeroDivisionError:
#     print("Cannot divide number with 0.")

# except ValueError as v:
#     print("Value cannot be converted!!!")

except (ZeroDivisionError,ValueError) as err:
    print(err)

except Exception as ex:
    print(ex)
else:
    print("No exception happened")
    
finally:
    print("File Closed")
    file.close()

print("Done!")