score = 0
print('Welcome to the Bruni test!')
print('Keep track of your score: there will be a key shown at the end!')
sel = input('Start? (yes):')
if sel == 'yes':
    
    q1 = input('Q.1: What is your favourite season? (spring/summer/fall/winter):')
if q1 == 'spring':
    score+=0
    print('score:',score)
elif q1=='summer':
    score+=1
    print('score:',score)
elif q1=='fall':
    score+=2
    print('score:',score)
elif q1=='winter':
    score+=3
    print('score:',score)
    
if q1 == 'spring' or 'summer' or 'fall' or 'winter':
    q2 = input('Q.2: Who is your favourite character in Frozen? (Elsa, Anna, Olaf, Bruni, None):')
if q2 == 'Elsa' or 'elsa':
    score+=2
    print('score:',score)
elif q2=='Anna' or 'anna':
    score+=0
    print('score:',score)
elif q2=='Olaf' or 'olaf':
    score+=1
    print('score:',score)
elif q2=='bruni' or 'Bruni':
    score+=3
    print('score:',score)
elif q2=='none' or 'None':
    score+=0
    print('score:',score)
    
if q1 == 'elsa' or 'Elsa' or 'anna' or 'Anna' or 'olaf' or 'Olaf' or 'bruni' or 'Bruni' or 'none' or 'None':
    q3 = input('Q.3: Daytime or Nighttime? (daytime/nighttime):')
if q3 == 'Daytime' or 'daytime':
    score+=2
    print('score:',score)
elif q3=='Nighttime' or 'nighttime':
    score+=3
    print('score:',score)
    
if q3 == 'daytime' or 'Daytime' or 'nighttime' or 'Nighttime':
    q4 = input('Q.4: Fire or Ice? (fire/ice):')
if q3 == 'fire' or 'Fire':
    score+=2
    print('score:',score)
elif q3 == 'ice' or 'Ice':
    print('score:',score)
    score+=3

print('Key:')
print('12 points: Bruni Bruni!')
print('8-11 points: Happy Bruni!')
print('7-4 points: Sad Bruni!')
print('3-0 points: Mad Bruni!')