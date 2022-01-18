import sys
read = sys.stdin.readline

def mergesort(array):

    if len(array) <= 1 :
        return array

    mid = len(array) // 2

    left = mergesort(array[:mid])
    right = mergesort(array[mid:])

    i,j = 0,0
    ar = []

    while len(left) > i and len(right) > j :
        #나이를 판별해서 작은 것을 append
        if left[i][0][0] < right[j][0][0]:
            ar.append(left[i])
            i += 1
        elif left[i][0][0] > right[j][0][0] :
            ar.append(right[j])
            j += 1
        else : # 나이가 같은경우
            # 들어온 순서 대로 정렬을 한다.
            if left[i][1] < right[j][1] :
                ar.append(left[i])
                i+=1
            else:
                ar.append(left[j])
                j+= 1

    ar += left[i:]
    ar += right[j:]

    return ar


n = int(read())
name_list = []
for i in range(n):
    age,name = map(str,read().split())
    age = int(age)
    name_list.append(( (age,name) ,i)) # ((나이,이름), 들어온순서)

name_list  = mergesort(name_list)

for i in range(0,n):
    print(name_list[i][0][0] , name_list[i][0][1])

# solution 2
# 파이썬은 기본적으로 stable 정렬을 하기 때문에 sort함수로 구현 가능.
# n = int(read())
# name_list = []
#
# for i in range(n):
#     age,name = map(str, read().split())
#     age = int(age)
#     name_list.append((age,name))
#
#
# name_list.sort(key= lambda k : k[0])
# for i in range(n):
#     print(name_list[i][0] , name_list[i][1])





