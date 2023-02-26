import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    max_result = 0
    # N이 M 보다 길면 서로의 값을 바꿔주기
    if N > M:
        N, M = M, N
        arr1, arr2 = arr2, arr1
    for i in range(M-N+1):
        result = 0
        for j in range(N):
            result += (arr2[i+j] * arr1[j])
        if max_result < result:
            max_result = result

    print(f'#{tc}',max_result)

