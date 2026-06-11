# 답지 만들기
answer = [1,3,5]

# 유저의 추측을 가정하기
guess = [1,7,3]

# strike ( = 위치와 숫자 전부 맞은 경우)
strike = 0

# 일단은 strike만 몇 개인지 세보기
for i  in range(3):
    if answer[i] == guess[i]:
        strike += 1

# strike 확인
print(strike)