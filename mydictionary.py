import os.path
    
dic = {}

if not os.path.isfile('mydictionary.txt'):
    fo = open('mydictionary.txt','w')
    print('new file')
else:
    fo = open('mydictionary.txt','r')
    print('old file')
    
for row in fo.readlines():
    data = row.split(':')
    
    key = data[0]
    value = data[1]
    value = value.strip()
    
    dic[key]=value
print(dic)

fo.close()

while True:
    print('1. Set up vocabulary')
    print('2. Print all data')
    print('3. Translate English to Chinese')
    print('4. Translate Chinese to English')
    print('5. Learning test')
    print('6. Exit system')
    
    sel = input('Please enter selected option number:')
    if sel=='1':
        en = input('Enter English:')
        ch = input('Enter Chinese:')
        dic[en]=ch
        fo = open('mydictionary.txt','a')
        for k,v in dic.items():
            fo.write(k)
            fo.write(':')
            fo.write(v)
            fo.write('/n')
        fo.close(  )
    elif sel=='2':
        for k,v in dic.items():
            print(k,':',v)
    elif sel=='3':
        search = input('Enter English:')
        print(dic[search])
    elif sel=='4':
        search = input('Enter Chinese:')
        for k,v in dic.items():
            if search==v:
                print(k)
    elif sel=='5':
        score=0
        for k,v in dic.items():
            print(v,':')
            ans = input('Please enter your answer:')
            if ans==k:
                print('Correct!')
                score = score + 1
        print('Your score is:',score)
    elif sel=='6':
        break