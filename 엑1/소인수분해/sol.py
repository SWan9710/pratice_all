# 간단한 소인수 분해
# 입력받은 값을 2, 3, 5, 7, 11 로 나눈 후 몇번 나눴는지 구하기
import sys
sys.stdin = open('input.txt')

num_list = [2, 3, 5, 7, 11]

test_case = int(input())
for tc in range(1, test_case+1):

    N = int(input())
    result = [0] * 5
    for i in range(len(num_list)):
        while N % num_list[i] == 0:
            result[i] += 1
            N = N // num_list[i]

    print(f'#{tc}', *result)

