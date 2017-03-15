while True:
    reply = input('最早年份:')
    if not reply.isdigit():
        print('Please Entry Number')
        continue
    else:
        reply2 = input('最近年份:')
        if not reply2.isdigit():
            print('Please Entry Number')
            continue
        else:
            break
reply = int(reply)
reply2 = int(reply2)
rangelist = list(range(reply,reply2 + 1))
for a in range(len(rangelist)):
    rangelist[a] = str(rangelist[a]) + '.txt'
for a in rangelist:
    file_object = open(a)
    raw = file_object.read().splitlines()
    raw1 = ''
    for b in raw:
        raw1 = raw1 + b
raw1 = raw1.split(' ')
punctuation = '''!"#$%&'()*+,./:;<=>?@[\]^_`{|}~'''
c = ''
for a in raw1:
    for e in punctuation:
        if e == ".":
          a = a.replace(e,' ')#每句之间加空格
        elif e == """'""":
          a = a.replace(e,' ')#应对可能出现的缩写
        else:
          a = a.replace(e,'') #去掉其他各种标点
    a = a.lower()             #全部小写
    if len(a) < 3:            #去掉单个和双字母的单词
        pass
    elif a == ' ':
        pass
    else:
        c = c + ' ' +a
c = c.split(' ')
D = {}
for f in c:
    if f in D:
        D[f] += 1
    else:
        D[f] = 1
if '' in D:
    del D['']
#挑选简单词
iseasy = []
noteasy = []
listd = list(D.keys())
for a in range(len(listd)):
    reply = input('Do You Recognise' + ' '+ str(listd[a]) + ' ? y///n' + str(len(list(D.keys())) - len(iseasy)))
    if reply == 'y':
        iseasy.append(listd[a])
        continue
    if reply == 'n':
        noteasy.append(listd[a])
        continue
    else :
        print('parden?')
        continue
E = open(r'easytext.txt','w')
for a in range(len(iseasy)):
    iseasy[a] = str(iseasy[a]) + '\n'
bigeasy = ''
for a in range(len(iseasy)):
    bigeasy = bigeasy + iseasy[a]
E.writelines(bigeasy)
E.close()
#处理简单词
file_easy = open('easytext.txt')
raw_easy = file_easy.read()
raw_easy1 = ''
for b in raw_easy:
    b = b.lower()
    raw_easy1 = raw_easy1 + b
raw_easy1 = raw_easy1.split('\n')
for a in raw_easy1:
    if a in D:
        del D[a]
#写入难词
D = str(D)
D = D[1:-1]
D = D.split(',')
for a in range(len(D)):
    D[a] = str(D[a]) + '\n'
hardtext = ''
for a in range(len(D)):
    hardtext = hardtext + D[a]
H = open(r'hard.txt', 'w')
H.writelines(hardtext)
H.close()