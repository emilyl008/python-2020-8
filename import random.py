number = int(input('Please select a number from 1-10:'))
print('The number is...')
import random
num = random.randint(1,10)
print(num)
if number==num:
    print('CORRECT')
else:
    print('TRY AGAIN')