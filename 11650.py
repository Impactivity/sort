import sys
read = sys.stdin.readline

n = int(read())
axis = [list(map(int,read().split())) for _ in range(n)]

#solution 1 mergesort를 이용하여 구현 1052ms
# def mergesort(array):
#
#     if len(array) <= 1 :
#         return array
#
#     mid = len(array) // 2
#
#     left = mergesort(array[:mid])
#     right = mergesort(array[mid:])
#
#     i,j = 0,0
#
#     conquer = []
#
#     while i < len(left) and j < len(right):
#         if left[i][0] < right[j][0]:
#             conquer.append(left[i])
#             i += 1
#         elif left[i][0] > right[j][0]:
#             conquer.append(right[j])
#             j += 1
#         else : # 두 수가 같은 경우
#             if left[i][1] <= right[j][1]:
#                 conquer.append(left[i])
#                 i += 1
#             else :
#                 conquer.append(right[j])
#                 j += 1
#
#     conquer += left[i:]
#     conquer += right[j:]
#
#     return conquer
#
# answer = mergesort(axis)


# solution 2 라이브러리 사용 464ms
answer = sorted(axis)

for i in range(0,n):
    print(answer[i][0] , answer[i][1])
