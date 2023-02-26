import sys
sys.stdin = open('구간합.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_v = 0
    min_v = sum(arr)


    for i in range(N-M+1):
        result = 0
        for j in range(i, i+M):
            result += arr[j]
        if max_v < result:
            max_v = result
        if min_v > result:
            min_v = result

    print(f'#{tc}',max_v - min_v)