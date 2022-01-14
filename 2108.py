import sys
from collections import Counter

read = sys.stdin.readline
n = int(read())
arr = []
for i in range(n):
    arr.append(int(read()))

_max = max(arr)
_min = min(arr)

arr.sort()

tmp = dict(Counter(arr))
tmp = list(sorted(tmp.items(), key=lambda k:k[1]  , reverse=True))

print(round(sum(arr) / n))
print(arr[n // 2])
if len(tmp) > 1 :
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(tmp[0][0])
print(_max - _min)