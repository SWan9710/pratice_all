import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):

    # 가로배열
    arr = []
    for i in range(9):
        arr.append(list(input().split()))

    # 세로배열
    arr2 = [[0]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            arr2[i][j] = arr[j][i]

    arr3 = []
    for x in (0,3,6):
        for y in (0,3,6):

            temp = []
            for i in range(3):
                for j in range(3):
                    temp.append((arr[x+i][y+j]))
            arr3.append(temp)

    duplication = 0
    for i in range(9):
        if len(set(arr[i])) != 9:
            duplication += 1
            break

        if len(set(arr2[i])) != 9:
            duplication += 1
            break

        if len(set(arr3[i])) != 9:
            duplication += 1
            break

    if duplication == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')