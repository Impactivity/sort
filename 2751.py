import sys


def merge_sort(arr):
    if len(arr) <= 1 :
        return arr
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i,j = 0,0
    conquer = []

    # 분할 된 left , right를 비교하면서 작은수를 적재
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            conquer.append(left[i])
            i+=1
        else:
            conquer.append(right[j])
            j+=1

    # while 조건이 끝나면 나머지 대상들을 합쳐준다.
    conquer += left[i:]
    conquer += right[j:]

    return conquer




read = sys.stdin.readline
n = int(read())

arr = []
for i in range(n):
    arr.append(int(read()))


arr = merge_sort(arr)

for num in arr:
    print(num)