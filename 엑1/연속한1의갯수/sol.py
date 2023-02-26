import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = input()

    result = 0
    count = 0

    for i in range(N):
        if num_list[i] == '1':
            count += 1
            if result < count:
                result = count
        else:
            count = 0
    print(f'#{tc}',result)