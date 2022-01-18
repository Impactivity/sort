import sys
read = sys.stdin.readline
n = int(read())

words = []

for _ in range(n):
    words.append(read().strip())

set_words = set(words)
words = list(set_words)

#문제에서 길이에 따라 오름차순으로 정렬할 때 길이가 같을 경우 사전순으로 정렬
words.sort() #먼저 사전순으로 정렬
words.sort(key=len) #길이 순으로 정렬

for i in words:
    print(i)



