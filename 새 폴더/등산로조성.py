import sys
sys.stdin = open('등산로조성.txt')

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(x, y):
    stack = [(x,y)]
    visited[x][y] = 1
    while stack:
        sx, sy = stack.pop()

        for k in range(4):
            nx, ny = sx + dx[k], sy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] < arr[sx][sy]:
                    stack.append((nx,ny))
                    visited[nx][ny] = visited[sx][sy]+1

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > result:
                result = arr[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == result:
                x, y = i, j
                DFS(x, y)
    print(arr)
    print((visited))

