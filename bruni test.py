import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width = 300, height = 300)      
canvas.pack()
score = 0
print('Welcome to the Bruni test!')
print('Keep track of your score: there will be a key shown at the end!')
sel = input('Start? (yes):')
if sel == 'yes':
    while True:
       
        q_1 = input('Q.1: What is your favourite season? (spring/summer/fall/winter):')
        if q_1 == 'spring':
            score+=0
            print('score:',score)
            break
        elif q_1=='summer':
            score+=1
            print('score:',score)
            break
        elif q_1=='fall':
            score+=2
            print('score:',score)
            break
        elif q_1=='winter':
            score+=3
            print('score:',score)
            break
        else:
            print('ANSWER!!!')

   
    while True:
        qu = input('Q.2: Who is your favourite character in Frozen? (Elsa, Anna, Olaf, Bruni, None):')
        if qu=='Elsa' or qu=='elsa':
            score+=2
            print('score:',score)
            break
        elif qu=='Anna' or qu == 'anna':
            score+=0
            print('score:',score)
            break
        elif qu=='Olaf' or qu == 'olaf':
            score+=1
            print('score:',score)
            break
        elif qu=='bruni' or qu=='Bruni':
            score+=3
            print('score:',score)
            break
        elif qu=='none' or qu=='None':
            score+=0
            print('score:',score)
            break
        else:
            print('ANSWER!!!')
    while True:
        q_3 = input('Q.3: Daytime or Nighttime? (daytime/nighttime):')
        if q_3 == 'Daytime' or q_3 == 'daytime':
            score+=2
            print('score:',score)
            break
        elif q_3=='Nighttime' or q_3 == 'nighttime':
            score+=3
            print('score:',score)
            break
        else:
            print('ANSWER!!!')
   
    while True:
        q_4 = input('Q.4: Fire or Ice? (fire/ice):')
        if q_4 == 'fire' or q_4 == 'Fire':
            score+=2
            print('score:',score)
            break
        elif q_4 == 'ice' or q_4 == 'Ice':
            score+=3
            print('score:',score)
            break
        else:
            print('ANSWER!!!')

if q_4 == 'fire' or q_4 == 'Fire' or q_4 == 'ice' or q_4 == 'Ice':
    print('Key:')
    print('12 points: Bruni Bruni!')
    print('8-11 points: Happy Bruni!')
    print('7-4 points: Sad Bruni!')
    print('3-0 points: Mad Bruni!')

if score == 12:
    img = tk.PhotoImage(file = 'bruni_bruni.jpg')
    Lab = tk.Label(image=img)
    Lab.pack()


if 11>=score >=8:
    img = tk.PhotoImage(file = 'bruni_bruni.jpg')
    Lab = tk.Label(image=img)
    Lab.pack()
if 7>=score>=4:
    img = tk.PhotoImage(file = 'bruni_bruni.jpg')
    Lab = tk.Label(image=img)
    Lab.pack()
if 3>=score>=0:
    img = tk.PhotoImage(file = 'bruni_bruni.jpg')
    Lab = tk.Label(image=img)
    Lab.pack()
tk.mainloop()