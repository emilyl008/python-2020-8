a = int(input('How many students are there?'))
list_score = []
name = []

for i in range (a):
    name_input = input('Please enter student name:')
    score = int(input('Please enter test score:'))
    list_score.append(score)
    name.append(name_input)
    
sum_score = sum(list_score)
print('Class average:',sum_score/a)

highest = 0
for n in range(a):
    if list_score[n]>highest:
        highest = list_score[n]
        high_name = name[n]
print('Highest test score:',highest,high_name)

lowest = 100
for n in range(a):
    if list_score[n]<lowest:
        lowest = list_score[n]
        low_name = name[n]
print('Lowest test score:',lowest,low_name)