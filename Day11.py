'''
input : 첫째 줄에 카드의 개수 N과 M이 주어진다.
        둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 
        이 값은 100,000을 넘지 않는 양의 정수이다
        합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
output : 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
'''

import sys

N, M = map(int, sys.stdin.readline().split(' '))
#print(N, M)

num = list(map(int, sys.stdin.readline().split(' ')))
num.sort()
#print(num)

result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a = num[i] + num[j] + num[k]
            if a <= M and a > result :
                result = a

print(result)