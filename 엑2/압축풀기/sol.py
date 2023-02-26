import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    result = ''

    for i in range(N):
        words, num = input().split()
        num = int(num)

        result += words*num

    print(f'#{tc}')
    for i in range(0,len(result),10): # > 0,9,19
        print(result[i : 10+i])



