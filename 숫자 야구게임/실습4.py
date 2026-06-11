answer = []
import random

while len(answer) < 3:
    n =  str(random.randint(1, 9))
    if n not in answer:
        answer.append(n)
print(answer)
nums = input("숫자 입력 : ")
guess = list(nums)
print(guess)

# strike ( = 위치와 숫자 전부 맞은 경우)
strike = 0
ball = 0

# 일단은 strike만 몇 개인지 세보기
for i  in range(3):
    if answer[i] == guess[i]:
        strike += 1
    if guess[i] in answer and guess[i] != answer[i]:
        ball += 1

# strike 확인
print(strike)

# ball 개수 출력하기
print(ball)