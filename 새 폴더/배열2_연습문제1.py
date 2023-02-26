import sys
sys.stdin = open('연습문제1.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    result = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    result += abs(arr[nx][ny] - arr[i][j])
    print(f'#{tc}',result)