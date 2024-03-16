def result(alist):
    return [alist[0],int(alist[-1])/(2023-int(alist[2]))]


with open('languages.csv', encoding='utf8') as f:
    name = f.readline()
    n = f.readlines()
for i in range(len(n)):
    if i != len(n) - 1:
        n[i] = n[i][:-1]
        n[i] = n[i].split(';')
    else:
        n[i] = n[i].split(';')

for i in range(len(n)):
    if i != len(n)-1:
        print(*result(n[i]))