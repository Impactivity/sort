import sys
read = sys.stdin.readline
arr = list(map(int,read().strip()))
arr.sort(reverse=True)
print(''.join(map(str,arr)))