logs_0 = ['[2020-03-16 16:15:25] INFO Disk size is 100 Gb',
          '[2020-03-16 16:15:25] ERROR Db failute]',
          '[2020-03-16 16:15:25] ERROR Network failute',
          '[2020-03-16 16:16:29] ERROR Cant write varlog',
          '[2020-03-16 16:16:42] ERROR Unable to start process',
          '[2020-03-16 16:16:43] WARNING Disk size is too small',
          '[2020-03-16 16:16:43] ERROR Config not found',
          '[2020-03-16 16:16:53] ERROR Timeout detected']

import datetime

lst = []
t, e = list(map(int, input().split()))

while True:
    try:
        temp = input()
        temp = temp.split('] ')
        temp[0] = temp[0].replace('[', '')
        if temp[1][0:5] == 'ERROR':
            date = datetime.datetime.strptime(temp[0], '%Y-%m-%d %H:%M:%S')
            lst.append(date)
    except EOFError:
        break

count = 0
K = -1
flag = False
for i in range(len(lst)):
    for j in range(i - 1, -1, -1):
        time_delta = lst[i] - lst[j]
        if time_delta.total_seconds() < t and i + 1 - j >= e:
            print(lst[i])
            flag = True
            break
    if flag:
        break
if not flag:
    print(-1)
