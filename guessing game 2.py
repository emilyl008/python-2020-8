import random
a = 1
b = 100
num = random.randint(1,100)

while True:
    print('Current range %d-%d'%(a,b))
    ans = int(input('Please enter a number:'))
    if ans<a or ans>b:
        print('Please enter a number within range.')
    elif ans>num:
        b = ans
    elif ans<num:
        a = ans
    elif ans==num:
        print('SCORE!')
        break