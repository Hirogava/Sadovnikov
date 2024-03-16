def message_send(alist):
    return f'{alist[0]} был создан: {alist[3]} в {alist[2]}'


best = []
with open('languages.csv', encoding='utf8') as f:
    name = f.readline()
    n = f.readlines()
for i in range(len(n)):
    if i != len(n) - 1:
        n[i] = n[i][:-1]
        n[i] = n[i].split(';')
        best.append(n[i][0])
    else:
        n[i] = n[i].split(';')
        best.append(n[i][0])
message = input()
while message != 'stop':
    if message not in best:
        print('Хм.. Вы уверены, что слышали об этом ЯП?')
        message = input()
    else:
        ind = best.index(message)
        print(message_send(n[ind]))
        message = input()