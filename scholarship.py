eng_score = int(input('Please enter your ENGLISH score:'))
math_score = int(input('Please enter your MATH score:'))
if eng_score==100 or math_score==100:
    print('GREAT')
elif eng_score>=90 and math_score>=90:
    print('PRIZE')
elif eng_score>=60 or math_score>=60:
    print('WORK HARDER YOU DWEEB')
else:
    print('PUNISHMENT')