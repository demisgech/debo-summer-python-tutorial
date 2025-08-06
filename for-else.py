# For ... else
# While ... else

success = False

# for x in range(1,4):
#     print(F"Attempt {x}")
#     if success:
#         break
# else:
#     print("Sending message failed")

success = True
x = 1
while x <= 3:
    print(F"Attempt {x}")
    x += 1
    if success:
        break
else:
    print("Sending message failed")
    