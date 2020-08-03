import random


num = random.randint(1,10)
while True:
    number = int(input('Please select a number from 1-10:'))
    if number==num:
        print('CORRECT')
        break
    else:
        print('TRY AGAIN!')