import sys

read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))

#입력받은 arr의 중복을 제거하고 리스트로 형 변환하여 오름차순 정렬
c = list(set(arr))
c.sort()

answer = {}
# 정렬이 되었기 때문에 해당 수보다 작은 갯수는 결국 현재 index가 된다.
for i in range(0,len(c)):
    answer[c[i]] = i

# 문제에서 요구한 정답을 출력하기 위해 처음에 입력받은 arr 숫자에 매칭되는 값을 출력
for i in arr:
    print(answer[i], end= ' ')



