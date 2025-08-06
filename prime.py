
number = int(input("Number: "))

prime_count = 0
for x in range(1,number + 1):
    if number % x  == 0:
        prime_count += 1

if prime_count == 2:
    print(F"{number} is prime!")
else:
    print(F"{number } is not prime!")