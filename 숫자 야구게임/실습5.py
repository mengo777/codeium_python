answer = []
count = 0
import random

while len(answer) < 3:
    n =  str(random.randint(1, 9))
    if n not in answer:
        answer.append(n)
print(answer)
while True:
    count +=1
    nums = input("숫자 입력 : ")
    guess = list(nums)
    print(guess)

    # strike ( = 위치와 숫자 전부 맞은 경우)
    strike = 0
    ball = 0
    out = 0

    # 일단은 strike만 몇 개인지 세보기
    for i  in range(3):
        if answer[i] == guess[i]:
            strike += 1
        elif guess[i] in answer and guess[i] != answer[i]:
            ball += 1
        else:
            out +=1

    if strike == 3:
        print(count,"번쨰 시도끝에 정답을 맞췄습니다")
        break

    if count >= 20:
        print("시도횟수가 20번 이상이 되셔서 게임 오버")
        break

    # strike 확인
    print(strike)

    # ball 개수 출력하기
    print(ball)
