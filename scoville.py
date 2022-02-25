from heapq import *

def solution(scoville, K):
    count = 0
    heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        num1 = heappop(scoville) # 파이썬의 힙은 0번째가 최솟값이된다. pop후 자동정렬됨.
        num2 = heappop(scoville)
        heappush(scoville, num1 + num2 * 2) # 문제에서 요구하는 ( 최솟값 + 두번째작은값 * 2 ) 을 push해준다.
        count += 1
    return count if scoville[0] >= K else -1


# 이분탐색으로 k보다 작은 값 전까지
# 배열을 따로 만들어서
# 해당 배열에서 계산하려고 했음.
# 결과는 오답.
#
# def solution(scoville, K):
#     scoville.sort()
#
#     l = 0
#     r = len(scoville) - 1
#
#     while l <= r:
#         mid = (l + r) // 2
#
#         if scoville[mid] >= K:
#             r = mid - 1
#         elif scoville[mid] < K:
#             l = mid + 1
#
#     arr = scoville[0:r + 1]
#
#     cnt = 0
#
#     while arr[0] < K and len(arr) > 1:
#         arr.sort()
#         num = arr.pop(0)
#         num2 = arr.pop(0)
#         arr.append(num + (num2 * 2))
#         cnt += 1
#
#     return cnt if arr[0] >= K else -1