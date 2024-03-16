def quicksort(alist, start, end):
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


best=[]
prom = []
with open('languages.csv', encoding='utf8') as f:
    name = f.readline()
    n = f.readlines()
for i in range(len(n)):
    if i != len(n) - 1:
        n[i] = n[i][:-1]
        n[i] = n[i].split(';')
        prom.append(n[i][0])
    else:
        n[i] = n[i].split(';')


quicksort(prom,0,len(prom))
for i in range(len(prom)):
    x=0
    while prom[i] not in n[x]:
        x+=1
    best.append(n[x])


print(f'{best[0][2]}:')
for j in range(2):
    print(f'\t{best[j][0]} - {best[j][3]}')
print(f'{best[2][2]}:')
print(f'\t{best[2][0]} - {best[2][3]}')
