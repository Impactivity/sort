import sys

read = sys.stdin.readline
n = int(read())

arr = [0] * 10001

for i in range(n):
    arr[int(read()) - 1] += 1

for i in range(0,10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)


