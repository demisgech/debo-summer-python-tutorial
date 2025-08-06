
# Control flow summary
# if-ese
# if-elif-else
# match...case
# ternary operator(conditional operator)
# loop(for and while)
# continue and break

# for, while

# for x in range(20):
#     if x % 2 == 1:
#         print(x)

import math
print("X\tX^2\tx^3\t\\/x")
for x in range(30):
    print("_",end="")
print()
for x in range(11):
    print(F"{x}\t{math.pow(x,2)}\t{math.pow(x,3)}\t{round(math.sqrt(x),2)}")