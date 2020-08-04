a = int(input('How many students are in the class?'))
list_score = []
for i in range(a):
    score = int(input('Please enter test scores:'))
    if score not in list_score:
        list_score.append(score)
sum_score = sum(list_score)
print('Average score for class:',sum_score/a)
highest = 0
for n in list_score:
    if n>highest:
        highest = n
print('Highest score for class:',highest)
lowest = 100
for n in list_score:
    if n<lowest:
        lowest = n
print('Lowest score for class:',lowest)         