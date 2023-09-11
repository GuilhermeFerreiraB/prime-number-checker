number = int(input("Write a number, please: "))
counter = 0
for divisor in range(1, number + 1):
    if number % divisor == 0:
        counter += 1
if counter == 2:
    print('The number written is a prime number.')
else:
    print('The number written is not a prime number.')
