# 0 ~ 9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을때
# 3장의 카드가 연속되는 번호 run
# 3장이 동일 triplet
# 6장이 run이나 triplet으로 이루어진 경우 baby_gin

num = 235777
# run 조사할때 배열범위 벗어나니까 처음부터 그냥 카드수 + 3 만큼 만들어줌
card = [0] * 12

for i in range(6):
    card[num % 10] += 1
    num //= 10
    # 카운트 배열 만들기

    # run과 tri가 되는 경우의 수 세주기
    run = 0
    triplet = 0

    # triple 조사하기
i = 0
while i < 10:
    if card[i] >= 3:
        card[i] -= 3
        triplet += 1
        continue
    # run 조사하기
    if card[i] >= 1 and card[i+1] >= 1 and card[i+2] >= 1:
        card[i] -= 1
        card[i+1] -= 1
        card[i+2] -= 1
        run += 1
        continue
    i += 1

if run + triplet == 2:  print('baby-gin')
else:   print('lose')
