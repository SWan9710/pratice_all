import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(input().split()))

    r1 = []
    for i in range(N):
        for j in range(N-1,-1,-1):
            r1.append(arr[j][i])

    r2 = []
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            r2.append(arr[i][j])

    r3 = []
    for i in range(N-1,-1,-1):
        for j in range(N):
            r3.append(arr[j][i])
    print(f'#{tc}')
    for i in range(N):
        print(*r1[i*N:(i+1)*N],' ',*r2[i*N:(i+1)*N],' ',*r3[i*N:(i+1)*N],sep='')
