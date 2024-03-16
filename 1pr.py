def book_count(alist):
    res = {}
    for i in range(len(alist)):
        if len(alist[i][4])>0:
            if alist[i][1] not in res:
                res[alist[i][1]] = int(alist[i][4])
            else:
                res[alist[i][1]] += int(alist[i][4])
    return res


def report(alist):
    with open('count_book.txt', 'w', encoding='utf8') as f:
        for keys in alist:
            f.write(f'Книг для изучения {keys} в библиотеке нашлось: {alist[keys]}\n')


with open('languages.csv', encoding='utf8') as f:
    name = f.readline()
    n = f.readlines()
for i in range(len(n)):
    if i != len(n) - 1:
        n[i] = n[i][:-1]
        n[i] = n[i].split(';')
    else:
        n[i] = n[i].split(';')
res = book_count(n)
report(res)
