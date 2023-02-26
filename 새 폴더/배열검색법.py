arr = [[0] * 5 for _ in range(5)]
k = 1
for i in range(5):
    for j in range(5):
        arr[i][j] += k
        k += 1

# 행 우선 조회
# for i in range(5):
#     for j in range(5):
#         print(arr[i][j])

# 열 우선 조회
# for i in range(5):
#     for j in range(5):
#         print(arr[j][i])

# 지그재그 순회
# for i in range(5):
#     for j in range(5):
#         # 0부터 시작하니까 짝수일때는 앞에서
#         # 홀수일때는 뒤에서 가져오기
#         print(arr[i][j + (5-1-2*j) * (i%2)])

# 델타탐색
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
#
# for i in range(5):
#     for j in range(5):
#         for k in range(4):
#             nx = i + dx[k]
#             ny = i + dy[k]
#
#             if 0 <= nx < 5 and 0 <= ny < 5:
#                 print(arr[nx][ny])

# 전치행렬
# for i in range(5):
#     for j in range(5):
#         if i < j:
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
