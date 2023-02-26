import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot_size = list(map(int, input().split()))

    count = 1
    result = 1

    for i in range(1,N):
        if carrot_size[i-1] < carrot_size[i]:
            count += 1
            if result < count:
                result = count
        else:
            count = 1
    print(f'#{tc}', result)


